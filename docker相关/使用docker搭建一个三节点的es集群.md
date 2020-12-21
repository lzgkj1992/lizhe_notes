# 使用docker搭建一个三节点es集群

## 基于阿里云安装docker

### 申请云主机

待补充！

### 安装docker

```shell
# 确保yum源是没问题的
# 将现有yum源配置文件进行备份改名
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
# 配置阿里云yum源
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
# 更新缓存
yum makecache
# yum包更新到最新
yum update

# 安装需要的软件包，yum-util 提供yum-config-manager功能，另外两个是devicemapper驱动依赖的
yum install -y yum-utils device-mapper-persistent-data lvm2
# 配置阿里云docker镜像源
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
# 安装docker,出现输入的界面都按 y
yum install -y docker-ce
# 查看docker版本，验证是否安装成功
docker -v
# 查看docker安装的位置
yum list installed | grep docker

# 启动docker服务
systemctl start docker
# 查看docker服务状态
systemctl status docker
# 停止docker服务
systemctl stop docker
# 设置开机自启动docker服务
systemctl enable docker
```

### 配置Docker镜像加速器

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

### 安装dockerUI

docker图像页面管理工具常用的有三种：

​	DockerUI

​	Portainer

​	Shipyard

DockerUI 是  Portainer的前身，这三个工具通过docker api来获取管理的资源信息。平时我们常常对着shell对着这些命令行客户端，审美会很疲劳，如果有漂亮的图形化界面可以直观查看docker资源信息，也是非常方便的。

**DockerUI Portainer**

#### 1、查看dockerui Portainer镜像

```shell
docker search Portainer
```

#### 2、选择喜欢的dockerui风格镜像，下载

```shell
docker pull docker.io/portainer/portainer

# 查看镜像
docker images
[root@zookeeper-env yum.repos.d]# docker images
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
portainer/portainer   latest              62771b0b9b09        3 weeks ago         79.1MB
```

#### 3、启动UI

```shell
docker run -d -p 9000:9000 --restart=always -v /var/run/docker.sock:/var/run/docker.sock --name portainer-arry portainer/portainer

# 运行结果
[root@zookeeper-env yum.repos.d]# docker run -d -p 9000:9000 --restart=always -v /var/run/docker.sock:/var/run/docker.sock --name portainer-arry portainer/portainer
714aaf1d3a6b220d44b98db09455303bd3470928564a95228d5f86c958bca4bc
```

#### 4、查看容器

```shell
# 查看docker运行信息
docker ps -a

[root@zookeeper-env yum.repos.d]# docker ps -a
CONTAINER ID        IMAGE                 COMMAND             CREATED              STATUS              PORTS                    NAMES
714aaf1d3a6b        portainer/portainer   "/portainer"        About a minute ago   Up About a minute   0.0.0.0:9000->9000/tcp   portainer-arry

# 查看docker启动日志信息
docker logs -f portainer-arry

[root@zookeeper-env yum.repos.d]# docker logs -f portainer-arry
2020/08/13 10:32:46 Warning: the --template-file flag is deprecated and will likely be removed in a future version of Portainer.
2020/08/13 10:32:49 server: Reverse tunnelling enabled
2020/08/13 10:32:49 server: Fingerprint c6:f2:60:0b:6c:f0:42:66:b4:49:ba:d7:41:6b:ab:ce
2020/08/13 10:32:49 server: Listening on 0.0.0.0:8000...
2020/08/13 10:32:49 Starting Portainer 1.24.1 on :9000
2020/08/13 10:32:49 [DEBUG] [chisel, monitoring] [check_interval_seconds: 10.000000] [message: starting tunnel management process]
```

#### 5、浏览器访问

http://114.67.250.137:9000/

初始化用户和密码：

Username: admin

Password: admin123

Confirm password: admin123

### Docker ES 安装 集群的搭建

**目标**

使用docker安装es并且完成集群的配置工作

**步骤**

#### 1、安装es的镜像

```shell
docker pull elasticsearch:6.7.1
```

#### 2、在根目录建立一个文件夹 /ES/config

```shell
# 创建文件夹 ES/config
mkdir -p /ES/config
# 进入config
cd /ES/config
# 分别创建三个文件
vim es1.yml
vim es2.yml
vim es3.yml
```

#### 3、三个文件内容如下：

vim es1.yml

