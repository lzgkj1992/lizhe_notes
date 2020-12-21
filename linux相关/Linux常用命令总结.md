# Linux常用命令总结

pidstat -d 1   # 查看磁盘io使用情况，1秒钟刷新一次

reboot命令    重启集群

uptime命令

last命令

dmesg命令

vim /var/log/messages

ps -ef | grep agent

ps -ef | grep ifr

du -sh filename   查看文件大小

du -sh * | sort -hr   查看磁盘空间，并从高到底进行排序

find /export/Data/kafka-logs* -name "Audi*" |xargs -i du -sh {} |sort -hr

ulimit -a







新建elasticsearch用户

```shell
[root@A01-R06-I29-98-7C8BT92 --prod-- ~]# useradd elasticsearch  // 创建用户名
Group 'mail' not found. Creating the user mailbox file with 0600 mode.
[root@A01-R06-I29-98-7C8BT92 --prod-- ~]# passwd elasticsearch  // 设置密码
Changing password for user elasticsearch.
New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: all authentication tokens updated successfully.
# 给

[root@A01-R06-I29-98-7C8BT92 --prod-- ~]# su - elasticsearch
[elasticsearch@A01-R06-I29-98-7C8BT92 --prod-- ~]$ 

```

## bc 计算器命令

```shell
[root@A01-R06-I13-73 users][DBA]# bc
bc 1.06.95
Copyright 1991-1994, 1997, 1998, 2000, 2004, 2006 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty'. 
5000 + 9000
14000
1000 * 5
5000
^C
(interrupt) Exiting bc.
[root@A01-R06-I13-73 users][DBA]# 
```

## dig 域名解析

```shell
[root@A01-R06-I13-73 users][DBA]# dig http://hb-es-public.jdcloud.com

; <<>> DiG 9.9.4-RedHat-9.9.4-51.el7_4.2 <<>> http://hb-es-public.jdcloud.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 61114
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;http://hb-es-public.jdcloud.com. IN	A

;; Query time: 4001 msec
;; SERVER: 172.16.16.16#53(172.16.16.16)
;; WHEN: Tue Sep 22 17:03:00 CST 2020
;; MSG SIZE  rcvd: 49
```

## base64编码

```shell
[root@A01-R06-I13-73 users][DBA]# echo -n "jcloud_zBwciPs" | base64
amNsb3VkX3pCd2NpUHM=
```

## yum

- Centos yum源

http://mirror.centos.org/centos/7/

- 国内镜像

https://opsx.alibaba.com/mirror

将原生yum源替换为阿里云yum源

```yaml
# 默认yum源配置文件链接的是国外的网站，下载非常缓慢，更改为阿里云的yum源配置文件
# 将现有yum源配置文件进行备份改名
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
# 配置阿里云yum源
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
# 更新缓存
yum makecache
# yum包更新到最新
yum update
```



## nohup



## date

显示当前系统时间

[root@A04-R08-I132-131-8WC4F22 ~]# date
Sat Aug  1 15:12:19 CST 2020

## which



## whereis



## 防火墙

 一、防火墙的开启、关闭、禁用命令

（1）设置开机启用防火墙：systemctl enable firewalld.service

（2）设置开机禁用防火墙：systemctl disable firewalld.service

（3）启动防火墙：systemctl start firewalld

（4）关闭防火墙：systemctl stop firewalld

（5）检查防火墙状态：systemctl status firewalld 

二、使用firewall-cmd配置端口

（1）查看防火墙状态：firewall-cmd --state

（2）重新加载配置：firewall-cmd --reload

（3）查看开放的端口：firewall-cmd --list-ports

（4）开启防火墙端口：firewall-cmd --zone=public --add-port=9200/tcp --permanent

　　命令含义：

　　–zone #作用域

　　–add-port=9200/tcp #添加端口，格式为：端口/通讯协议

　　–permanent #永久生效，没有此参数重启后失效

　　**注意：添加端口后，必须用命令firewall-cmd --reload重新加载一遍才会生效**

（5）关闭防火墙端口：firewall-cmd --zone=public --remove-port=9200/tcp --permanent









uname -a  # 查看系统位数

```shell
[root@A04-R08-I132-131-8WC4F22 ~]# uname -a
Linux A04-R08-I132-131-8WC4F22.JCLOUD.COM 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
# 可知操作系统是64位的
```



