# CI 预览服验收

此预览分支在服务器初始化日志和 `/vexexample` 命令中输出 `Vex Example CI preview 1`。

PR 的 GitHub Actions 产物被 Vex 接收后，预览房间应使用该 PR 的 head SHA。检查房间返回的 Build ID、generation 和 Minecraft 日志中的标识，再通过游戏或 RCON 执行 `vexexample`，确认输出相同标识。

后续修改标识并推送新提交，可以检查评论和 mrpack 更新，以及房间在无人且无租约时使用新 generation。原有世界中的验收方块应继续存在。关闭 PR 后检查正常保存、归档快照和 closed 状态。

完整构建和测试命令：`./gradlew --no-daemon --max-workers=2 clean build`。
