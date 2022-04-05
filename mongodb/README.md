# The manual of MongoDB

面向 MongoDB 的基本教程。

## 说明

MongoDB 4.x 和 MongoDB 5.x 分别在 Ubuntu 18.04.6 LTS 和 Ubuntu 20.04.4 LTS 下调试通过。

## [安装](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu-tarball/)

### [MongoDB 5.x](https://www.mongodb.com/try/download/community)

#### mongod

获取 MongoDB。

```
$ wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2004-5.0.6.tgz
```

提取相应的包。

```
$ sudo tar -C /usr/local -xzvf mongodb-linux-x86_64-ubuntu2004-5.0.6.tgz

$ sudo mv /usr/local/mongodb-linux-x86_64-ubuntu2004-5.0.6 /usr/local/mongodb

$ sudo mkdir -p /var/lib/mongo
$ sudo mkdir -p /var/log/mongodb

$ sudo chown your-user /var/lib/mongo
$ sudo chown your-user /var/log/mongodb
```

运行。

```
$ mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --fork
```

#### mongosh

获取 MongoDB Shell。

```
$ wget https://downloads.mongodb.com/compass/mongosh-1.3.1-linux-x64.tgz
```

提取相应的包。

```
$ sudo tar -C /usr/local -xzvf mongosh-1.3.1-linux-x64.tgz

$ sudo mv /usr/local/mongosh-1.3.1-linux-x64 /usr/local/mongosh
```

运行。

```
$ mongosh
```

### [MongoDB 4.x](https://www.mongodb.org/dl/linux/x86_64-ubuntu1804)

#### mongod

获取 MongoDB。

```
$ wget http://downloads.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1804-4.2.3.tgz
```

提取相应的包。

```
$ tar -C /usr/local -xzvf mongodb-linux-x86_64-ubuntu1804-4.2.3.tgz

$ mv /usr/local/mongodb-linux-x86_64-ubuntu1804-4.2.3 /usr/local/mongodb

$ cd /usr/local/mongodb
$ mkdir -p data/db
$ mkdir log
```

创建 mongod.conf 文件并添加以下内容：

```yaml
processManagement:
  fork: true
security:
  authorization: enabled
storage:
  dbPath: /usr/local/mongodb/data/db
systemLog:
  destination: file
  path: /usr/local/mongodb/log/mongod.log
```

在 ~/.profile 文件中添加以下命令。

```
export PATH=$PATH:/usr/local/mongodb/bin
```

运行一下。

```
$ source ~/.profile
```

创建 /etc/systemd/system/mongodb.service 文件并添加以下内容：

```
[Unit]
Description=mongodb
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/mongodb/bin/mongod -f /usr/local/mongodb/mongod.conf
ExecStop=/usr/local/mongodb/bin/mongod --shutdown -f /usr/local/mongodb/mongod.conf
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

执行以下命令：

```
$ sudo systemctl enable mongodb
$ sudo systemctl start mongodb
```

#### mongo

运行。

```
$ mongo
```

## [mongosh Methods](https://www.mongodb.com/docs/manual/reference/method/)

相关脚本如下所示：

```js
> use admin

// 创建用户
> db.createUser({
    user: "root",
    pwd: "123456",
    roles: [{ role: "userAdminAnyDatabase", db: "admin" }]
})

// Authenticates a user to a database.
> db.auth("root", "123456")
// Returns information about the specified user.
> db.getUser("root")

// https://www.mongodb.com/docs/manual/reference/system-users-collection/
> db.system.users.find()
```
