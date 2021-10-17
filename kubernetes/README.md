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
```
