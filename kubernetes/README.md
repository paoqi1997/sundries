# The manual of Kubernetes

面向 [Kubernetes](https://kubernetes.io) 的基本教程。

## 说明

真 Kubernetes 装不来，就用 minikube 凑合了🙃

## [minikube](https://minikube.sigs.k8s.io/docs/)

首先获取 minikube。

```
$ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
$ sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

接下来启动 minikube。注意，minikube 至少需要2个 CPU，如果你是单核机器的话，启动参数需要做一些调整（建议安装好 Docker 再启动）。

```
$ minikube start --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 1 --image-mirror-country=cn --image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers
```

## [kubectl](https://kubernetes.io/docs/reference/kubectl/)

### [安装](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

执行以下命令即可。

```
$ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# 校验 kubectl
$ curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
$ echo "$(<kubectl.sha256) kubectl" | sha256sum --check

$ sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

### [基本命令](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)

以下是一些基本的命令：

```
# 查看集群是否正常工作
$ kubectl cluster-info
# 列出支持的 API versions
$ kubectl api-versions
# 列出支持的 API resources
$ kubectl api-resources

# 列出集群节点
$ kubectl get nodes
$ kubectl get node
$ kubectl get no -o wide

# 列出当前命名空间下的 pod
$ kubectl get pods
$ kubectl get pod
$ kubectl get po your-pod -o yaml
# 列出所有命名空间下的 pod
$ kubectl get po --all-namespaces

# 列出服务
$ kubectl get services
$ kubectl get service
$ kubectl get svc

# 列出部署
$ kubectl get deployments
$ kubectl get deployment
$ kubectl get deploy

# 列出事件
$ kubectl get events
$ kubectl get ev

# Show details of a specific resource or group of resources.
$ kubectl describe nodes your-node
$ kubectl describe po your-pod -n your-namespace

# Display Resource (CPU/Memory/Storage) usage.
$ kubectl top no
$ kubectl top po
```

## 实战

### [部署 nginx 服务](https://kubernetes.io/zh/docs/tasks/run-application/run-stateless-application-deployment/)

执行以下命令即可。

```
# https://kubernetes.io/zh/docs/concepts/workloads/controllers/deployment/
$ kubectl apply -f nginx-deployment.yaml

$ kubectl get po --show-labels
$ kubectl get po -l app=nginx

# Print the logs for a container in a pod or specified resource.
$ kubectl logs your-pod

# Create a resource from a file or from stdin.
$ kubectl create -f nginx-service.yaml

# Returns the Kubernetes URL for a service in your local cluster.
$ minikube service list
$ minikube service nginx-service --url
```

结束服务。

```
$ kubectl delete svc nginx-service

$ kubectl delete deploy nginx-deployment

$ kubectl delete po -l app=nginx
```

### [部署 Kong Ingress Controller](https://docs.konghq.com/kubernetes-ingress-controller/latest/get-started/)

添加 Helm repo 源。

```
$ helm repo add kong https://charts.konghq.com
$ helm repo update
```

部署。

```
$ helm install kong kong/ingress -n kong --create-namespace
```

查看服务地址。

```
$ minikube service kong-gateway-proxy -n kong
$ minikube ip
$ minikube profile list
```

测试代理访问情况。

```
$ PROXY_IP=192.168.49.2:31455
$ curl -i $PROXY_IP
```

测试：重启 kong-controller 部署。

```
$ kubectl rollout restart deployment kong-controller -n kong
```

## TPs

+ [Automate public DNS entries with External DNS for Kubernetes](https://linuxblog.xyz/posts/kubernetes-external-dns/)

+ [📚 Kubernetes（K8S）简介 - K8S 教程 - 易文档](https://k8s.easydoc.net/docs/dRiQjyTY/28366845/6GiNOzyZ/9EX8Cp45)

+ [Kubernetes教程 | Kuboard](https://kuboard.cn/learning/)
