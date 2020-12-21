# 机器 cpu 压测

## 安装docker

### 在线安装

### 离线安装

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

## 准备镜像

**docker-stress源码：**https://github.com/progrium/docker-stress

```shell
# 本地拉取源码
git clone git@github.com:progrium/docker-stress.git

# 将源码上传到测试服务器上，并打包成镜像
[root@A04-R08-I132-131-8WC4F22 docker-stress]# ll
total 20
-rw-r--r-- 1 root root  170 Dec 14 11:04 Dockerfile
-rw-r--r-- 1 root root 1061 Dec 14 11:04 LICENSE
-rw-r--r-- 1 root root   35 Dec 14 11:04 Makefile
-rw-r--r-- 1 root root 1603 Dec 14 11:04 README.md
-rw-r--r-- 1 root root   37 Dec 14 11:04 SPONSORS
[root@A04-R08-I132-131-8WC4F22 docker-stress]# make build
[root@A04-R08-I132-131-8WC4F22 docker-stress]# docker images
REPOSITORY                                      TAG                 IMAGE ID            CREATED             SIZE
stress                                          latest              f19dc9c34d30        7 seconds ago       211 MB
# 修改 REPOSITORY 名称
[root@A04-R08-I132-131-8WC4F22 docker-stress]# docker tag stress progrium/stress
[root@A04-R08-I132-131-8WC4F22 docker-stress]# docker images
REPOSITORY                                      TAG                 IMAGE ID            CREATED              SIZE
progrium/stress                                 latest              f19dc9c34d30        About a minute ago   211 MB
stress                                          latest              f19dc9c34d30        About a minute ago   211 MB

# 导出镜像
[root@A04-R08-I132-131-8WC4F22 tmp]# docker save progrium/stress -o /tmp/stress.tar
[root@A04-R08-I132-131-8WC4F22 tmp]# ll /tmp/stress.tar 
-rw------- 1 root root 221345280 Dec 15 11:36 /tmp/stress.tar

# 将导出的镜像文件上传到目标服务器并load镜像
[root@A04-R08-I192-75-6WK0S62 tmp]# docker load -i stress.tar
[root@A04-R08-I192-75-6WK0S62 tmp]# docker images
REPOSITORY        TAG       IMAGE ID       CREATED        SIZE
progrium/stress   latest    62ac75034168   20 hours ago   211MB
```

## 脚本压测

vim cpu_stress.sh

```shell
#!/bin/bash

function rand() {
  min=$1
  max=$(($2 - $min + 1))
  num=$(date +%s%N)
  echo $(($num % $max + $min))
}

CPU=$(rand 8 13)
TIME=$(( $(rand 8 48) * 60 ))

docker stop stress
docker rm stress

#docker pull 172.19.23.180:5000/progrium/stress
#docker tag 172.19.23.180:5000/progrium/stress progrium/stress

docker run \
  -d \
  --name stress \
  progrium/stress \
  --cpu ${CPU} \
  --io 1 \
  --vm 1 \
  --vm-bytes 512M \
  --timeout ${TIME}s
```

执行脚本：

```shell
chmod +x cpu_stress.sh
# 调试运行脚本
[root@A04-R08-I192-75-6WK0S62 tmp]# bash -x cpu_stress.sh
# 运行脚本
[root@A04-R08-I192-75-6WK0S62 tmp]# ./cpu_stress.sh
[root@A04-R08-I192-75-6WK0S62 tmp]# docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS          PORTS     NAMES
e8882c4bf13d   progrium/stress   "/usr/bin/stress --v…"   45 seconds ago   Up 40 seconds             stress
```

## 查看机器cpu使用情况

发现cpu使用率明显上升，可以通过修改压测的cpu核数来调整cpu使用率。

## 配置crontab定时执行

```shell
[root@A04-R08-I192-75-6WK0S62 tmp]# crontab -e
[root@A04-R08-I192-75-6WK0S62 tmp]# crontab -l
30 */5 * * * /tmp/cpu_stress.sh >>/tmp/cpu_stress.log
```





