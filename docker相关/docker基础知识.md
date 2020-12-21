# docker基础知识

Docker本身并不是容器，它是创建容器的工具，是应用容器引擎。

Docker技术的三大核心概念，分别是：

- 镜像
- 容器
- 仓库

- 下载安装 Docker 与 Docker Compose
  - www.docker.com
  - https://download.docker.com/linux/static/stable/x86_64/
  - https://docs.docker.com/compose
  - https://docs.docker.com/machine/install-machine
  - docker_hub：https://hub.docker.com/
- Docker-compose 相关命令
  - 运行 docker-compose up
  - docker compose down
  - docker compose down -v
  - docker stop / rm containerID

Demo

- 运行 Docker-compose，本地构建更高效的开发环境，更直观地了解 Elasticsearch 分布式特性
- 集成 Cerebro，方便查看集群状态

## Docker 安装

- 官方文档：https://docs.docker.com/engine/install/centos/

- 环境准备

  - CentOS 7 + 版本

  - 系统内核是 3.10 以上

    ```shell
    [root@A01-R15-I104-75-300H0MK --prod-- systemctl-test]# cat /etc/os-release 
    NAME="CentOS Linux"
    VERSION="7 (Core)"
    ID="centos"
    ID_LIKE="rhel fedora"
    VERSION_ID="7"
    PRETTY_NAME="CentOS Linux 7 (Core)"
    ANSI_COLOR="0;31"
    CPE_NAME="cpe:/o:centos:centos:7"
    HOME_URL="https://www.centos.org/"
    BUG_REPORT_URL="https://bugs.centos.org/"
    
    CENTOS_MANTISBT_PROJECT="CentOS-7"
    CENTOS_MANTISBT_PROJECT_VERSION="7"
    REDHAT_SUPPORT_PRODUCT="centos"
    REDHAT_SUPPORT_PRODUCT_VERSION="7"
    
    [root@A01-R15-I104-75-300H0MK --prod-- systemctl-test]# uname -r
    3.10.0-327.28.3.el7.x86_64
    ```

### Docker在线安装

```shell
# 确保yum源是没问题的
# 将现有yum源配置文件进行备份改名
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
# 配置阿里云yum源
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
# 更新缓存
yum makecache  
或：yum makecache fast
# yum包更新到最新
yum update

# 卸载旧版本
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

# 安装需要的软件包，yum-util 提供yum-config-manager功能，另外两个是devicemapper驱动依赖的
yum install -y yum-utils device-mapper-persistent-data lvm2
# 安装docker,出现输入的界面都按 y
yum install -y docker-ce
或者：yum install docker -y
# 查看docker版本，验证是否安装成功
docker -v
```

### Docker离线安装

**参考资料：**https://www.cnblogs.com/testway/p/13235683.html

1、去官网下载docker 安装二进制包，选择适合自己的版本。这里下载的是docker-20.10.0.tgz，在centos7中安装（cento6无法使用，提示linux版本内核版本太低）

下载地址：https://download.docker.com/linux/static/stable/x86_64/

2、上传docker-20.10.0.tgz到服务器上，进行解压

```shell
[root@A04-R08-I192-75-6WK0S62 tmp]tar -zxvf docker-20.10.0.tgz
[root@A04-R08-I192-75-6WK0S62 tmp]# ll
total 67320
drwxrwxr-x 2 work     work     4096 Dec  9 02:59 docker
-rw-r--r-- 1 root     root 68923289 Dec 15 11:17 docker-20.10.0.tgz
```

3、进入docker目录复制所有文件到/usr/bin目录下，目的/user/bin是环境变量目录，在路径下都可以运行docker命令

```shell
[root@A04-R08-I192-75-6WK0S62 tmp]# ls -l docker
total 224204
-rwxr-xr-x 1 work work 39602024 Dec  9 02:59 containerd
-rwxr-xr-x 1 work work  7270400 Dec  9 02:59 containerd-shim
-rwxr-xr-x 1 work work  9957376 Dec  9 02:59 containerd-shim-runc-v2
-rwxr-xr-x 1 work work 21516360 Dec  9 02:59 ctr
-rwxr-xr-x 1 work work 55151379 Dec  9 02:59 docker
-rwxr-xr-x 1 work work 78806856 Dec  9 02:59 dockerd
-rwxr-xr-x 1 work work   708616 Dec  9 02:59 docker-init
-rwxr-xr-x 1 work work  2928566 Dec  9 02:59 docker-proxy
-rwxr-xr-x 1 work work 13631120 Dec  9 02:59 runc
[root@A04-R08-I192-75-6WK0S62 tmp]# cp docker/* /usr/bin
```

