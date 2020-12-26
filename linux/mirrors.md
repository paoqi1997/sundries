# mirrors

更新镜像源的相关指引。

## elementary OS

将默认软件镜像换成中科大的镜像：

```
$ sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
$ sudo sed -i 's/cn.archive.ubuntu.com/mirrors.ustc.edu.cn/' /etc/apt/sources.list
$ sudo sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/' /etc/apt/sources.list
$ sudo sed -i 's/http/https/' /etc/apt/sources.list
```

针对elementary.list的操作：

```
$ sudo cp /etc/apt/sources.list.d/elementary.list /etc/apt/sources.list.d/elementary.list.bak
$ sudo sed -i 's/ppa.launchpad.net/launchpad.proxy.ustclug.org/' /etc/apt/sources.list.d/elementary.list
$ sudo sed -i 's/http/https/' /etc/apt/sources.list.d/elementary.list
```

针对patches.list的操作：

```
$ sudo cp /etc/apt/sources.list.d/patches.list /etc/apt/sources.list.d/patches.list.bak
$ sudo sed -i 's/ppa.launchpad.net/launchpad.proxy.ustclug.org/' /etc/apt/sources.list.d/patches.list
$ sudo sed -i 's/http/https/' /etc/apt/sources.list.d/patches.list
```

## MSYS2

将以下内容设置在对应文件的开头。

```
# /etc/pacman.d/mirrorlist.mingw32
Server = https://mirrors.ustc.edu.cn/msys2/mingw/i686

# /etc/pacman.d/mirrorlist.mingw64
Server = https://mirrors.ustc.edu.cn/msys2/mingw/x86_64

# /etc/pacman.d/mirrorlist.msys
Server = https://mirrors.ustc.edu.cn/msys2/msys/$arch
```

安装 gcc 等软件。

```
$ pacman -Sy gcc
```

## openSUSE

执行以下命令。

```
# 查看软件源
$ zypper lr -u

# 禁用当前所有的软件源
$ zypper mr -da

# 添加软件源
$ zypper ar -fcg https://mirrors.ustc.edu.cn/opensuse/distribution/leap/15.2/repo/oss ustc-repo-oss
$ zypper ar -fcg https://mirrors.ustc.edu.cn/opensuse/distribution/leap/15.2/repo/non-oss ustc-repo-non-oss
$ zypper ar -fcg https://mirrors.ustc.edu.cn/opensuse/update/leap/15.2/oss ustc-repo-update
$ zypper ar -fcg https://mirrors.ustc.edu.cn/opensuse/update/leap/15.2/non-oss ustc-repo-update-non-oss

# 刷新软件源
$ zypper ref
```

安装 gcc 等软件。

```
$ zypper install gcc
```
