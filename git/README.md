# The manual of Git

面向 Git 的基本教程。

## 说明

以下操作均在 Git 2.17.1 下调试通过。

## Config

配置一下。

```
$ git config --global user.name "paoqi1997"
$ git config --global user.email "604869221@qq.com"
```

查看配置。

```
$ git config -l
```

## Learn Git

创建一个 Git 仓库。

```
$ mkdir learngit
$ cd learngit
$ git init

$ touch readme.txt
$ echo "Hello Git!" > readme.txt

$ git add readme.txt
$ git commit -m "create readme.txt"

# 查看提交历史
$ git log
# 查看提交历史（一行信息）
$ git log --oneline
```

查看difference。

```
$ echo "Git is better than SVN." >> readme.txt
$ git diff readme.txt
$ git status

$ git add readme.txt
$ git commit -m "update readme.txt"
```