```yaml
# 集群唯一名称，所有节点一致
cluster.name: elasticsearch-cluster
# 节点名称
node.name: es-node1
# 设置可以访问的ip，默认为0.0.0.1，这里全部设置通过
network.host: 0.0.0.0
# 设置对外服务的http端口，默认为9200
http.port: 9200
# 设置节点之间交互的tcp端口，默认是9300
transport.tcp.port: 9300
# 是否支持跨域，是：true
http.cors.enabled: true
# 是否支持所有域名
http.cors.allow-origin: "*"
# 配置节点角色
node.master: true
node.data: true
node.ingest: true
# discovery发现机制
discovery.zen.ping.unicast.hosts: ["114.67.250.137:9300","114.67.250.137:9301","114.67.250.137:9302"]
# 防止脑裂
discovery.zen.minimum_master_nodes: 1

# bootstrap.memory_lock: true

# 配置断路器
indices.recovery.max_bytes_per_sec: 500mb
indices.memory.index_buffer_size: 20%
indices.breaker.fielddata.limit: 10%
indices.breaker.request.limit: 20%
indices.breaker.total.limit: 50%
indices.fielddata.cache.size: 20%

# 多实例部署时，保证主、副本分片不会分在同一台物理机上
cluster.routing.allocation.same_shard.host: true

# 以下为拷贝内容
====================================================================
cluster.name: elasticsearch-cluster
node.name: es-node1
network.host: 0.0.0.0
http.port: 9200
transport.tcp.port: 9300
http.cors.enabled: true
http.cors.allow-origin: "*"
node.master: true
node.data: true
node.ingest: true
discovery.zen.ping.unicast.hosts: ["114.67.250.137:9300","114.67.250.137:9301","114.67.250.137:9302"]
discovery.zen.minimum_master_nodes: 1
# bootstrap.memory_lock: true
indices.recovery.max_bytes_per_sec: 500mb
indices.memory.index_buffer_size: 20%
indices.breaker.fielddata.limit: 10%
indices.breaker.request.limit: 20%
indices.breaker.total.limit: 50%
indices.fielddata.cache.size: 20%
cluster.routing.allocation.same_shard.host: true
```

vim es2.yml

```yaml
# 集群唯一名称，所有节点一致
cluster.name: elasticsearch-cluster
# 节点名称
node.name: es-node2
# 设置可以访问的ip，默认为0.0.0.1，这里全部设置通过
network.host: 0.0.0.0
# 设置对外服务的http端口，默认为9200
http.port: 9201
# 设置节点之间交互的tcp端口，默认是9300
transport.tcp.port: 9301
# 是否支持跨域，是：true
http.cors.enabled: true
# 是否支持所有域名
http.cors.allow-origin: "*"
# 配置节点角色
node.master: true
node.data: true
node.ingest: true
# discovery发现机制
discovery.zen.ping.unicast.hosts: ["114.67.250.137:9300","114.67.250.137:9301","114.67.250.137:9302"]
# 防止脑裂
discovery.zen.minimum_master_nodes: 1

# bootstrap.memory_lock: true

# 配置断路器
indices.recovery.max_bytes_per_sec: 500mb
indices.memory.index_buffer_size: 20%
indices.breaker.fielddata.limit: 10%
indices.breaker.request.limit: 20%
indices.breaker.total.limit: 50%
indices.fielddata.cache.size: 20%

# 多实例部署时，保证主、副本分片不会分在同一台物理机上
cluster.routing.allocation.same_shard.host: true
```

vim es3.yml

```yaml
# 集群唯一名称，所有节点一致
cluster.name: elasticsearch-cluster
# 节点名称
node.name: es-node3
# 设置可以访问的ip，默认为0.0.0.1，这里全部设置通过
network.host: 0.0.0.0
# 设置对外服务的http端口，默认为9200
http.port: 9202
# 设置节点之间交互的tcp端口，默认是9300
transport.tcp.port: 9302
# 是否支持跨域，是：true
http.cors.enabled: true
# 是否支持所有域名
http.cors.allow-origin: "*"
# 配置节点角色
node.master: true
node.data: true
node.ingest: true
# discovery发现机制
discovery.zen.ping.unicast.hosts: ["114.67.250.137:9300","114.67.250.137:9301","114.67.250.137:9302"]
# 防止脑裂
discovery.zen.minimum_master_nodes: 1

# bootstrap.memory_lock: true

# 配置断路器
indices.recovery.max_bytes_per_sec: 500mb
indices.memory.index_buffer_size: 20%
indices.breaker.fielddata.limit: 10%
indices.breaker.request.limit: 20%
indices.breaker.total.limit: 50%
indices.fielddata.cache.size: 20%

# 多实例部署时，保证主、副本分片不会分在同一台物理机上
cluster.routing.allocation.same_shard.host: true
```

#### 4、创建容器

