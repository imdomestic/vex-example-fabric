# Vex fork approval acceptance

This branch runs the actual project build and Vex bundler in a personal fork pull request. The dedicated `vex-fork-it.yml` workflow supplies the isolated controller acceptance test. The test verifies that the artifact remains unavailable until a repository maintainer approves the current pull request head.

The acceptance test uses GitHub, the actual Git repository and an independent SQLite database. Minecraft processes and Kubernetes resources are outside this test.