4、systectl 启动 docker

```shell
# 编写 systemd 脚本
[root@A04-R08-I192-75-6WK0S62 tmp]# vim /etc/systemd/system/docker.service
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target

[Service]
Type=notify
ExecStart=/usr/bin/dockerd
ExecReload=/bin/kill -s HUP $MAINPID
LimitNOFILE=infinity
LimitNPROC=infinity
TimeoutStartSec=0
Delegate=yes
KillMode=process
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s

[Install]
WantedBy=multi-user.target

# 赋执行权限
chmod +x /etc/systemd/system/docker.service
systemctl daemon-reload 
systemctl enable docker.service
systemctl start docker

# 开机启动
systemctl enable docker.service

# 启动docker
systemctl start docker

# 检测是否安装成功
[root@A04-R08-I192-75-6WK0S62 tmp]# docker -v
Docker version 20.10.0, build 7287ab3
```

### B 站安装教程（在线安装）

```shell
# 官方安装教程：https://docs.docker.com/engine/install/centos/

```

## Docker相关概念

- 镜像（Image）：docker镜像就好比是一个模板，可以通过这个模板来创建容器服务，tomcat镜像 ===> run ===> tomcat01 容器（提供服务器），通过这个镜像可以创建多个容器（最终服务运行或者项目运行就是在容器中的）。

- 容器（Container）：镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的类和对象一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。
- 仓库（Repository）：仓库可看成一个代码控制中心，用来保存镜像。仓库就是存放镜像的地方！仓库分为公有仓库和私有仓库！Docker Hub（默认是国外的），阿里云...都有容器服务器（配置镜像加速！）

## 配置Docker镜像加速器

