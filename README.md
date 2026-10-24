# Vex Example Fabric

Minecraft 26.3、Java 25、Fabric Loader 0.19.5、Fabric API 0.161.0+26.3 的最小服务端示例。

进入房间后执行 `/vexexample`，聊天栏显示 `Vex Example v2`。前一个提交显示 `Vex Example v1`，可以用于核对历史提交房间。命令无需管理员权限；也可以通过服务器控制台运行。客户端使用原版 Minecraft 或兼容的 Fabric 实例。

构建：`./gradlew --no-daemon --max-workers=2 build`。产物位于 `build/libs/vex-example-fabric-1.1.1.jar`。Minecraft、Java、Fabric Loader、Fabric API 和模组版本由 `gradle.properties` 配置，Gradle 和模组元数据使用相同属性。测试通过真实 Minecraft Bootstrap 和 Brigadier 解析命令，并验证额外参数和未知命令的拒绝行为。

该仓库可登记为 Vex 的独立项目，用来验证项目隔离、分支构建、历史提交房间和服务端模组。

## 从模板接入 Vex

1. 在 GitHub 点击 **Use this template**，创建自己的项目仓库。
2. 修改模组名称、Java 包名和 `gradle.properties`，并同步调整模组元数据。使用 `./gradlew build --no-daemon` 验证项目可以构建。
3. 按项目需要修改 `vex.toml` 的 Minecraft、Java、loader 版本、产物匹配规则和依赖摘要。依赖文件的 SHA-1、SHA-256、SHA-512 必须来自实际下载文件。
4. 保留 `.github/workflows/vex.yml` 中的构建与打包步骤。它调用固定提交的 `imdomestic/vex-action`，上传名为 `vex-build` 的 artifact；项目不需要保存 Vex API 凭据。
5. 在新仓库安装所在 Vex 平台的 GitHub App，并由平台管理员登记仓库、CI workflow 和构建来源。启用 PR 预览时，同时配置预览访问权限。
6. 推送 main 或创建 PR，等待 GitHub Actions 成功。Vex 接收 CI 产物后，可以在客户端查看对应分支或 PR 房间。