```yaml
# 查看镜像
[root@zookeeper-env config]# docker images
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
portainer/portainer   latest              62771b0b9b09        3 weeks ago         79.1MB
elasticsearch         6.7.1               e2667f5db289        16 months ago       812MB

# 创建容器
docker run -e ES_JAVA_OPTS="-Xms1g -Xmx1g" -d -p 9200:9200 -p 9300:9300 -v /ES/config/es1.yml:/usr/share/elasticsearch/config/elasticsearch.yml --name ES01 e2667f5db289

docker run -e ES_JAVA_OPTS="-Xms1g -Xmx1g" -d -p 9201:9201 -p 9301:9301 -v /ES/config/es2.yml:/usr/share/elasticsearch/config/elasticsearch.yml --name ES02 e2667f5db289

docker run -e ES_JAVA_OPTS="-Xms1g -Xmx1g" -d -p 9202:9202 -p 9302:9302 -v /ES/config/es3.yml:/usr/share/elasticsearch/config/elasticsearch.yml --name ES03 e2667f5db289
```

#### 5、可能出现的错误

错误一：max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]

解决办法：

```shell
vim /etc/sysctl.conf
# 最后一行添加
vm.max_map_count = 262144
vm.swappiness = 0
sysctl -p
```

错误二：ERROR: [1] bootstrap checks failed [1]: memory locking requested for elasticsearch process but memory is not locked

解决办法：

```yaml
# 修改容器里面的文件或者将bootstrap.memory_lock: true配置去掉（如果测试使用）
vim /etc/security/limits.conf
# 添加以下两行
*            soft    memlock         unlimited
*            hard    memlock         unlimited
```

#### 6、访问集群

```shell
[root@zookeeper-env config]# curl localhost:9200/_cluster/health?pretty
{
  "cluster_name" : "elasticsearch-cluster",
  "status" : "green",
  "timed_out" : false,
  "number_of_nodes" : 3,
  "number_of_data_nodes" : 3,
  "active_primary_shards" : 0,
  "active_shards" : 0,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 0,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 100.0
}
```

### 使用docker安装HEAD插件

#### 1、拉取HEAD镜像

```shell
docker pull mobz/elasticsearch-head:5
```

#### 2、创建容器

```shell
docker run -d --name es_admin -p 9100:9100 mobz/elasticsearch-head:5
```

#### 3、浏览器测试

```shell
http://114.67.250.137:9100/
```

#### 4、常见错误

错误一：docker es 406 (Not Acceptable)

解决方法：

```shell
# 进入es_admin容器
docker exec -it es_admin /bin/bash

# 进入head安装目录
# 进入_site/目录，编辑vendor.js文件，修改两处内容：
[root@zookeeper-env config]# docker exec -it es_admin /bin/bash
root@8b38801c8662:/usr/src/app# ls
Dockerfile    README.textile			  elasticsearch-head.sublime-workspace	node_modules		      src
Gruntfile.js  _site				  grunt_fileSets.js			package.json		      test
LICENCE       elasticsearch-head.sublime-project  index.html				plugin-descriptor.properties
root@8b38801c8662:/usr/src/app# cd _site/
root@8b38801c8662:/usr/src/app/_site# ls
app.css  app.js  base  fonts  i18n.js  index.html  lang  vendor.css  vendor.js
root@8b38801c8662:/usr/src/app/_site# vim vendor.js 
bash: vim: command not found
# 如果找不到vim方法，请参考5、docker容器中安装vim
6886行：/contentType: "application/x-www-form-urlencoded" 改成：
contentType: "application/json;charset=UTF-8"

7573行：var inspectData = s.contentType === "application/x-www-form-urlencoded" && 改成：
var inspectData = s.contentType === "application/json;charset=UTF-8" &&
```

修改完后，重启head容器。

#### 5、在docker容器中安装vim

在使用docker容器时，有时候里边没有安装vim，敲vim命令时提示说：vim: command not found，这个时候就需要安装vim，可是当你敲apt-get install vim命令时，提示：

```shell
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package vim
```

这时候需要敲：apt-get update，这个命令的作用是：同步 /etc/apt/sources.list 和 /etc/apt/sources.list.d 中列出的源的索引，这样才能获取到最新的软件包。

等更新完毕以后再敲命令：apt-get install vim命令即可。

**配置国内镜像源**

实际在使用过程中，运行 apt-get update，然后执行 apt-get install -y vim，下载地址由于是海外地址，下载速度异常慢而且可能中断更新流程，所以做下面配置：

```shell
mv /etc/apt/sources.list /etc/apt/sources.list.bak
echo "deb http://mirrors.163.com/debian/ jessie main non-free contrib" >> /etc/apt/sources.list
echo "deb http://mirrors.163.com/debian/ jessie-proposed-updates main non-free contrib" >>/etc/apt/sources.list
echo "deb-src http://mirrors.163.com/debian/ jessie main non-free contrib" >>/etc/apt/sources.list
echo "deb-src http://mirrors.163.com/debian/ jessie-proposed-updates main non-free contrib" >>/etc/apt/sources.list
# 更新安装源
apt-get update
```

