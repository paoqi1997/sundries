# The manual of FFmpeg

面向FFmpeg的基本教程。

## 说明

以下操作均在 FFmpeg 4.3.1 下调试通过。

## [安装](https://ffmpeg.org/download.html)

Windows下通过 MSYS2 安装即可。

```
$ pacman -Sy gcc make
$ pacman -Sy yasm diffutils pkg-config
```

构建FFmpeg。

```
$ tar -xzvf ffmpeg-4.3.1.tar.gz
$ cd ffmpeg-4.3.1

$ ./configure --enable-shared
$ make -j4
$ make install
```

编译 libavcodec 时可能会遇到以下错误：

```
CC      libavcodec/mf_utils.o
In file included from /usr/include/w32api/dshow.h:33,
                 from libavcodec/mf_utils.h:32,
                 from libavcodec/mf_utils.c:25:
/usr/include/w32api/strsafe.h: 在函数‘StringGetsExWorkerW’中:
/usr/include/w32api/strsafe.h:1859:11: 错误：‘WEOF’ undeclared (first use in this function); did you mean ‘EOF’?
 1859 |    if(ch==WEOF) {
      |           ^~~~
      |           EOF
/usr/include/w32api/strsafe.h:1859:11: 附注：每个未声明的标识符在其出现的函数内只报告一次
make: *** [ffbuild/common.mak:59：libavcodec/mf_utils.o] 错误 1
```

在 strsafe.h 文件中添加`#include <wchar.h>`后重新 make 即可。

## Use FFmpeg

相关命令如下所示：

```
# 查看 1.wav 文件的元信息
$ ffmpeg -hide_banner -i 1.wav

# 将 wav 转换成 mp3 格式
$ ffmpeg -hide_banner -i 1.wav 1.mp3
```