## chmod命令

chmod 777 filename  # 赋予对文件操作的全部权限

```shell
[root@A04-R08-I132-131-8WC4F22 lizhe]# ll 1.sh
-rw-r--r-- 1 root root 0 Aug  1 11:46 1.sh
[root@A04-R08-I132-131-8WC4F22 lizhe]# chmod u+x 1.sh   # 加可执行权限
[root@A04-R08-I132-131-8WC4F22 lizhe]# ll 1.sh
-rwxr--r-- 1 root root 0 Aug  1 11:46 1.sh
[root@A04-R08-I132-131-8WC4F22 lizhe]# chmod a+x 1.sh   # 在3个位置加可执行权限
[root@A04-R08-I132-131-8WC4F22 lizhe]# ll 1.sh
-rwxr-xr-x 1 root root 0 Aug  1 11:46 1.sh
```

## basename命令

```shell
[root@A04-R08-I132-131-8WC4F22 tmp]# basename 12.sh
12.sh
[root@A04-R08-I132-131-8WC4F22 tmp]# basename 12.sh .sh
12
```

## vim命令

- 多模式产生的原因
- 四种模式
  - 正常模式（Normal-mode）
  - 插入模式（Insert-mode）
  - 命令模式（Command-mode）
  - 可视模式（Visual-mode）

- 普通模式

  yy 复制一行  p 粘贴

  3yy 复制向下三行 

  y$ 复制一行中的从光标位置开始直到结尾的所有字符

  dd 剪切一行        p 粘贴

  5dd 剪切向下五行       p 粘贴

  d$ 剪切从光标位置开始到结尾的所有字符

  u 撤销     ctrl+r 之前撤销的操作重新执行

  x 删除单个字符

  r 替换单个字符

  :set nu 显示行号                             

  :set nonu 不显示行号

  :set hlsearch 设置高亮显示

  :set nohlsearch 取消高亮显示

  **注意：**:set 命令做出的修改都只是暂时的，若想永久生效，需改配置文件vim /etc/vimrc

  **要求：**每次打开vim时，都会显示行号

  vim /etc/vimrc

  ```yaml
  # 在文件最后一行添加
  set nu
  ```

  11 shift+g 移动到第11行

  g 移动到第一行

  G或shift+g移动到最后一行

  ^ 即shift+6 ，移动到一行的开头

  $ 即shift+4，移动到一行的结尾

- 命令模式

  :w 保存

  :q 退出

  :wq 保存并退出

  :q! 不保存强制退出

  :! 临时执行其它命令，回车后回到vim正常模式

  /  查找命令   /x  回车后，查找x字符，n 向下查找，N或者shift+n 向上查找

  :%s/x/X/g  将全文中的x替换成X（全部）

  :s/x/X 将光标所在行的x替换成X（单个）

  :s/x/X/g将光标所在行的x替换成X（全部）

- 可视模式

  v  字符可视

  shift+v 行可视   选中多行。

  ctrl+v   块可视   选中块，shift+i 可进行批量操作，然后两次esc，使批量操作生效。

## 用户和用户组管理及密码管理

- useradd 新建用户   （只有root用户才有新建用户的权限）

- userdel 删除用户
- passwd 修改用户密码
- usermod 修改用户属性
- chage 修改用户属性

```shell
[root@A01-R06-I170-129-5001725 ~][DBA]# useradd work      # 新建work用户
[root@A01-R06-I170-129-5001725 ~][DBA]# id work
uid=1000(work) gid=1000(work) groups=1000(work)
[root@A01-R06-I170-129-5001725 ~][DBA]# id abc            # 没有abc用户
id: abc: no such user
[root@A01-R06-I170-129-5001725 ~][DBA]# ls /home/work     # work用户的家目录
# 创建的用户都会加入到/etc/passwd文件中
vim /etc/passwd
work:x:1000:1000::/export/work/:/bin/bash    #说明有work这个用户
# 在/etc/shadow文件中也会有work用户的信息，是与用户密码相关的文件
vim /etc/shadow
tail -10 /etc/shadow
# 当新创建一个用户时，每个用户会有一个uid，用来标识唯一，并且系统会默认会为用户创建一个同名的用户组
[root@A01-R06-I170-129-5001725 ~][DBA]# id work
uid=1000(work) gid=1000(work) groups=1000(work)
[root@A01-R06-I170-129-5001725 ~][DBA]# id root
uid=0(root) gid=0(root) groups=0(root)

#创建好用户之后，需要为用户创建密码
passwd # 更改root用户的密码
passwd work      # 更改work用户的密码
设置用户密码
新的密码：
无效的密码：密码少于8个字符
重新输入新的密码：
passwd：所有的身份验证令牌已经成功更新

# 删除用户
userdel work    # 直接用该命令删除用户，会保留用户的家目录
userdel -r work # 彻底删除用户   /home/、/etc/passwd、/etc/shadow目录下的信息都会被删除

# usermod命令修改用户家目录（尽量不用）
useradd lizhe   # 创建lizhe用户
usermod -d /home/w1 lizhe   # 将用户的家目录进行了修改，改成了w1
# 用户的家目录发生变化，造成的影响就是用户登陆lizhe用户访问的第一个目录是/home/w1

# chage命令用来修改用户的生命周期

```

