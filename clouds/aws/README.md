# Amazon Web Services

面向 AWS 的指南。

## TPs

### ACM

+ [DNS 验证](https://docs.aws.amazon.com/zh_cn/acm/latest/userguide/dns-validation.html)

### CloudTrail

+ [查看事件历史记录](https://docs.aws.amazon.com/zh_cn/awscloudtrail/latest/userguide/tutorial-event-history.html)

### DynamoDB

+ [Amazon DynamoDB NoSQL Workbench](https://aws.amazon.com/cn/dynamodb/nosql-workbench/)

+ [NoSQL Workbench for DynamoDB](https://docs.aws.amazon.com/zh_cn/amazondynamodb/latest/developerguide/workbench.html)

### EC2

+ [云服务器实例类型](https://aws.amazon.com/cn/ec2/instance-types/)

+ [实例类型](https://docs.aws.amazon.com/zh_cn/AWSEC2/latest/UserGuide/instance-types.html)

+ [检索实例元数据](https://docs.aws.amazon.com/zh_cn/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html)

### ECR

+ [什么是 Amazon Elastic Container Registry？](https://docs.aws.amazon.com/zh_cn/AmazonECR/latest/userguide/what-is-ecr.html)

### ELB

+ [Elastic Load Balancing 功能](https://aws.amazon.com/cn/elasticloadbalancing/features/)

+ [什么是经典负载均衡器？](https://docs.aws.amazon.com/zh_cn/elasticloadbalancing/latest/classic/introduction.html)

+ [什么是 Application Load Balancer？](https://docs.aws.amazon.com/zh_cn/elasticloadbalancing/latest/application/introduction.html)

+ [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.6/)

### Global Accelerator

+ [什么是 AWS Global Accelerator？](https://docs.aws.amazon.com/zh_cn/global-accelerator/latest/dg/what-is-global-accelerator.html)

### Route 53

+ [路由子域的流量](https://docs.aws.amazon.com/zh_cn/Route53/latest/DeveloperGuide/dns-routing-traffic-for-subdomains.html)

+ [Amazon Route 53 为公有托管区域创建的 NS 和 SOA 记录](https://docs.aws.amazon.com/zh_cn/Route53/latest/DeveloperGuide/SOA-NSrecords.html)

+ [在别名记录和非别名记录之间进行选择](https://docs.aws.amazon.com/zh_cn/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)

+ [支持的 DNS 记录类型](https://docs.aws.amazon.com/zh_cn/Route53/latest/DeveloperGuide/ResourceRecordTypes.html)

### ExternalDNS

+ [Setting up ExternalDNS for Services on AWS](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md)

### Terraform

+ [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

## [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html)

如下所示：

```
# EC2
$ curl https://ec2.ap-northeast-1.amazonaws.com/ping
# GameLift
$ curl https://gamelift.ap-northeast-1.amazonaws.com/ping
```