默认情况下，将从docker hub (https://hub.docker.com) 上下载docker镜像，太慢。一般都会配置镜像加速器。

- USTC：中科大镜像加速器（https://docker.mirrors.ustc.edu.cn）

```shell
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker

# 验证
[root@A01-R06-I29-98-7C8BT92 --prod-- etc]# cat /etc/docker/daemon.json
{
  "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
}
```

- 阿里云：需要阿里云账户才可以拿到

```shell
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://m741cepa.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker

# 验证
[root@A01-R06-I29-98-7C8BT92 --prod-- etc]# cat /etc/docker/daemon.json
{
  "registry-mirrors": ["https://m741cepa.mirror.aliyuncs.com"]
}
```

- 网易云
- 腾讯云

## Docker 命令

### 帮助命令

```shell
docker version  # 显示 docker 的版本信息
docker info  # 显示docker的系统信息，包括镜像和容器的数量
docker 命令 --help  # 帮助命令
```

帮助文档的地址：https://docs.docker.com/engine/reference/commandline/

### Docker服务相关命令

- 启动docker服务
- 停止docker服务
- 重启docker服务
- 查看docker服务状态
- 开机启动docker服务

```shell
# 启动docker服务
systemctl start docker
# 查看docker服务状态
systemctl status docker
# 停止docker服务
systemctl stop docker
# 设置开机自启动docker服务
systemctl enable docker
```

### Docker镜像相关命令

- 查看镜像
- 搜索镜像
- 拉取镜像
- 删除镜像

```shell
# 查看镜像
docker images
docker images -a   # --all 列出所有镜像
docker images -q   # --quiet 只显示镜像的id

# 搜索镜像
docker search --help
docker search mysql  # 搜索 mysql镜像
docker search mysql --filter=STARS=3000  # 过滤收藏数大于3000的mysql镜像
docker search mysql --filter=STARS=5000  # 过滤收藏数大于5000的mysql镜像
  
# 拉取镜像
docker pull mysql  # 默认拉取最新版本
docker pull mysql:5.7 # 拉取指定版本 mysql 镜像
[root@A04-R08-I132-131-8WC4F22 ~]# docker images
REPOSITORY                                      TAG                 IMAGE ID            CREATED             SIZE
docker.io/mysql                                 5.7                 697daaecf703        4 days ago          448 MB

# 删除镜像
docker rmi dd156dd42341
# 删除指定本地镜像
docker rmi 镜像id
docker rmi -f 镜像id
# 删除多个本地镜像
docker rmi 镜像id 镜像id 镜像id 镜像id
docker rmi -f 镜像id 镜像id 镜像id 镜像id
# 删除所有本地镜像
docker rmi `docker images -aq` 
docker rmi -f `docker images -aq`
```

### Docker容器相关命令

- 查看容器
- 创建容器
- 进入容器
- 启动容器
- 停止容器
- 删除容器
- 查看容器信息

```shell
# 查看容器
docker ps  # 查看正在运行的容器
docker ps -a  # 查看所有的容器
# 创建容器
docker run -it --name=cl elasticsearch:7.4.0 /bin/bash  # 默认就是/bin/bash
# 后台创建容器
docker run -id --name=c2 elasticsearch:7.4.0 /bin/bash
# -i：保持容器运行。通常与-t同时使用。加入it这两个参数后，容器创建后自动进入容器中，退出容器后，容器自动关闭
# -t：为容器重新分配一个伪输入终端，通常与-i同时使用
# -d：以守护（后台）模式运行容器。创建一个容器在后台运行，需要使用docker exec进入容器。退出后，容器不会关闭
# -it：创建的容器一般称为交互式容器，-id创建的容器一般称为守护式容器
# --name：为创建的容器命名

[root@A01-R06-I29-98-7C8BT92 --prod-- export]# docker run -it --name=cl elasticsearch:7.4.0 /bin/bash
[root@88e077bf97f3 elasticsearch]# ll
total 552
-rw-r--r--  1 elasticsearch root  13675 Sep 27  2019 LICENSE.txt
-rw-r--r--  1 elasticsearch root 523209 Sep 27  2019 NOTICE.txt
-rw-r--r--  1 elasticsearch root   8500 Sep 27  2019 README.textile
drwxr-xr-x  2 elasticsearch root   4096 Sep 27  2019 bin
drwxrwxr-x  2 elasticsearch root    148 Sep 27  2019 config
drwxrwxr-x  2 elasticsearch root      6 Sep 27  2019 data
drwxr-xr-x 10 elasticsearch root    119 Sep 27  2019 jdk
drwxr-xr-x  3 elasticsearch root   4096 Sep 27  2019 lib
drwxrwxr-x  2 elasticsearch root      6 Sep 27  2019 logs
drwxr-xr-x 37 elasticsearch root   4096 Sep 27  2019 modules
drwxr-xr-x  2 elasticsearch root      6 Sep 27  2019 plugins

# 进入容器
docker exec -it c2 /bin/bash
# 退出容器
exit

# 启动容器
docker start c2

# 停止容器
docker stop c2

# 删除容器
docker rm c2
docker rm `docker ps -aq`  # 删除所有容器

# 查看容器信息
docker inspect c2
```

### Docker 容器的数据卷

​	需要时看视频！

## Docker-compose

**服务编排**

微服务架构的应用系统中一般包含若干个微服务，每个微服务一般都会部署多个实例，如果每个微服务都要手动启停，维护的工作量会很大。

- 要从Dockerfile build image 或者去 dockerhub 拉取 image
- 要创建多个 container
- 要管理这些 container（启动停止删除）

服务编排：按照一定的业务规则批量管理容器

**Docker-Compose**

Docker-Compose是一个编排多容器分布式部署的工具，提供命令集管理容器化应用的完整开发周期，包括服务构建、启动和停止。使用步骤：

1、利用 Dockerfile 定义运行环境镜像

2、使用 docker - compose.yml定义组成应用的个服务

3、运行 docker - compose up 启动应用

一、安装Docker Compose

```shell
# Compose目前已经完全支持Linux、Mac OS和Windows，在我们安装Compose之前，需要先安装Docker。下面我们以编译好的二进制包方式安装在Linux系统中。
curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 设置文件可执行权限
chmod +x /usr/local/bin/docker-compose

# 查看版本信息
docker-compose -version

# 卸载Docker Compose
rm /usr/local/bin/docker-compose
# 二进制包方式安装的，删除二进制文件即可
```













