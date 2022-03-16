# DynamoDB

面向 DynamoDB 的基本教程。

## [DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html)

执行以下命令。

```
$ docker-compose up
# your-user 是你当前的用户名
$ sudo chown -c your-user dynamodb
```

## [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

安装 aws-cli。

```
# https://github.com/aws/aws-cli
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install

# https://hub.docker.com/r/amazon/aws-cli
$ docker pull amazon/aws-cli
```

配置 aws-cli。

```
$ aws configure
AWS Access Key ID [None]: DUMMYIDEXAMPLE
AWS Secret Access Key [None]: DUMMYEXAMPLEKEY
Default region name [None]: cn-south-2
Default output format [None]: json
```

执行以下命令。

```
$ aws dynamodb describe-limits --endpoint-url http://localhost:8000
$ aws dynamodb list-tables --endpoint-url http://localhost:8000
```

## [DynamoDB Manager](https://github.com/YoyaTeam/dynamodb-manager)

执行以下命令。

```
$ docker pull taydy/dynamodb-manager
$ docker run -d --rm -p 8008:80 --name dmgr taydy/dynamodb-manager
```
