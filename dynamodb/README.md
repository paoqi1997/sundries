# DynamoDB

面向 DynamoDB 的基本教程。

## [DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html)

执行以下命令。

```
$ docker-compose up

$ sudo chown -c your-user dynamodb
```

## [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

安装 [aws-cli](https://hub.docker.com/r/amazon/aws-cli)。

```
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
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
