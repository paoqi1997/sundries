# The manual of Node.js

面向Node.js的基本教程。

## 说明

以下操作均在 Node.js 12.19.0 下调试通过。

## [安装](https://nodejs.org/en/)

Windows下直接通过 msi 安装即可。

## Use [npm](https://www.npmjs.com)

配置一下。

```
>npm config set registry https://registry.npm.taobao.org

# 假设 nodejs 安装在 D:\nodejs
>npm config set prefix "D:\nodejs\global"
>npm config set cache "D:\nodejs\npm-cache"
```

查看配置。

```
>npm config get registry

>npm prefix
>npm prefix -g

>npm config list
>npm config list -l
```

安装[Vue](https://www.npmjs.com/package/vue)。

```
>mkdir myproj
>cd myproj
>npm install vue@2.6.12
```