- groupadd 新建用户组
- groupdel 删除用户组    

```yaml
# 创建组group1
groupadd group1
#将用户lizhe加入group1
usermod -g group1 lizhe
#查看
id lizhe
uid=1008(lizhe) gid=1009(group1) groups=1009(group1)
# 在新建用户的同时指定组 创建用户lizhe，并将其加入group1组
useradd -g group1 lizhe 
# 切换用户 
# 从root用户切换到lizhe用户，-的含义是同时把运行环境从root切换到lizhe，完全的切换
su - lizhe
# 不完全的切换
su lizhe  
# 删除用户组
groupdel group1
```

## su和sudo命令的区别和使用方法

su 切换用户

​	su - username  使用login shell方式切换用户

sudo 以其他用户身份执行命令

​	visudo 设置需要使用sudo的用户

```shell
# root用户
# 30分钟之后关闭系统
shutdown -h 30
shutdown -h now   # 立刻关闭系统
shutdown -c # 取消关闭系统操作
# 将shutdown -c命令的执行权限赋给lizhe用户
visudo  # 打开sudo命令的配置文件
# 想要为lizhe用户赋予sudo命令的全部权限 在打开的文件中添加如下内容
lizhe  ALL=(ALL)  NOPASSWD:ALL
# 这样，lizhe用户环境下，通过使用sudo，就可以具有root用户的权限
# 若想只赋予lizhe用户某些权限，比如说sh

```

## 用户和用户组的配置文件介绍

**vim /etc/passwd**

```shell
root:x:0:0:root:/root:/bin/bash
work:x:1000:1000::/export/work/:/bin/bash
```

第一个字段：用户名

第二个字段：是否需要密码登录

第三个字段：uid     uid不能随意更改，否则就会变成其它用户，例如改成0，就变成了root用户

第四个字段：gid

第五个字段：注释

第六个字段：表示用户的家目录在哪里

第七个字段：用户登录成功后用哪一个命令解释器来解释命令。若将/bin/bash改成/sbin/nologin后，该用户将不可登录终端。

**vim /etc/shadow**

```shell
# 保存用户和用户密码相关的信息
root:$1$bOs46V.h$XTszMTssY8j3ANY2Fqe8/1:18155:0:99999:7:::
work:$1$.XSD6HFn$xt1REi2LVfXCXKRIrh/8l1:17422:0:99999:7:::
```

第一个字段：用户名

第二个字段：加密后的用户密码

**vim /etc/group**

```shell
root:x:0:
work:x:1000:work
```

第一个字段：组名

第二个字段：组是否需要密码验证

第三个字段：组的gid

第四个字段：其它组设置。假如希望用户既属于group1，又属于group2，需要用到第四个字段。例如：

```yaml
# 让lizhe用户属于work这个组,lizhe用户还属于lizhe这个组，这样lizhe用户就属于两个组了
work:x:1000:lizhe
lizhe:x:1001:
```

## 文件与目录权限的表示方法

## 文件权限的修改方法和数字表示方法

## 权限管理以及文件的特殊权限

网络管理

查看网络配置

修改网络配置

## 网络故障排除命令

- ping

ping命令用来检测当前主机与目标主机是否畅通，如果ping不通，说明网络不可达、网络中断或者对方有防火墙的限制。

- traceroute
- mtr

