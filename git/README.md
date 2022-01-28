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
```

## 提交规范

参考自 AngularJS 的 [Git Commit Guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits) 和 Angular 的 [Commit Message Format](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit)。
