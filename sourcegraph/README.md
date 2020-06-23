# The manual of Sourcegraph

面向Sourcegraph的基本教程。

## 说明

以下操作均在 Ubuntu 18.04 bionic 下调试通过。

## [安装](https://docs.sourcegraph.com/admin/install/docker)

相关命令如下所示：

```
# --publish: Publish a container's port(s) to the host
# -d: Run container in background and print container ID
# --rm: Automatically remove the container when it exits
# --volume: Bind mount a volume
# 关于--rm选项，你可以启停容器并观察 /var/lib/docker/containers 的变化
$ docker run \
    --publish 12358:7080 -d --rm \
    --volume ~/.sourcegraph/config:/etc/sourcegraph \
    --volume ~/.sourcegraph/data:/var/opt/sourcegraph \
    sourcegraph/server:3.17.0
```

## [配置](https://docs.sourcegraph.com/admin/config)

初次注册后禁止注册。

```json
{
    "auth.providers": [
        {
            "types": "builtin",
            "allowSignup": false
        }
    ]
}
```

从[此处](https://github.com/settings/tokens)获取token。

```json
{
    "url": "https://github.com",
    "token": "<access token>",
    "orgs": [
        "<owner>"
    ],
    "repos": [
        "<owner>/<repository>"
    ]
}
```

## 异常

创建管理员后某次登录出现异常：

```
# Console
POST http://ip:port/-/sign-in 403 (Forbidden)
# Response
Forbidden - CSRF token invalid
```

在GitHub上搜到相关的[issue](https://github.com/sourcegraph/sourcegraph/issues/65)，但目前对网站用户认证不太了解，先暂时搁置。