tracerout和mtr命令用来检测当前主机与目标主机间的网络状态，是辅助ping命令使用的。如果ping通，说明当前主机与目标主机之间的网络是畅通的，但是还是出现了访问异常，就说明中间的网络质量出现了问题。可用traceroute命令来追踪路由，追踪服务器每一跳的质量。可用mtr命令检查到目标主机之间是否有数据包的丢失。

- nslookup

访问的时候可能使用域名，那域名对应的ip地址是什么呢？可以使用nslookup查看到。

以上四个命令是用来解决主机问题的，主机问题解决之后，下面来解决端口问题。

- telnet

主机能够连通，但是服务仍然访问不了，就可以使用telnet来检查端口的状态。当端口也通了，仍然发现有问题，就可以更细致的分析数据包，即可以使用tcpdump命令。

- tcpdump

当这些全没有问题后，可能是我们提供的服务的范围不对，比如我们只对127.0.0.1提供了服务，那其它的ip访问过来肯定是访问不到我们的服务，所以我们还提供了netstat和ss这两条命令。

- netstat
- ss

接下来依次来测试一下各命令的使用：

```shell
# 查看网卡信息
ifconfig eth0
# 查看网关信息
route -n
# ping
ping www.baidu.com   # ctrl+c用来停掉ping操作
# traceroute
traceroute -w 1 www.baidu.com  # 最多等待1秒钟
# 示例：
[root@A01-R06-I170-129-5001725 ~][DBA]# traceroute -w 1 192.168.170.162
traceroute to 192.168.170.162 (192.168.170.162), 30 hops max, 60 byte packets
 1  192.168.170.162 (192.168.170.162)  0.193 ms  0.130 ms  0.113 ms

# mtr 会比traceroot显示的内容更加丰富
[root@A01-R06-I13-73 ansible][DBA]# mtr
# 结果显示如下图所示：ctrl+c退出
```

![1568630404074](C:\Users\lizhe427\AppData\Roaming\Typora\typora-user-images\1568630404074.png)

```shell
# nslookup 
# 用来解析域名对应的ip地址是多少
[root@A01-R06-I13-73 ansible][DBA]# nslookup hb-es-public.jdcloud.com
Server:		172.16.16.16
Address:	172.16.16.16#53

Name:	hb-es-public.jdcloud.com
Address: 10.160.254.248

# telnet 
telnet 
bash: telnet: 未找到命令...    # 说明还没有安装对应的软件包，可以使用yum install telnet -y命令安装
# 对某一个ip的某一个端口进行检测  
[root@A01-R06-I170-129-5001725 ~][DBA]# telnet www.baidu.com 80
Trying 220.181.38.150...
Connected to www.baidu.com.
Escape character is '^]'.
^]                              # 退出方式，ctrl+] 进入telnet命令行，然后输入quit，退出！
telnet> quit
Connection closed.

# tcpdump
[root@A01-R06-I170-129-5001725 ~][DBA]# tcpdump -i any -n port 80
[root@A01-R06-I170-129-5001725 ~][DBA]# tcpdump -i any -n host 192.168.178.162
[root@A01-R06-I170-129-5001725 ~][DBA]# tcpdump -i any -n host 192.168.178.162 and port 9500
[root@A01-R06-I170-129-5001725 ~][DBA]# tcpdump -i any -n host 192.168.178.162 and port 9500 -w /tmp/tmp.log   #将捕获的信息保存在/tmp/tmp.log文件中

# netstat
[root@A01-R06-I170-129-5001725 ~][DBA]# netstat -ntpl | grep 9500
tcp6     0      0 192.168.170.129:9500    :::*      LISTEN      136662/java      

# ss
[root@A01-R06-I170-129-5001725 ~][DBA]# ss -ntpl | grep 9200
LISTEN     0     32768     :::9200      :::*     users:(("java",pid=114729,fd=528))
```

## 网络管理和配置文件

## 软件包管理器的使用

- 软件包管理器
- rpm包和rpm命令
- yum仓库
- 源代码编译安装
- 内核升级
- grub配置文件

## 使用rpm命令安装软件包

## 使用yum包管理器安装软件包

## 通过源代码编译安装软件包

