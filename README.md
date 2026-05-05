仓库地址：https://github.com/2338166720-droid/git-learning-2026
一、学习资料来源及相关链接
本次 Git 学习主要依托以下优质资源，涵盖基础教程、实战案例和官方文档，兼顾入门与进阶：
官方文档：Git 官方手册 - 权威的命令解释和使用规范
菜鸟教程：Git 教程 - 入门级图文讲解，适合零基础上手
B 站视频：尚硅谷 Git 全套教程 - 实战导向的视频讲解，包含本地仓库和远程仓库操作
GitHub 入门指南：GitHub Docs - 远程仓库协作的核心教程
二、实践流程
1. 环境安装
Windows 系统：从 Git 官网 下载对应版本安装包，一路默认安装（勾选 “Git Bash Here” 便于右键快速打开终端）；安装完成后通过 git --version 验证版本（本次安装版本：git version 2.42.0.windows.1）。
配置用户信息：首次使用需配置全局用户名和邮箱（关联 GitHub 账号）：
bash
运行
git config --global user.name "2338166720-droid"
git config --global user.email "2338166720@qq.com"
# 验证配置：git config --list
2. 仓库初始化与远程关联
本地仓库创建：新建文件夹 git-learning-2026，在文件夹内右键打开 Git Bash，执行 git init 初始化本地仓库。
远程仓库关联：在 GitHub 创建空仓库 git-learning-2026，通过以下命令关联本地与远程：
git remote add origin https://github.com/2338166720-droid/git-learning-2026.git
3. 核心操作流程
本次实践遵循 “修改 → 暂存 → 提交 → 推送” 的核心流程，主要操作包括：
1.新建 / 修改文件（如 notes.md、practice.sh 等）；
2.git add 文件名（或 git add .）暂存修改；
3.git commit -m "提交说明" 提交到本地仓库；
4.git push -u origin main（首次推送）/ git push（后续推送）同步到远程仓库；
5.期间使用 git status 查看状态、git log 查看提交记录。
三、提交记录说明
1.0725a29	May 5，2026，3:53 PM GMT+8 Add print statement to test.py(1)新建 test.py 文件；(2)写入基础测试代码:print("Hello Git")；(3)完成项目首次代码提交，初始化仓库内容。
2.43baef6	May 5，2026，4:01 PM GMT+8 Add MatCalculate class for matrix operations	(1)引入 numpy 库作为数值计算依赖；(2)完整实现 MatCalculate 矩阵运算类，包含以下核心功能：初始化矩阵并解析行列 / 向量信息；数乘、矩阵乘法、基变换、逆矩阵求解；特征值 / 特征向量计算、施密特正交化；矩阵求秩、转置等辅助方法；(3)新增打印语句：print("在提交过之后，对本程序进行第二次提交！")；(4)代码行数新增 137 行，完成核心功能开发。
3.6c23e77	May 5，2026，4:01 PM GMT+8 Add print statements for submission updates	(1)在 test.py 中新增打印语句：print("第三次提交：完成Git实践任务")；(2) 补充提交标识信息，完善代码提交闭环；(3)代码行数新增 2 行，完成代码层的最终提交。
4.f00eada	May 5，2026，4:13 PM GMT+8 Create README.md	(1)新建 README.md 文件，文件行数新增 67 行；(2)完整梳理本次 Git 实践的全流程：学习资料来源及相关链接；Git 环境安装、仓库初始化与远程关联流程；核心操作命令与提交规范；(3)完成实践总结，形成可回溯、可复用的 Git 学习笔记。
四、遇到的问题及解决方法
问题 1：推送代码时提示 “Permission denied (publickey)”
现象：执行git push origin main时，报错拒绝访问，无法将本地代码推送到 GitHub 远程仓库。
原因：本地未配置 SSH 密钥，GitHub 无法验证身份（HTTPS 方式也可，但 SSH 更便捷，本次选择配置 SSH）。
解决方法：
生成 SSH 密钥：ssh-keygen -t ed25519 -C "2338166720@qq.com"；
查看并复制公钥：cat ~/.ssh/id_ed25519.pub；
打开 GitHub → Settings → SSH and GPG keys → New SSH key，粘贴公钥并保存；
验证连接：ssh -T git@github.com，出现 “Hi 2338166720-droid! You've successfully authenticated...” 即配置成功；
重新推送：git push origin main，推送成功。
问题 2：执行git commit时提示 “Please tell me who you are”
现象：首次提交时忘记配置全局用户信息，报错要求填写用户名和邮箱。
原因：Git 需要用户信息来标记提交者，未配置时无法完成提交。
解决方法：
配置全局用户信息（永久生效）：
git config --global user.name "2338166720-droid"
git config --global user.email "2338166720@qq.com"
若仅想针对当前仓库配置（局部生效），去掉--global参数：
git config user.name "2338166720-droid"
git config user.email "2338166720@qq.com"
重新执行git commit -m "提交说明"，提交成功。
问题 3：修改文件后执行git push无反应，提示 “Everything up-to-date”
现象：修改了本地文件，但推送时提示 “所有内容已是最新”，远程仓库未同步修改。
原因：修改后仅保存了文件，未执行git add暂存和git commit提交到本地仓库，Git 认为本地与远程无差异。
解决方法：
执行git status查看未暂存的文件，确认修改的文件处于 “Changes not staged for commit” 状态；
暂存修改：git add 文件名（或git add .暂存所有修改）；
提交到本地：git commit -m "修改xxx文件，补充xxx内容"；
推送远程：git push origin main，修改成功同步。
五、Git 学习心得
1基础命令是核心，理解流程比死记硬背重要：Git 的核心是 “工作区 → 暂存区 → 本地仓库 → 远程仓库” 的数据流，理解每个命令（add/commit/push/pull）对应的数据流节点，就能避免大部分基础错误（如忘记暂存直接推送）。
2.报错不可怕，善用官方文档和关键词搜索：本次遇到的 SSH 权限、用户配置问题，都是新手高频问题，通过 GitHub 官方文档和 “报错关键词 + Git” 搜索，能快速找到解决方案；同时git status和git log是排查问题的关键命令，要养成随时查看的习惯。
3.规范提交信息，便于协作和回溯：本次实践中统一了提交说明的格式（如init:/feat:/fix:/docs:），后续查看提交记录时能快速识别每个版本的变更目的，这在多人协作中尤为重要。
4.远程仓库关联和权限配置是新手门槛：HTTPS 和 SSH 两种方式各有优劣，HTTPS 无需配置密钥但每次推送可能需要输密码，SSH 配置后更便捷，建议新手先掌握一种方式，再逐步熟悉另一种。
5.实践是最好的学习方式：单纯看教程容易遗忘，通过 “新建仓库 → 编写文档 → 反复提交 / 修改 / 推送” 的实战流程，能快速掌握核心操作；后续计划进一步学习分支管理（branch/checkout/merge）和冲突解决，提升 Git 实战能力。
