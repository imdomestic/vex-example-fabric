# Vex Example Fabric

Minecraft 26.3、Java 25、Fabric Loader 0.19.5、Fabric API 0.161.0+26.3 的最小服务端示例。

进入房间后执行 `/vexexample`，聊天栏显示 `Vex Example v2`。第一个提交显示 `Vex Example v1`，可以用于核对历史提交房间。命令无需管理员权限；也可以通过服务器控制台运行。客户端使用原版 Minecraft 或兼容的 Fabric 实例。

构建：`./gradlew --no-daemon --max-workers=2 build`。产物位于 `build/libs/vex-example-fabric-1.1.0.jar`。测试通过真实 Minecraft Bootstrap 和 Brigadier 解析命令，并验证额外参数和未知命令的拒绝行为。

该仓库可登记为 Vex 的独立项目，用来验证项目隔离、分支构建、历史提交房间和服务端模组。