- 二进制安装
- 源代码编译安装
  1. wget https://openresty.org/download/openresty-1.15.8.1.tar.gz
  2. tar -zxf openresty-VERSION.tar.gz
  3. cd openresty-VERSION.tar.gz
  4. ./configure --prefix=/usr/local/openresty
  5. make -j2
  6. make install

尽量是yum install的方式来安装软件包，但是yum install的方式安装的软件包版本往往不是最新的，如果对软件包的版本有要求，而yum install安装满足不了，这个时候就需要使用源代码编译的方式进行安装。

## 如何进行内核升级

- rpm格式内核

  - 查看内核版本   uname -r
  - 升级内核版本   yum install kernel-3.10.0
  - 升级已安装的其他软件包和补丁   yum update

- 安装依赖包

  yum install gcc gcc-c++ make ncurses-devel openssl-devel elfutils-libelf-devel

- 下载并解压缩内核

  - https://www.kernel.org
  - tar xvf linux-5.1.10.tar.xz -C /usr/src/kernels

grub配置文件介绍

## 使用ps和top命令查看进程

ps -eLf | more   分页查看进程



- 进程的概念与进程查看
- 进程的控制命令
- 进程的通信方式——信号
- 守护进程和系统日志
- 服务管理工具systemctl
- SELinux简介







进程的控制和进程之间的关系

进程的通信方式和信号：kill

守护进程

screen命令和系统日志

服务管理工具systemctl

SELinux简介

内存与磁盘管理

内存查看命令

磁盘分区和文件大小查看

文件系统管理

i节点与数据块操作

分区和挂载

分区和挂载磁盘配额

交换分区swap的查看与创建

软件RAID的使用

逻辑卷LVM的用途与创建

系统综合状态查看命令sar以及第三方命令

## 环境变量配置文件

- /etc/profile   全局配置环境变量的文件  
- ~/.bash_profile  用户专用   su - elasticsearch  
- ~/.bashrc  用户专用  su elasticsearch   su - elasticsearch这两种切换用户的方式均可生效
- /etc/bashrc   全局配置环境变量的文件   使用su elasticsearch时会被执行，即不加

注意：~ 表示的是家目录，即用户专有的配置文件，/etc/profile和/etc/bashrc是全局配置文件，所有用户都生效

profile和bashrc的区别是：当切换用户时，是使用的login shell还是nologin shell，比如，su - work是login shell，而 su work是nologin shell，如果使用login shell的方式，那么这四种配置文件均能检测到，如果使用nologin shell的方式，那么只能检测到bashrc配置文件，所以在切换用户的时候，养成带 - 的方式，还是很好的。

优先级： /etc/bashrc > ~/.bashrc  >  ~/.bash_profile > /etc/profile

使用 su root 命令登陆用户，只会加载两个配置文件，加载不完全；所以建议使用su - root命令登陆，这样可以将四个配置文件全部加载上。

```shell
# 配置环境变量
vim /etc/profile
环境变量配置文件：
注意：凡是保存在etc下的，是所有用户通用的文件。
/etc/profile
~/.bash_profile
~/.bashrc
/etc/bashrc

一般都将环境变量配置在/etc/profile文件中，对所有用户都生效。
```

修改完这四个文件后，并不会立即生效，需要  source 文件名 一下才会生效，或者关闭终端重新打开。

**查看某个环境变量**

```shell
[root@A01-R06-I29-53-27SKT92 elasticsearch]# echo $JAVA_HOME
/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.111-1.b15.el7_2.x86_64/jre
```





## 案例

### 创建一个elasticsearch用户

```shell
[root@A01-R06-I29-98-7C8BT92 --prod-- ~]# useradd elasticsearch  // 创建用户名
Group 'mail' not found. Creating the user mailbox file with 0600 mode.
[root@A01-R06-I29-98-7C8BT92 --prod-- ~]# passwd elasticsearch  // 设置密码
Changing password for user elasticsearch.
New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: all authentication tokens updated successfully.

# 为elasticsearch用户添加sudo权限
visudo  # 打开sudo命令的配置文件
# 想要为lizhe用户赋予sudo命令的全部权限 在打开的文件中添加如下内容
elasticsearch   ALL=(ALL)  NOPASSWD:ALL
# 切换到elasticsearch用户
[root@A01-R06-I29-98-7C8BT92 --prod-- ~]# su - elasticsearch
[elasticsearch@A01-R06-I29-98-7C8BT92 --prod-- ~]$ 
```
