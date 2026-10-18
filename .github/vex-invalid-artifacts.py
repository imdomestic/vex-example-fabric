import argparse
import copy
import hashlib
import io
import json
import zipfile
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("source", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()
source = args.source.resolve(strict=True)
document = json.loads((source / "vex-build.json").read_text())
assert document["schema"] == 1 and set(document["loaders"]) == {"fabric"}
files = document["loaders"]["fabric"]["files"]
project_files = [item for item in files if item["origin"] == "build"]
assert len(project_files) == 1
project_file = project_files[0]
contents = {}
for item in files:
    path = source / item["path"]
    assert path.resolve(strict=True).is_relative_to(source) and not path.is_symlink()
    content = path.read_bytes()
    assert len(content) == item["size"]
    for algorithm in ("sha1", "sha256", "sha512"):
        assert hashlib.new(algorithm, content).hexdigest() == item[algorithm]
    contents[item["path"]] = content

args.output.mkdir(parents=True, exist_ok=False)


def write_bundle(name, metadata, changes=None, extra=None):
    target = args.output / name
    with zipfile.ZipFile(target, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("vex-build.json", json.dumps(metadata, separators=(",", ":")))
        for path, content in contents.items():
            archive.writestr(path, (changes or {}).get(path, content))
        if extra == "path":
            archive.writestr("../escape.jar", contents[project_file["path"]])
        elif extra == "size":
            # 真实写入超过单文件限制的内容，由 ZIP 库计算大小和 CRC。
            with archive.open("oversize.jar", "w", force_zip64=True) as stream:
                block = bytes(1024 * 1024)
                for _ in range(256):
                    stream.write(block)
                stream.write(b"x")
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None
        if extra == "size":
            assert archive.getinfo("oversize.jar").file_size == 256 * 1024 * 1024 + 1
    return {"name": name, "size": target.stat().st_size, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}


results = [write_bundle("bad-path.zip", document, extra="path"), write_bundle("bad-size.zip", document, extra="size")]
changed = bytearray(contents[project_file["path"]])
changed[len(changed) // 2] ^= 1
results.append(write_bundle("bad-hash.zip", document, changes={project_file["path"]: bytes(changed)}))

ordinary_jar = io.BytesIO()
with zipfile.ZipFile(ordinary_jar, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    archive.writestr("META-INF/MANIFEST.MF", "Manifest-Version: 1.0\n\n")
metadata = copy.deepcopy(document)
replacement = next(item for item in metadata["loaders"]["fabric"]["files"] if item["origin"] == "build")
replacement["size"] = len(ordinary_jar.getvalue())
for algorithm in ("sha1", "sha256", "sha512"):
    replacement[algorithm] = hashlib.new(algorithm, ordinary_jar.getvalue()).hexdigest()
results.append(write_bundle("bad-metadata.zip", metadata, changes={project_file["path"]: ordinary_jar.getvalue()}))
(args.output / "files.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results))
