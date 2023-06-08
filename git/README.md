# The manual of Git

面向 Git 的基本教程。

## 说明

以下操作均在 Git 2.17.1 下调试通过。

## [Config](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%88%9D%E6%AC%A1%E8%BF%90%E8%A1%8C-Git-%E5%89%8D%E7%9A%84%E9%85%8D%E7%BD%AE)

初次运行 Git 前对其进行配置。

```
# https://git-scm.com/docs/git-config
$ git config --global user.name "paoqi1997"
$ git config --global user.email "604869221@qq.com"
$ git config --global core.editor vim

$ git config -l
$ git config --list --show-origin
```

## Learn Git

创建一个 Git 仓库。

```
$ mkdir learngit
$ cd learngit
$ git init

$ echo "Hello Git!" > readme.txt

$ git add readme.txt
$ git commit -m "docs: create readme.txt"
```

查看提交历史。

```
# https://git-scm.com/docs/git-log
$ git log -p
$ git log --oneline
$ git log --stat --graph
```

比较差异。

```
$ echo "Git is better than SVN." >> readme.txt
$ git status

# https://git-scm.com/docs/git-diff
$ git diff readme.txt
$ git diff --stat

$ git add readme.txt

$ git diff --cached
$ git diff --staged

$ git commit -m "docs: update readme.txt"

$ echo 002918 > version
$ git add version
# 重新提交
$ git commit --amend

# 比较差异
$ git diff commit-id1 commit-id2
```

使用分支。

```
$ git branch -l
$ git branch -a

# 查看远程分支
$ git branch -r

# 从当前提交创建分支
$ git checkout -b mybranch

# https://www.mikestreety.co.uk/blog/the-git-commit-hash/
# 从指定提交创建分支
$ git checkout -b mybranch commit-hash

# 拉取远程 dev 分支并创建本地分支
$ git checkout -b mybranch origin/dev

# 删除分支
$ git branch -d mybranch
$ git branch -D mybranch

# 将 mybranch 改名为 220302-patch
$ git branch -m mypatch 220302-patch

# 查看本地分支及与上游分支的关系
$ git branch -vv
# 设置跟踪分支
$ git branch --set-upstream-to=origin/master 220302-patch

$ echo "But I am not very proficient with Git yet." >> readme.txt
$ git add readme.txt

$ git commit -m "docs: update readme.txt with the patch"

# 修改最近一次的提交信息
$ git commit --amend
# 修改最近一次的提交（如提交遗漏文件），但不需要修改提交信息
$ git commit --amend --no-edit

# 推送当前分支到同名的远程分支
$ git push origin HEAD
# 强制推送分支，但会检查上游是否已发生改变
$ git push --force-with-lease origin HEAD

# 更新远程分支列表
$ git remote update origin --prune

# 删除远程分支 target
$ git push origin :target

# 重置当前分支为远程分支
$ git reset --hard origin/master
```

使用标签。

```
# 从远端拉取所有标签
$ git fetch --tags

# 查看本地标签
$ git tag
# 查看远程标签
$ git ls-remote --tags origin

# 从指定标签创建分支
$ git checkout -b mybranch your-tag

# https://www.ruanyifeng.com/blog/2020/04/git-cherry-pick.html
# 将指定提交应用到当前分支
$ git cherry-pick commit-hash

# 打标签
$ git tag -a v0.0.1 -m 'The first tag'

# 查看标签
$ git show v0.0.1

# 将本地某个标签推送到远程分支
$ git push origin your-tag
# 将本地所有未推送的标签推送到远程分支
$ git push origin --tags

# 删除本地标签
$ git tag -d v0.0.1
# 删除远程标签
$ git push origin :refs/tags/v0.0.1
```

这里列出一些[撤消操作](https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E6%92%A4%E6%B6%88%E6%93%8D%E4%BD%9C)。

```
$ echo 002919 > version
$ git add version

# 取消暂存
$ git reset HEAD version
# 撤销修改
$ git checkout -- version
```

其他的一些命令放在这里。

```
# 贮藏修改
$ git stash

# https://blog.csdn.net/yao_hou/article/details/108178717
# https://blog.csdn.net/weixin_42310154/article/details/119004977
# 拉取代码
$ git pull --rebase

# 应用之前贮藏的修改
$ git stash apply
# 应用之前贮藏的修改，并在应用后删除这个 stash
$ git stash pop
```

## 提交规范

参考自 AngularJS 的 [Git Commit Guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits) 和 Angular 的 [Commit Message Format](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit)。

## TPs

### 帮助

+ [更改提交消息](https://docs.github.com/cn/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/changing-a-commit-message)

+ [Oh Shit, Git!?!](https://ohshitgit.com/zh)

### 官网

1. [Git](https://git-scm.com)

2. [Git for Windows](https://gitforwindows.org)

3. [Git LFS](https://git-lfs.github.com)

4. [libgit2](https://libgit2.org)

### repos on GitHub

1. [git/git](https://github.com/git/git)

2. [git-for-windows/git](https://github.com/git-for-windows/git)

3. [git-lfs/git-lfs](https://github.com/git-lfs/git-lfs)

4. [libgit2/libgit2](https://github.com/libgit2/libgit2)
