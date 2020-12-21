# 极客时间Linux实战技能笔记100讲笔记

**配套视频：**《极客时间-Linux实战技能100讲》

## 第一章 基础篇

### 01 课程介绍

​	略！

### 02 内容综述

- Linux 背景介绍
- 系统操作
- 服务管理
- Shell 脚本
- 文本操作
- 常用服务搭建

### 03 什么是Linux

- Linux 有两种含义：
  - 一种是 Linus 编写的开源操作系统的内核
  - 另一种是广义的操作系统

- Linux 的第一印象
  - 服务端操作系统和客户端操作系统要做的事情不一样
  - 命令行操作方式与图形界面的差异
- 学习 Linux 之前的环境准备
  - 云主机
  - 无数据的 PC（不推荐多系统混跑）
  - 虚拟机（推荐方式）

### 04 Linux的内核版本及常见发行版

- Linux 版本
  - 内核版本
  - 发行版本
- 内核版本
  - https://www.kernel.org/
  - 内核版本分为三个部分
  - 主版本号、次版本号、末版本号
  - 次版本号是奇数为开发版，偶数为稳定版
- 发行版本
  - Red Hat
  - CentOS（推荐使用）
  - Ubuntu

### 05 安装VirtualBox虚拟机

略！

### 06 在虚拟机中安装Linux系统

略！

### 07 第一次启动Linux

- 终端
  - 图形终端
  - 命令行终端
  - 远程终端（SSH、VNC）
- 常见目录介绍
  - / 根目录
  - /root  root 用户的家目录
  - /home/username 普通用户的家目录
  - /etc 配置文件目录
  - /bin 命令目录
  - /sbin 管理命令目录
  - /usr/bin  /usr/sbin 

## 第二章 系统操作篇（18讲）

### 08 万能的帮助命令：man、help、info

- 万能的帮助命令

  - 为什么要学习帮助命令
  - man 帮助
  - help 帮助
  - info 帮助
  - 使用网络资源（搜索引擎和官方文档）

- man 帮助

  - man 是 manual 的缩写
  - man 帮助用法演示
    - man ls

  - man 也是一条命令，分为 9 章，可以使用 man 命令获得 man 的帮助
    - man 7 man

- help 帮助
  - shell（命令解释器）自带的命令称为内部命令，其他的是外部命令
  - 内部命令使用 help 帮助
    - help cd
  - 外部命令使用 help 帮助
    - ls --help
- info 帮助
  - info 帮助比 help 更详细，作为 help 的补充
    - info ls
- 为什么要学习帮助命令
  - Linux 的基本操作方式是命令行
  - 海量的命令不适合“死记硬背”
  - 你要升级你的大脑

### 09 初识pwd和ls命令

- 一切皆文件
  - 文件查看
  - 目录文件的创建与删除
  - 通配符
  - 文件操作
  - 文件内容查看
- pwd 显示当前的目录名称
- cd 更改当前的操作目录
- ls 查看当前目录下的文件
  - ls [选项，选项...] 参数...
  - 常用参数
    - -l 长格式
    - -a 显示隐藏文件
    - -r 逆序显示
    - -t 按照时间顺序显示
    - -R 递归显示
    - -h 可易读方式显示文件大小

### 10 详解ls命令

```shell
[root@A04-R08-I132-131-8WC4F22 ~]# ls -l
[root@A04-R08-I132-131-8WC4F22 ~]# ls -a
[root@A04-R08-I132-131-8WC4F22 ~]# ls -al
[root@A04-R08-I132-131-8WC4F22 ~]# ls -r  # 逆序显示
[root@A04-R08-I132-131-8WC4F22 ~]# ls -t  # 按照时间顺序显示
[root@A04-R08-I132-131-8WC4F22 ~]# ls -l -r -t
[root@A04-R08-I132-131-8WC4F22 ~]# ls -lrt
[root@A04-R08-I132-131-8WC4F22 ~]# ls -R  # 递归显示
[root@A04-R08-I132-131-8WC4F22 ~]# ls -lrtR
[root@A04-R08-I132-131-8WC4F22 ~]# ls /root /
```

### 11 详解cd命令

**更改当前的操作目录**

- cd  更改当前的操作目录
  - cd /path/to/...   绝对路径
  - cd ./path/to/...  相对路径
  - cd ../path/to/...  相对路径

```shell
cd .. # 返回上层目录
cd -  # 显示工作目录
cd ~  # 切换到工作目录
```

### 12 创建和删除目录

- mkdir 创建目录
  - 常用参数
    - -p 建立多级目录
- 删除空目录
  - rmdir 删除空目录
  - rm -r 删除非空目录

### 13 复制和移动目录

**复制文件**

- cp 复制文件和目录
  - cp [选项]  文件路径
  - cp [选项]  文件...  路径
- 常用参数
  - -r  复制目录
  - -p 保留用户、权限、时间等文件属性
  - -a 等同于 -dpR

**移动文件**

- mv  移动文件
  - mv [选项]  源文件 目标文件
  - mv [选项]  源文件 目录

**删除文件**

- rm 删除文件
  - 常用参数
    - -r 删除目录（包括目录下的所有文件）
    - -f 删除文件不进行提示
  - 注意：rm 命令可以删除多个目录，需谨慎使用

**通配符**

- 定义：shell 内建的符号
- 用途：操作多个相似（有简单规律）的文件
- 常用通配符
  - `* 匹配任何字符串`
  - `? 匹配1个字符串`
  - `[xyz] 匹配xyz任意一个字符`
  - `[a-z] 匹配一个范围`
  - `[!xyz]或[^xyz] 不匹配`

### 14 如何在Linux下进行文本查看

**文本查看命令**

- cat  文本内容显示到终端

```shell
# 查看文件
cat log4j2.properties
cat log4j2.properties | more  # 按回车键，往下翻一行，ctrl + f 往下翻一页
cat log4j2.properties | less  # 按回车键，往下翻一行，ctrl + f 往下翻一页
```

- head  查看文件开头

```shell
head log4j2.properties  # 默认显示前10行
head -n50 log4j2.properties  # 显示前50行
```

- tail  查看文件结尾
  - 常用参数 -f 文件内容更新后，显示信息同步更新

```shell
tail log4j2.properties  # 默认显示最后10行
tail -f log4j2.properties  # 显示最后10行，并且信息同步更新
tail -n50 log4j2.properties  # 显示最后50行
```

- wc  统计文件内容信息

```shell
[root@A04-R08-I132-131-8WC4F22 config]# wc log4j2.properties 
  188   888 13085 log4j2.properties
  
[root@A04-R08-I132-131-8WC4F22 config]# wc --help
Usage: wc [OPTION]... [FILE]...
  or:  wc [OPTION]... --files0-from=F
Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  With no FILE, or when FILE is -,
read standard input.  A word is a non-zero-length sequence of characters
delimited by white space.
The options below may be used to select which counts are printed, always in
the following order: newline, word, character, byte, maximum line length.
  -c, --bytes            print the byte counts
  -m, --chars            print the character counts
  -l, --lines            print the newline counts
      --files0-from=F    read input from the files specified by
                           NUL-terminated names in file F;
                           If F is - then read names from standard input
  -L, --max-line-length  print the length of the longest line
  -w, --words            print the word counts
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
For complete documentation, run: info coreutils 'wc invocation'
```

### 15 打包压缩和解压缩

**Linux 的备份压缩**

- 最早的 linux 备份介质是磁带，使用的命令是 tar
- 可以打包后的磁带文件进行压缩储存，压缩的命令是 gzip 和 bzip2
- 经常使用的扩展名是 .tar.gz  .tar.bz2  .tgz

**打包命令**

- tar 打包命令
- 常用参数
  - c 打包
  - x 解包
  - f 指定操作类型为文件

**压缩和解压缩**

- 可以使用 gzip 和 bzip2 命令单独操作
- 通常和 tar 命令配合操作
- 常用参数
  - -z gzip 格式压缩和解压缩
  - -j bzip2 格式压缩和解压缩

```shell
# 压缩,将当前目录下的文件打包成test.tar.gz
tar -zcvf test.tar.gz ./

# 解压缩
tar -zxvf 压缩包.tar.gz
```

### 16~19 Vim

- 安装vim  `yum install vim-enhanced`

vim命令

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

### 20 用户和用户组管理及密码管理

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

### 21 su和sudo命令的区别和使用方法

su 切换用户

​	su username   # 只切换用户，但不切换shell环境，nologin shell 方式

​	su - username  # （建议使用） 不仅切换用户，而且切换shell环境，使用 login shell 方式切换用户 

sudo 以其他用户身份执行命令

​	visudo 设置需要使用 sudo 的用户，相当于打开 vim /etc/sudoers

```shell
# 切换到root用户
sudo -s
sudo su
su root  # 需要密码
su - root  # 需要密码

# root用户
# 30分钟之后关闭系统
shutdown -h 30
shutdown -h now   # 立刻关闭系统
shutdown -c # 取消关闭系统操作

# 赋予用户sudo命令的权限
# 将shutdown -c命令的执行权限赋给lizhe用户
visudo  # 打开sudo命令的配置文件
# 想要为lizhe用户赋予sudo命令的全部权限 在打开的文件中添加如下内容
## Allow root to run any commands anywhere 
root    ALL=(ALL)       ALL
lizhe  ALL=(ALL)  NOPASSWD:ALL
# 这样，lizhe用户环境下，通过使用sudo，就可以具有root用户的权限
# 若想只赋予lizhe用户某些权限，比如说sh

# 使用sudo常见问题
# Disable "ssh hostname sudo <cmd>", because it will show the password in clear text. 
# Sorry, You have to run "ssh -t hostname sudo <cmd>".
# 解决办法：将 Defaults requiretty 注释掉
# Defaults requiretty

# 问题 su username 和 su - username 的区别？
```

### 22 用户和用户组的配置文件介绍

- /etc/passwd  用户配置文件
- /etc/shadow  用户密码相关配置文件
- /etc/group  用户组配置文件

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

### 23 文件与目录权限的表示方法

- 查看文件权限 ls -l

<img src="https://raw.githubusercontent.com/lzgkj1992/markdown_images/master/image-20201027144646857.png" alt="image-20201027144646857" style="zoom:67%;" />

- 注意：对于权限处的三组权限（9个字母）
  - 第一组（rw-）表示当前用户对该文件所拥有的权限
  - 第二组（---）表示同组用户对该文件所拥有的权限
  - 第三组（---）表示其他用户对该文件所拥有的权限

```shell
[root@A04-R08-I132-131-8WC4F22 elasticsearch6_9700]# ls -l
total 468
drwxr-xr-x  3 work work   4096 Aug 27  2019 bin
drwxr-xr-x  2 work work   4096 Aug 27  2019 config
drwxrwxr-x  3 work work     26 Aug 27  2019 data
drwxr-xr-x  3 work work   4096 May 16  2019 lib
-rw-r--r--  1 work work  13675 May 16  2019 LICENSE.txt
drwxrwxr-x  2 work work   4096 Aug 27  2019 log
drwxr-xr-x  2 work work     37 Aug 27  2019 logs
drwxr-xr-x 31 work work   4096 May 16  2019 modules
-rw-r--r--  1 work work 427502 May 16  2019 NOTICE.txt
drwxr-xr-x  2 work work     10 May 16  2019 plugins
-rw-r--r--  1 work work   8519 May 16  2019 README.textile
```

- 文件类型

  - `-`  普通文件
  - `d`  目录文件
  - `b`  块特殊文件
  - `c`  字符特殊文件
  - `l`  符号链接
  - `f`  命名管道
  - `s`  套接字文件

- 文件权限的表示方法

  - 字符权限表示方法
    - r  读
    - w  写
    - x  执行
  - 数字权限的表示方法
    - r = 4
    - w = 2
    - x = 1

  - `-rw-r-xr-- 1 username groupname mtime filename`
    - rw- 文件属主的权限
    - r-x  文件属组的权限
    - r--   其他用户的权限

- 创建新文件有默认权限，根据 umask 值计算，属主和属组根据当前进程的用户来设定

- 目录权限的表示方法

  - x  进入目录
  - rx 显示目录内的文件名
  - wx 修改目录内的文件名

### 24 文件权限的修改方法和数字表示方法

- 修改权限命令
  - chmod  修改文件、目录权限
    - chmod u+x /tmp/testfile
    - chmod 755 /tmp/testfile
  - chown  更改属主、属组   -R 级联  `chown -R admin:admin elasticearch-9200`
  - chgrp  可以单独更改属组，不常用

```shell
# chmod 更改文件、目录权限
# 字符权限
[root@A04-R08-I132-131-8WC4F22 test]# touch afile
[root@A04-R08-I132-131-8WC4F22 test]# ls -l afile 
-rw-r--r-- 1 root root 0 Oct 27 15:13 afile
[root@A04-R08-I132-131-8WC4F22 test]# chmod u+x afile 
[root@A04-R08-I132-131-8WC4F22 test]# ls -l afile 
-rwxr--r-- 1 root root 0 Oct 27 15:13 afile
[root@A04-R08-I132-131-8WC4F22 test]# chmod g-r afile 
[root@A04-R08-I132-131-8WC4F22 test]# ls -l afile 
-rwx---r-- 1 root root 0 Oct 27 15:13 afile
[root@A04-R08-I132-131-8WC4F22 test]# chmod o=w afile 
[root@A04-R08-I132-131-8WC4F22 test]# ls -l afile 
-rwx----w- 1 root root 0 Oct 27 15:13 afile
[root@A04-R08-I132-131-8WC4F22 test]# chmod a+r afile 
[root@A04-R08-I132-131-8WC4F22 test]# ls -l afile 
-rwxr--rw- 1 root root 0 Oct 27 15:13 afile
# 数字权限
chmod 644 afile
chmod 777 afile  # 赋予全部权限

# chown 更改属主、属组
# 工作中案例
[root@A04-R08-I132-131-8WC4F22 tmp]# mkdir test
[root@A04-R08-I132-131-8WC4F22 tmp]# ls -ld test/
drwxr-xr-x 2 root root 40 Oct 27 15:07 test/
[root@A04-R08-I132-131-8WC4F22 tmp]# chown -R work:work test/
[root@A04-R08-I132-131-8WC4F22 tmp]# ls -ld test/
drwxr-xr-x 2 work work 40 Oct 27 15:07 test/

# 极客时间案例
[root@A04-R08-I132-131-8WC4F22 tmp]# mkdir test
[root@A04-R08-I132-131-8WC4F22 tmp]# ls -ld test/
drwxr-xr-x 2 root root 40 Oct 27 15:08 test/
[root@A04-R08-I132-131-8WC4F22 tmp]# chown work test/
[root@A04-R08-I132-131-8WC4F22 tmp]# ls -ld test/
drwxr-xr-x 2 work root 40 Oct 27 15:08 test/
[root@A04-R08-I132-131-8WC4F22 tmp]# chown :work test/
[root@A04-R08-I132-131-8WC4F22 tmp]# ls -ld test/
drwxr-xr-x 2 work work 40 Oct 27 15:08 test/
[root@A04-R08-I132-131-8WC4F22 tmp]# chgrp root test/
[root@A04-R08-I132-131-8WC4F22 tmp]# ls -ld test/
drwxr-xr-x 2 work root 40 Oct 27 15:08 test/
```

### 25 权限管理以及文件的特殊权限（了解）

**特殊权限**

- SUID  用于二进制可执行文件，执行命令时取得文件属主权限
  - 如 /usr/bin/passwd
- SGID  用于目录，在该目录下创建新的文件和目录，权限自动更改为该目录的属组
- SBIT  用于目录，该目录下新建的文件和目录，仅 root 和自己可以删除
  - 如 /tmp

## 第三章 系统管理篇（29讲）

### 26 网络管理

**网络管理**

- 网络状态查看
- 网络配置
- 路由命令
- 网络故障排除
- 网络服务管理
- 常用网络配置文件

**网络状态查看工具**

- net-tools  VS  iproute

  1.net-tools

  - ifconfig
  - route
  - netstat

  2.iproute2

  - ip
  - ss

**网络状态查看命令**

- ifconfig
  - eth0  第一块网卡（网络接口）
  - 你的第一个网络接口可能叫做下面的名字
    - eno1  板载网卡
    - ens33  PCI-E 网卡
    - enp0s3  无法获取物理信息的 PCI-E 网卡
    - CentOS 7 使用了一致性网络设备命名，以上都不匹配则使用 eth0

**网络接口命名修改**

- 网卡命名规则受 biosdevname 和 net.ifnames 两个参数影响

- 编辑 /etc/default/grub 文件，增加 biosdevname=0 net.ifnames=0

- 更新 grub

  - grub2-mkconfig -o /boot/grub2/grub.cfg

- 重启

  - reboot

  ![image-20201027153957467](https://raw.githubusercontent.com/lzgkj1992/markdown_images/master/image-20201027153957467.png)

### 27 查看网络配置

略！

### 28 修改网络配置

略！

### 29 网络故障排除命令

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

**示例：**

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

### 30 网络管理和配置文件

略！

### 31 软件包管理器的使用

- 软件包管理器
- rpm包和rpm命令
- yum仓库
- 源代码编译安装
- 内核升级
- grub配置文件

### 32 使用rpm命令安装软件包

略！

### 33 使用yum包管理器安装软件包

**yum 包管理器**

- rpm 包的问题
  - 需要自己解决依赖关系
  - 软件包来源不可靠
- CentOS yum 源
  - http://mirror.centos.org/centos/7/
- 国内镜像
  - https://opsx/alibaba.com/mirror

**yum 配置文件**

- yum 配置文件

  - /etc/yum.repos.d/CentOS-Base.repo

  ![image-20201027155154697](https://raw.githubusercontent.com/lzgkj1992/markdown_images/master/image-20201027155154697.png)

  - wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
  - 替换阿里云 yum 源

  ```shell
  # 将现有yum源配置文件进行备份改名
  mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
  # 配置阿里云yum源
  wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
  # 更新缓存
  yum makecache
  # yum包更新到最新
  yum update
  # 安装vim编辑器
  yum install vim-enhanced
  ```

**yum 命令常用选项**

- 常用选项
  - install 安装软件包  `yum install elasticsearch`
  - remove 卸载软件包  `yum remove elasticsearch`
  - list | grouplist 查看软件包  `yum list | elasticsearch`
  - update 升级软件包  `yum update`

### 34 通过源代码编译安装软件包

**其他方式安装**

有时候使用yum并不能安装最新版本得软件包，这时候可以使用二进制源代码编译安装的方式。

- 二进制安装
- 源代码编译安装
  - wget https://openresty.org/download/openresty-1.15.8.1.tar.gz
  - tar -zxvf openresty-VERSION.tar.gz
  - cd openresty-VERSION
  - 安装依赖：yum install gcc gcc-c++ pcre-devel openssl-devel -y
  - ./configure --prefix=/usr/local/openresty
  - make  或者  make -j2   -j2表示使用2个逻辑内核进行编译    
  - make install

示例：二进制安装最新版本的 git

```shell
# 安装git
# 查看系统是否已经安装git
[root@A01-R06-I170-129-5001725 python3][DBA]# git --version
git version 1.8.3.1
# 已经安装，这是执行yum install git进行的安装，但是git的版本太旧，满足不了需求，我们需要安装更高版本的git，所以使用源码方式安装
# 首先卸载git
yum remove git
wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.20.0.tar.gz
tar -zxvf git-2.20.0.tar.gz 
cd git-2.20.0
# 可能需要安装一些依赖
yum install gcc gcc-c++ pcre-devel openssl-devel -y
./configure --prefix=/usr/local/git
make 或者 make -j2
make install

# 配置环境变量
vim /etc/profile
# 在最后一行添加
PATH=$PATH:/usr/local/git/bin
export PATH

# 使修改后的环境变量配置文件生效
source /etc/profile  

# 验证
[root@A01-R06-I170-129-5001725 git][DBA]# git --version
git version 2.20.0
# 安装成功
```

### 35 如何进行内核升级

略！

### 36 grub配置文件介绍

略！

### 37 使用ps和top命令查看进程

**进程管理**

- 进程的概念与进程查看
- 进程的控制命令
- 进程的通信方式——信号
- 守护进程和系统日志
- 服务管理工具 systemctl
- SELinux 简介

**进程的概念**

- 进程——运行中的程序，从程序开始运行到终止的整个生命周期是可管理的
  - C 程序的启动是从 main 函数开始的
    - int main(int agrc, char *argv[])
    - 终止的方式并不唯一，分为正常终止和异常终止
      - 正常终止也分为从 main 返回、调用 exit 等方式
      - 异常终止分为调用 abort、接收信号等

**进程的查看命令**

- 查看命令
  - ps
  - pstree
  - top
- 结论：
  - 进程也是树形结构
  - 进程和权限有着密不可分的关系

```shell
ps -eLf
ps -eLf | more
ps -eLf | grep elasticsearch

ps aux
ps aux | more

top
# 只查询18746这个进程的信息
top -p 18746
```

### 38 进程控制与进程之间的关系

**进程的优先级调整**

- 调整优先级
  - nice 范围从 -20 到 19，值越小优先级越高，抢占资源就越多 （进程启动时占用的资源情况）
  - renice 重新设置优先级 （进程运行中重新设置优先级）
- 进程的作业控制
  - jobs
  - & 符号  （进程后台运行符号）

**示例1：**（通过 nice 和 renice 命令调整进程获取资源的多少）

- 先写一个脚本 a.sh

```sh
#!/bin/bash

echo $$

while :
do
  :
done
```

- 前台运行a.sh

```shell
[root@A04-R08-I132-131-8WC4F22 lizhe]# chmod u+x a.sh
[root@A04-R08-I132-131-8WC4F22 lizhe]# ls -l a.sh
-rwxr--r-- 1 root root 42 Oct 28 20:30 a.sh
[root@A04-R08-I132-131-8WC4F22 lizhe]# ./a.sh 
19213

```

- 另起一个终端，查看19213进程的优先级。（进程启动时默认 nice 值为 0）

![image-20201028203459106](https://raw.githubusercontent.com/lzgkj1992/markdown_images/master/image-20201028203459106.png)

- 如果这个进程不重要，没必要分那么资源，那么再启动时可降低优先级，即：

```shell
[root@A04-R08-I132-131-8WC4F22 lizhe]# nice -n 10 ./a.sh 
20173

```

- 查看进程 20173 运行的优先级，即nice值

![image-20201028203924165](https://raw.githubusercontent.com/lzgkj1992/markdown_images/master/image-20201028203924165.png)



- 进一步降低进程 20173 的优先级，即在进程运行时改变资源占用优先级，使用 renice 命令，将 nice 调整成 15

```shell
[root@A04-R08-I132-131-8WC4F22 lizhe]# renice -n 15 20173
20173 (process ID) old priority 10, new priority 15
```

![image-20201028204218668](https://raw.githubusercontent.com/lzgkj1992/markdown_images/master/image-20201028204218668.png)

- 注意：PR 的值 会根据 nice 值的变化而变化

**示例2：**（进程前台和后台间的切换）

```shell
# 进程前台启动
./a.sh

# 进程后台启动
./a.sh &

# 将后台启动的进程调回到前台
[root@A04-R08-I132-131-8WC4F22 lizhe]# ./a.sh &
[1] 21655
[root@A04-R08-I132-131-8WC4F22 lizhe]# 21655

[root@A04-R08-I132-131-8WC4F22 lizhe]# jobs
[1]+  Running                 ./a.sh &
[root@A04-R08-I132-131-8WC4F22 lizhe]# fg 1
./a.sh
^C
[root@A04-R08-I132-131-8WC4F22 lizhe]# 

# 将前台启动的进程调到后台启动
[root@A04-R08-I132-131-8WC4F22 lizhe]# ./a.sh 
21840
^Z     # 使用 ctrl + z 将前台启动的进程转为后台，此时进程处理挂起状态，并没有结束
[1]+  Stopped                 ./a.sh
[root@A04-R08-I132-131-8WC4F22 lizhe]# jobs
[1]+  Stopped                 ./a.sh
[root@A04-R08-I132-131-8WC4F22 lizhe]# bg 1  # 将 后台挂起 状态的进程拉起为 后台运行 状态
[1]+ ./a.sh &
[root@A04-R08-I132-131-8WC4F22 lizhe]# jobs   
[1]+  Running                 ./a.sh &
```

**示例3：**(& 符号后台启动的进程当终端关闭后，会结束，终端关闭相当于父进程被停掉)

```shell
[root@A04-R08-I132-131-8WC4F22 ~]# tail -f /var/log/messages &
[1] 25875
[root@A04-R08-I132-131-8WC4F22 ~]# 
```

### 39 进程的通信方式与信号：kill命令

**进程间通信**

- 信号是进程间通信方式之一，典型用法是：终端用户输入中断命令，通过信号机制体制一个程序的运行。
- 使用信号的常用快捷键和命令
  - kill -l   查看所有信号
    - SIGINT（2号信号） 通知前台进程组终止进程 ctrl + c 
    - SIGKILL（9号信号）立即结束程序，不能被阻塞和处理 kill -9 pid

```shell
[root@A04-R08-I132-131-8WC4F22 ~]# kill -l
 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL	 5) SIGTRAP
 6) SIGABRT	 7) SIGBUS	 8) SIGFPE	 9) SIGKILL	10) SIGUSR1
11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM	15) SIGTERM
16) SIGSTKFLT	17) SIGCHLD	18) SIGCONT	19) SIGSTOP	20) SIGTSTP
21) SIGTTIN	22) SIGTTOU	23) SIGURG	24) SIGXCPU	25) SIGXFSZ
26) SIGVTALRM	27) SIGPROF	28) SIGWINCH	29) SIGIO	30) SIGPWR
31) SIGSYS	34) SIGRTMIN	35) SIGRTMIN+1	36) SIGRTMIN+2	37) SIGRTMIN+3
38) SIGRTMIN+4	39) SIGRTMIN+5	40) SIGRTMIN+6	41) SIGRTMIN+7	42) SIGRTMIN+8
43) SIGRTMIN+9	44) SIGRTMIN+10	45) SIGRTMIN+11	46) SIGRTMIN+12	47) SIGRTMIN+13
48) SIGRTMIN+14	49) SIGRTMIN+15	50) SIGRTMAX-14	51) SIGRTMAX-13	52) SIGRTMAX-12
53) SIGRTMAX-11	54) SIGRTMAX-10	55) SIGRTMAX-9	56) SIGRTMAX-8	57) SIGRTMAX-7
58) SIGRTMAX-6	59) SIGRTMAX-5	60) SIGRTMAX-4	61) SIGRTMAX-3	62) SIGRTMAX-2
63) SIGRTMAX-1	64) SIGRTMAX	

[root@A04-R08-I132-131-8WC4F22 ~]# netstat -ntpul | grep 9200
tcp6       0      0 10.226.132.131:9200     :::*                    LISTEN      39170/java 
[root@A04-R08-I132-131-8WC4F22 ~]# kill -9 39170
```

### 40 守护进程

**nohup 与 & 配合启动的进程**

- 讲解守护进程之前，先讲一下使用 nohup 与 & （后台启动符号）配合运行一个命令所启动的进程
  - nohup 命令使进程忽略 hangup（挂起）信号
  - nohup 命令启动的进程的输出全部打到了 nohup.out 文件中

**示例1：**

- 1、使用 tail -f 命令打开 /var/log/messages 

```shell
[root@A04-R08-I132-131-8WC4F22 lizhe]# tail -f /var/log/messages
Oct 28 20:49:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360243 of user root.
Oct 28 20:50:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360245 of user root.
Oct 28 20:50:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360246 of user root.
Oct 28 20:51:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360247 of user root.
Oct 28 20:52:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360248 of user root.
Oct 28 20:53:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360249 of user root.
Oct 28 20:54:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360250 of user root.
Oct 28 20:55:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360251 of user root.
Oct 28 20:56:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360252 of user root.
Oct 28 20:57:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360253 of user root.

```

- 2、另打开一个终端查看进程状态

```shell
[root@A04-R08-I132-131-8WC4F22 lizhe]# ps -ef | grep tail
root 26975 25309 0 16:50 pts/0  00:00:00 tail -f /var/log/messages
root 27141 27005 0 16:51 pts/1  00:00:00 grep --color=auto tail
```

- 3、如果此时将终端关闭，则进程会结束

- 4、使用 nohup 与 & 配合运行一个进程

```shell
[root@A04-R08-I132-131-8WC4F22 lizhe]# nohup tail -f /var/log/messages &
[1] 24605
[root@A04-R08-I132-131-8WC4F22 lizhe]# nohup: ignoring input and appending output to ‘nohup.out’ 忽略输入并把输出追加到“nohup.out”

[root@A04-R08-I132-131-8WC4F22 lizhe]# ps -ef | grep 'tail -f /var/log/messages'
root     24605 19481  0 21:06 pts/6    00:00:00 tail -f /var/log/messages
root     24930 19481  0 21:08 pts/6    00:00:00 grep --color=auto tail -f /var/log/messages
```

- 5、此时就算将终端关闭，进程还是会存在

```shell
[root@A04-R08-I132-131-8WC4F22 lizhe]# ps -ef | grep 'tail -f /var/log/messages'
root     24605     1  0 21:06 ?        00:00:00 tail -f /var/log/messages
root     25225 18789  0 21:10 pts/5    00:00:00 grep --color=auto tail -f /var/log/messages

# 注意：24605进程的父进程发生了变化，由原来的19481变成了1，why?关闭了终端，相当于结束了创建它的父进程，父进程结束之后，当前进程就会变成孤儿进程，孤儿进程需要被其他的父进程所收留，就会被1号进程所收留（即systemd进程）
```

- 6、使用nohup命令的目的就是为了让进程可以在关闭终端的时候，依然可以正常运行。
- 7、有没有什么进程可以在不打开终端的时候也可以正常运行呢？这就是要讲的守护进程。（在用户登录之前，启动的进程）

**守护进程**

- 机器开机就自动启动的进程，输出会打印到特殊的文件当中，所占用的目录是根目录 /
- 守护进程不需要终端，守护进程在用户登录之前启动，即机器开机就启动

- 守护进程的输出会打到某个日志文件中，比如 /var/log/messages 文件，就是某个守护进程的日志文件。
- 守护进程占用的目录为根目录，根目录只有在关机和重启机器时才有可能被卸载，这样就杜绝掉启动 daemon 进程导致 u 盘或者其他硬盘无法被卸载。
- 更深入理解请多看几遍视频。。。

### 41 screen命令和系统日志

上面提到的nohup和守护进程的目的，就是为了让用户执行的程序可以脱离终端，防止因终端关闭导致程序终止。

**使用 screen 命令**

- screen有什么作用？在进行终端操作时，先进入到screen环境中，中间即使网路断开了，screen依然可以继续运行程序，网络恢复后，可以通过screen恢复程序运行现场

- screen 进入 screen 环境
- ctrl+a d 退出（detached）screen环境
- screen -ls 查看 screen 的会话
- screen -r sessionid 恢复会话

**示例：**

```shell
[root@A04-R08-I132-131-8WC4F22 ~]# screen
-bash: screen: command not found
[root@A04-R08-I132-131-8WC4F22 ~]# yum install screen
Loaded plugins: fastestmirror, langpacks
Repodata is over 2 weeks old. Install yum-cron? Or run: yum makecache fast
http://10.226.132.139/centos/7/os/x86_64/repodata/repomd.xml: [Errno 14] HTTP Error 403 - Forbidden
Trying other mirror.
To address this issue please refer to the below knowledge base article
...
[root@A04-R08-I132-131-8WC4F22 ~]# screen  # 进入screen环境
[root@A04-R08-I132-131-8WC4F22 ~]# tail -f /var/log/messages
Oct 28 20:49:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360243 of user root.
Oct 28 20:50:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360245 of user root.
Oct 28 20:50:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360246 of user root.
Oct 28 20:51:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360247 of user root.
Oct 28 20:52:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360248 of user root.
Oct 28 20:53:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360249 of user root.
Oct 28 20:54:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360250 of user root.
...
ctrl+a,然后 d，退出screen环境
[root@A04-R08-I132-131-8WC4F22 ~]# screen -ls
There is a screen on:
	1957.tty1/localhost  (Detached)
1 Socket in /var/run/screen/S-root.
[root@A04-R08-I132-131-8WC4F22 ~]# screen -r 1957
[root@A04-R08-I132-131-8WC4F22 ~]# tail -f /var/log/messages
Oct 28 20:49:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360243 of user root.
Oct 28 20:50:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360245 of user root.
Oct 28 20:50:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360246 of user root.
Oct 28 20:51:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360247 of user root.
Oct 28 20:52:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360248 of user root.
Oct 28 20:53:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360249 of user root.
Oct 28 20:54:01 A04-R08-I132-131-8WC4F22 systemd: Started Session 360250 of user root.
...
```

**常用系统日志文件**

/var/log/ 下面有大量的系统日志文件，这些文件就叫做系统日志。需要重点关注的文件：

- /var/log/messages，系统常规运行日志
- /var/log/dmesg，系统内核相关日志
- /var/log/secure，系统安全相关日志
- /var/log/cron，系统计划任务日志

### 42 服务管理工具 systemctl（重点）

**服务管理工具systemctl**

- 服务（提供常见功能的守护进程）集中管理工具
  - service （CentOS 6及以前的版本）
  - systemctl  （CentOS 7版本+）

- systemctl 常见操作
  - systemctl start | stop | restart | reload | enable | disable 服务名称
  - 软件包安装的服务单元 /usr/lib/systemd/system/

- target-服务级别

```yaml
[root@A04-R08-I132-131-8WC4F22 ~]# cd /usr/lib/systemd/system
[root@A04-R08-I132-131-8WC4F22 system]# ls -l runlevel*.target
lrwxrwxrwx 1 root root 15 Aug 29  2019 runlevel0.target -> poweroff.target
lrwxrwxrwx 1 root root 13 Aug 29  2019 runlevel1.target -> rescue.target
lrwxrwxrwx 1 root root 17 Aug 29  2019 runlevel2.target -> multi-user.target  
lrwxrwxrwx 1 root root 17 Aug 29  2019 runlevel3.target -> multi-user.target
lrwxrwxrwx 1 root root 17 Aug 29  2019 runlevel4.target -> multi-user.target # 命令行模式
lrwxrwxrwx 1 root root 16 Aug 29  2019 runlevel5.target -> graphical.target  # 图形界面模式
lrwxrwxrwx 1 root root 13 Aug 29  2019 runlevel6.target -> reboot.target
# 查看当前系统级别
[root@A04-R08-I132-131-8WC4F22 system]# systemctl get-default
multi-user.target
# 设置系统级别
[root@A04-R08-I132-131-8WC4F22 system]# systemctl set-default multi-user.target
```

- 示例1：

```shell
[root@A04-R08-I132-131-8WC4F22 ~]# cd /usr/lib/systemd/system
[root@A04-R08-I132-131-8WC4F22 system]# vim sshd.service
# 指定启动依赖与执行顺序
[Unit]
Description=OpenSSH server daemon
Documentation=man:sshd(8) man:sshd_config(5)
After=network.target sshd-keygen.service a.service
Requires=a.service
Wants=sshd-keygen.service

# 指定启动时要执行的命令
[Service]
EnvironmentFile=/etc/sysconfig/sshd
ExecStart=/usr/sbin/sshd -D $OPTIONS
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=on-failure
RestartSec=42s

# 设置开机自启动
[Install]
WantedBy=multi-user.target
```

- 示例2：elasticsearch 自启动配置

```shell
# cd /usr/lib/systemd/system/elasticsearch_9200.service
[Unit]
Description=elasticsearch
After=network.target
[Service]
Type=simple
Environment=JAVA_HOME=/export/work/jdk
ExecStart={WORKSPACE}/elasticsearch/bin/elasticsearch --quiet
RestartSec=10s
Restart=on-failure
LimitNOFILE=65536
LimitNPROC=204800
LimitMEMLOCK=infinity
User=admin
[Install]
WantedBy=multi-user.target

# 操作命令
sudo systemctl daemon-reload
sudo systemctl start elasticsearch_9200.service
sudo systemctl stop elasticsearch_9200.service
sudo systemctl restart elasticsearch_9200.service
```

- 示例3：更详细参考文档《systemd.md》

### 43 SELinux简介

- MAC（强制访问控制）与 DAC（自主访问控制）
- 查看 SELinux 命令
  - getenforce
  - /usr/sbin/sestatus
  - ps -Z and ls -Z and id -Z

- 关闭 SELinux
  - setenforce 0
  - /etc/selinux/sysconfig

```shell
root@A04-R08-I132-131-8WC4F22 ~]# getenforce
Disabled
[root@A04-R08-I132-131-8WC4F22 ~]# cat /etc/selinux/config 
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=disabled
# SELINUXTYPE= can take one of three two values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected. 
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted
[root@A04-R08-I132-131-8WC4F22 ~]# setenforce 0^C
[root@A04-R08-I132-131-8WC4F22 ~]# ps -Z
LABEL                             PID TTY          TIME CMD
-                               18323 pts/5    00:00:00 bash
-                               18433 pts/5    00:00:00 ps
[root@A04-R08-I132-131-8WC4F22 ~]# id -Z
id: --context (-Z) works only on an SELinux-enabled kernel
[root@A04-R08-I132-131-8WC4F22 ~]# ls -Z
-rw-r--r--  root root ?                                14.sh
-rw-r--r--  root root ?                                172.19.20.105   mirrors.idc.jcloud.com
-rw-------. root root system_u:object_r:admin_home_t:s0 anaconda-ks.cfg
-rw-r--r--  root root ?                                cap.json
-rwxr-xr-x  root root ?                                cloudhsm-cap
drwxr-xr-x  root root ?                                curator_install
-rw-r--r--  root root ?                                iaas_cloud.sh
-rw-r--r--. root root system_u:object_r:admin_home_t:s0 ks-post.log
-rw-------  root root ?                                nohup.out
-rw-r--r--  root root ?                                predixy.20190510113611.log
lrwxrwxrwx  root root ?                                predixy.log -> predixy.20190510113611.log
[root@A04-R08-I132-131-8WC4F22 ~]# 
```

### 44 内存与磁盘管理

- 内存和磁盘使用率查看
- est4 文件系统
- 磁盘配额的使用
- 磁盘的分区与挂载
- 交换分区（虚拟内存）的查看与创建
- 软件 RAID 的使用
- 逻辑卷管理
- 系统综合状态查看

### 45 内存常用查看命令

**free**

```python
[root@A04-R08-I192-139-6WM0S62 users]# free
              total        used        free      shared  buff/cache   available
Mem:      131747928    68615172     3117884     2459024    60014872    59899240
Swap:      16777212           0    16777212
[root@A04-R08-I192-139-6WM0S62 users]# free -m
              total        used        free      shared  buff/cache   available
Mem:         128660       67009        2882        2401       58768       58492
Swap:         16383           0       16383
[root@A04-R08-I192-139-6WM0S62 users]# free -g   # 会舍去不足1g的部分
              total        used        free      shared  buff/cache   available
Mem:            125          65           2           2          57          57
Swap:            15           0          15
    
# buff/cache 表示缓存内存，这些内存是可以释放掉的
# available 表示如果将buff/cache中的内存全部释放掉，还有多少内存可以使用。所以，再看内存空闲的时候，不要看free，要看available。比如部署es节点，会吃掉所有内存，free剩余的内存肯定很少，但是不要担心，看一下available，available显示的才是真正还可以使用的内存
# Swap 交换分区 当你的内存真的不够用的时候，即available中显示的内存不够用时，linux系统会将暂时不需要的内存给移到Swap里面，这时你会看到Swap中used字段被占用了，不为0了。注意：交换分区所占用的空间并不在内存中，而是在磁盘上。Linux系统中的交换分区在windows系统中称为虚拟内存，这个称呼更为贴切一些。磁盘相较于内存的读写性能要慢10倍左右，所以当你发现你的程序已经开始写Swap了，证明你系统的内存真的不够用了，这时候为了程序的运行效率，是要增加内存的。
问题：既然Swap交换分区性能这么差，那不设置Swap可以吗？
答：可以。但是如果你不设置Swap分区，一旦你的内存被沾满以后，linux内核有一种机制，叫随机杀掉占用内存最大的进程。比如占用内存最大的一般都是核心应用，这些应用会被内核随机杀掉，这实际上是一件非常恐怖的事情。我们正常运维，如果程序出错，可以通过查看日志文件排查，但是像这样随机的被杀掉属于不可预知的错误，导致系统出现一些奇奇怪怪的错误，假如真的出现了这样的错误，只能重启服务了。
	针对内存一旦被用满，linux内核会随机杀掉占用内存最多的应用这样的特点，我们还是需要设置Swap交换分区的。
    当然也不排除有些例外的程序，比如像redis、memorycache、spark等内存型消耗的应用，他们的内存是没有办法交换到Swap分区中的，所以一旦发现Swap被占用了，就要立即对内存进行一个扩大或者杀掉一些不需要的应用。
```

**top**

```python
# 对于free命令，是一个静态查看内存的命令，要想看到内存的更新变化，需要不断地执行free命令
# top命令是一个可以动态查看内存的命令
[root@A04-R08-I192-139-6WM0S62 users]# top
top - 17:45:08 up 184 days, 17:34,  2 users,  load average: 3.54, 4.87, 6.09
Tasks: 682 total,   2 running, 680 sleeping,   0 stopped,   0 zombie
%Cpu(s): 12.4 us,  2.9 sy,  0.0 ni, 83.2 id,  0.0 wa,  0.0 hi,  1.4 si,  0.0 st
KiB Mem : 13174792+total,  1983868 free, 68580656 used, 61183404 buff/cache
KiB Swap: 16777212 total, 16777212 free,        0 used. 59934004 avail Mem 
   PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                            
 56298 root      20   0 85.048g 4.126g  28216 S 298.3  3.3 771254:49 java                                            
 34348 root      20   0 38.373g 2.114g  31880 S  88.8  1.7 303303:29 java                                                     
  2755 root      20   0 10.173g 125848   7456 S   2.0  0.1   4802:10 etcd                                                  
 69154 root      20   0 17.679g 1.433g  12868 S   1.3  1.1   2966:40 java                                             
  2778 work      20   0  149608  12168   1320 S   1.0  0.0   3093:44 redis-server                                          
   154 root      20   0       0      0      0 S   0.7  0.0   1472:58 rcu_sched                                               
115779 root      20   0  162800   3212   1920 R   0.7  0.0   0:01.02 top                                                   
   155 root      20   0       0      0      0 S   0.3  0.0 306:02.72 rcuos/0                                              
   157 root      20   0       0      0      0 S   0.3  0.0 306:13.22 rcuos/2                                                  
   159 root      20   0       0      0      0 S   0.3  0.0 309:27.53 rcuos/4                                                
   163 root      20   0       0      0      0 S   0.3  0.0 309:09.05 rcuos/8                                                    
  2767 work      20   0  161632  24028   1196 S   0.3  0.0 302:13.08 redis-server                                              
  2773 work      20   0  161632  24028   1300 S   0.3  0.0 279:14.93 redis-server                                              
  2784 work      20   0  173920  35132   1304 S   0.3  0.0 334:25.64 redis-server                                              
  2786 work      20   0  200544  30664   1456 S   0.3  0.0 316:57.58 redis-server                                              
  2787 work      20   0  161632  24112   1276 S   0.3  0.0 296:55.25 redis-server                                               
  2788 root      20   0   30712   3496   3496 S   0.3  0.0 150:05.58 etcd                                                       
 80379 root      20   0       0      0      0 S   0.3  0.0   0:00.52 kworker/9:1                                        
109504 root      39  19 2150416  26084   7512 S   0.3  0.0 615:35.64 hawkeye-agent                                         
127537 root      20   0       0      0      0 S   0.3  0.0   0:03.54 kworker/10:1                                       
     1 root      20   0  205260  19812   1920 S   0.0  0.0   4:51.84 systemd                                                  
     2 root      20   0       0      0      0 S   0.0  0.0   0:34.49 kthreadd                                           
     3 root      20   0       0      0      0 S   0.0  0.0  31:21.70 ksoftirqd/0                                         
     5 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/0:0H      
# ctrl + c  退出
```

### 46 磁盘分区和文件大小查看

**fdisk**

**parted**

**df**

**du**

​	du -sh data  #  查看data文件的大小

​	du -sh * | sort -hr   # 查看全部文件的大小，并从高到底进行排序

**du与ls的区别：**

```shell
# 详细使用看文档《磁盘分区挂载及分区挂载磁盘配额》
fdisk -l  # 查看磁盘分区信息

parted -l  # 查看磁盘分区信息

df -h  # 查看分区及挂载目录信息

# 查看文件大小
du -h test.txt  # 查看单个文件大小/文件夹中的所有文件的大小
[root@A04-R08-I192-75-6WK0S62 elasticsearch]# du -sh data/  # 查看文件夹总大小
129G	data/

# du 与 ls 的区别
# 查看一个文件大小的命令有两种，一种是du命令，一种是ls命令，两者有一些区别
ls -lh 文件名  # 记录的是文件从开头到结尾的总大小,可能文件有空洞，但是也会进行统计
du -h  文件名  # 记录的是文件的实际数据量大小，如果文件有空洞，不会统计
```

### 47 文件系统管理

- Linux 支持多种文件系统，常见的有：
  - ext4 （centos 6版本经常使用）
  - xfs （centos 7版本经常使用）
  - NTFS（需安装额外软件，不常用）

```shell
	linux目前支持的文件系统一般只有两种，分别是ext4文件系统和xfs文件系统。在使用fdisk命令和parted命令查看磁盘分区信息时，可以发现centos 7默认使用的文件系统是xfs，而centos 6经常使用的文件系统是ext4。对于xfs和ext4文件系统，两者在底层方面的差异，可以自行百度。但是在实际工作和生产环境中，这两个文件系统的差异不大，都是非常稳定的，建议如果是centos 6，就使用ext4，如果是centos 7，就使用xfs。	
	为什么不推荐使用NTFS文件系统？因为Linux系统默认是不支持NTFS文件系统的，我们基本不能在Linux系统中挂载NTFS文件系统类型的硬盘或移动硬盘。为此，最主要的问题是如何使Linux系统支持NTFS文件系统。
	一般情况下，在Linux系统中，我们并不需要手动安装某些驱动，因为，大多数驱动Linux系统的内核都已经默认可以支持了。但是，某些最新的硬件设备的驱动或NTFS文件系统的驱动，对于我们当前的Linux系统版本，可能就无法支持了。那么，我们至少有两种方法来使Linux系统支持NTFS文件系统：
	1、重新编译Linux系统的内核（过于复杂，不推荐）
	2、手动下载安装NTFS文件系统的驱动，下载安装NTFS-3G插件来使Linux系统支持NTFS文件系统
```

ext4 文件系统

- ext4 文件系统基本结构比较复杂
  - 超级块
  - 超级块副本
  - i节点（inode）
  - 数据块（datablock）

```python
	通过ext4文件系统来讲解文件系统的底层结构。第一部分是超级块，是ext4文件系统最开头的部分。超级块中记录着整个文件系统中或整个分区中包含了多少文件，所有文件的总数是多少。我们在使用df -h 命令时，可以发现特别快就统计出来了分区中共包含多少文件，共占用多少空间，这类信息。为什么这么快？因为这些数据都是提前统计好的，当你创建新文件，写入新数据时，超级块会自动进行更新。df -h命令查看到的信息都叫做超级块信息，那么这么重要的信息当然要有备份了，所以文件系统中还有一部分称之为超级块副本，来保证一旦超级块中的数据丢失了，可以通过超级块副本对数据进行还原。我们经常说的磁盘被误格式化了，要恢复数据，说的就是恢复超级块上的数据。
    更重要的两个是i节点（inode）、数据块（datablock）。i 节点是用来记录每一个文件的名称、大小、编号等信息，文件都是有唯一编号的，还有文件的权限，在i节点中都有体现。大家要注意一下，文件的文件名和编号并没有记录在同一个i节点中。文件名记录在自己文件的父目录的i节点里面。
[root@A04-R08-I192-75-6WK0S62 config]# ls -l
total 40
-rw-rw---- 1 work work   207 Jan  6 16:40 elasticsearch.keystore
-rw-r--r-- 1 work work  2003 Apr 15 11:56 elasticsearch.yml
-rw-r----- 1 work work  2853 Jan  6 16:30 elasticsearch.yml.old
-rw-r----- 1 work work  3196 Jan  6 16:30 jvm.options
-rw-r----- 1 work work 12423 Jan  6 16:30 log4j2.properties
-rw-r----- 1 work work   473 Jan  6 16:30 role_mapping.yml
-rw-r----- 1 work work   197 Jan  6 16:30 roles.yml
-rw-r----- 1 work work     0 Jan  6 16:30 users
-rw-r----- 1 work work     0 Jan  6 16:30 users_roles
注意：-rw-rw---- 1 work work   207 Jan  6 16:40 elasticsearch.keystore  除了文件名elasticsearch.keystore以外，其他的信息全部是记录在文件的i节点中的。文件名是记录在该文件的父目录的i节点中的。
    
[root@A04-R08-I192-75-6WK0S62 config]# ls -i
2050528 elasticsearch.keystore  2108731 elasticsearch.yml.old    
2050553 log4j2.properties       2050576 roles.yml          2050574 users_roles
268417930 elasticsearch.yml     2050586 jvm.options        2050580 role_mapping.yml

ls -i命令可以查看文件的i节点信息。2050528 elasticsearch.keystore，其中，2050528指的是文件的i节点的id，elasticsearch.keystore是文件的文件名，它是记录在该文件的父目录的i节点中。

这样就能很好的解释文件权限和目录权限的区别了。
[root@A04-R08-I192-75-6WK0S62 elasticsearch]# ls -l
-rw-r--r--  1 work work  13675 Jan  6 16:30 LICENSE.txt   # 文件
drwxr-xr-x  3 work work   4096 Jan  6 16:30 bin   # 目录
文件权限中的读权限是指读取文件中的内容，这些内容在哪？在datablock里面。对于目录来说，目录中的读权限指的是读取目录下面文件的文件名。所以普通文件与目录文件的权限方面是有不同的含义的。

数据块（datablock）是用来记录数据的。i节点就像火车头一样，如果写入的数据一个数据块就可以装下了，那么会在i节点后面挂着一个数据块。如果一个数据块装不下，系统会创建更多的数据块，将之挂在前面的数据块之后。这种结构被称为链接式的结构。在这种结构中，只要找到i节点，就可以找到有多少数据块了，就可以根据数据块的多少来统计文件的大小。如果数据块为空，这就是为什么du命令和ls -lh命令统计出来的文件大小会有差异的原因。ls -lh统计的是datablock的数量，空的也会进行统计。而du统计的是datablock的实际大小。
```

### 48 i节点和数据块操作

示例1：

```python
[root@A04-R08-I192-75-6WK0S62 lizhe]# touch afile
[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile 
2148488884 -rw-r--r-- 1 root root 0 Apr 18 14:56 afile
[root@A04-R08-I192-75-6WK0S62 lizhe]# du -h afile 
0	afile
[root@A04-R08-I192-75-6WK0S62 lizhe]# echo 123 > afile 
[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile 
2148488884 -rw-r--r-- 1 root root 4 Apr 18 14:56 afile  # 大小是4个字节
[root@A04-R08-I192-75-6WK0S62 lizhe]# du -h afile 
4.0K	afile   
# 在xfs和ext4文件系统中，默认创建的一个datalock的大小就是4k，即使只写了一个字符，大小也是4k
# 这样，大家可能就会一个问题，如果在linux系统中存储了特别多的小文件，磁盘的开销是会非常大的。现在已经发明了很多专门存储小文件的网络文件系统。大家可以搜索一下，如何存储大量的小文件？

[root@A04-R08-I192-75-6WK0S62 lizhe]# cp afile afile2
[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile*
2148488884 -rw-r--r-- 1 root root 4 Apr 18 14:56 afile
2147850696 -rw-r--r-- 1 root root 4 Apr 18 15:03 afile2

# 使用cp复制后，发现两个文件的i节点是不同的，这两个是完全不同的文件，修改其中一个，不会影响另一个

[root@A04-R08-I192-75-6WK0S62 lizhe]# pwd
/export/user/lizhe/lizhe
[root@A04-R08-I192-75-6WK0S62 lizhe]# mv afile2 afile3
[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile*
2148488884 -rw-r--r-- 1 root root 4 Apr 18 14:56 afile
2147850696 -rw-r--r-- 1 root root 4 Apr 18 15:03 afile3

# 执行mv命令进行改名，将afile2改成afile3，文件的i节点没有任何变化，还是同一个文件。它改的只是/export/user/lizhe/lizhe目录的i节点中记录的文件名，
# 这个时候，你会发现，不管你的文件有多大，哪怕几百GB，改名也是瞬间完成的，这是因为改名改的文件父目录i节点中记录的文件名信息，而对文件的i节点和datalock数据块没有任何改变。

# 如果使用mv命令将文件移动到其它位置，花费的时间会不会很长呢？分两种情况：
# 1.如果这个其他位置还是在同一个分区内，则移动也是瞬间完成的。因为i节点和datalock是由整个文件系统管理的，如果你是在当前的文件系统里面对这个文件进行移动，只是改变了指定目录的文件名称的链接，也是瞬间完成的。
# 2.如果这个其他位置不是同一个分区内，则需要花费较长的时间
```

示例2：

```python
[root@A04-R08-I192-75-6WK0S62 lizhe]# vim afile4
[root@A04-R08-I192-75-6WK0S62 lizhe]# 
[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile4
2149747466 -rw-r--r-- 1 root root 4 Apr 18 15:15 afile4
[root@A04-R08-I192-75-6WK0S62 lizhe]# vim afile4
[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile4
2147984343 -rw-r--r-- 1 root root 8 Apr 18 15:15 afile4

# 上述实验表明，通过vim命令修改文件，会改变文件的i节点地址，可以通过硬链接的方式避免

[root@A04-R08-I192-75-6WK0S62 lizhe]# echo 789 > afile4
[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile4
2147984343 -rw-r--r-- 1 root root 4 Apr 18 15:17 afile4

# 通过echo 写入的方式修改文件，不会改变文件的i节点
# 当使用vim afile4 打开afile4文件时，会生成一个.afile4.swp文件，只有当wq保存修改并退出后，.afile4.swp才会替换掉原来的afile4文件（这也是为什么使用vim编辑文件后，文件的i节点会改变的原因）。这样的好处是当我们的文件被被人读取的时候，还是一个原始的状态，只有别人wq保存修改并退出后，才会替换掉原来的文件。还有就是当你vim编辑到一半时，系统宕机了，这个编辑到一半.afile4.swp文件还是会存在的。这是vim对文件一致性的考虑。
# 不可以同时对一个文件执行两次vim操作，只能这次执行完，下次再执行，否则会报错。。。

[root@A04-R08-I192-75-6WK0S62 lizhe]# \rm afile4

# rm 删除命令，断开的是文件名与文件i节点之间的连接。所以，不管你是删除多大的文件，删除的时间都是一样的。
# 这样就为找回误删除的文件提供了依据。如果文件被误删除了，我们应该立即断电，然后拿着硬盘找到专业维修的人员，拿着专业维修的工具，扫描硬盘中的i节点，然后找到对应的datalock数据块，进行恢复数据。这就是文件恢复的秘密。

# 硬链接
# 让更多的文件名指向i节点，避免误删除的问题
[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile
2148488884 -rw-r--r-- 1 root root 4 Apr 18 14:56 afile
[root@A04-R08-I192-75-6WK0S62 lizhe]# ln afile bfile
[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile
2148488884 -rw-r--r-- 2 root root 4 Apr 18 14:56 afile
[root@A04-R08-I192-75-6WK0S62 lizhe]# \rm -rf bfile 
[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile
2148488884 -rw-r--r-- 1 root root 4 Apr 18 14:56 afile
[root@A04-R08-I192-75-6WK0S62 lizhe]# \rm -rf afile
[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile
ls: cannot access afile: No such file or directory

# 当文件的链接数为0时，系统就会释放文件对应的空间了。和java中的引用概念类似。

# 使用ln 命令，是不能跨越文件系统的，也即是说，使用硬链接不能跨域文件系统。
# 若非要跨越分区，还想要这种链接形式的话，可以使用软链接

[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile
2148007884 -rw-r--r-- 1 root root 0 Apr 18 15:38 afile
[root@A04-R08-I192-75-6WK0S62 lizhe]# ln -s afile aafile
[root@A04-R08-I192-75-6WK0S62 lizhe]# ls -li afile aafile 
2148008041 lrwxrwxrwx 1 root root 5 Apr 18 15:38 aafile -> afile
2148007884 -rw-r--r-- 1 root root 0 Apr 18 15:38 afile

# 可以看到，使用软链接，会生成一个新的文件，这个软链接也称之为符号链接，它对应的i节点中记录的是目标文件的路径。
# 软连接和硬链接是有区别的，软链接会新建的一个文件，该文件中记录的是目标文件的路径，软链接可以实现跨文件系统/或者说跨分区进行访问，修改软链接实际上修改的是目录文件。
```

### 49 分区与挂载

常用命令：

​	fdisk

​	mkfs

​	parted

​	mount

常见配置文件：

​	/etc/fstab

#### fdisk命令：

```python
fdisk -l  # 查看机器分区信息

fdisk /dev/sdb  # 对/dev/sdb 磁盘进行分区，分区之前要确保磁盘中是没有数据的

m # 查看fdisk命令帮助信息

n # 进行分区

p # 进行主分区

分区号：1  # 分区号默认为1，即sdb1

起始 扇区 （2048-134217727，默认为 2048）：
将使用默认值 2048
Last 扇区，+扇区 or +size{K,M,G} (2048-134217727，默认为 134217727)：+50G 

# 上述配置是说给sdb1扇区分50GB大小
# 若全部采用默认值，则将所有磁盘资源分配给sdb1扇区

p  # 查看当前分区

w  # 保存配置，将配置由内存同步到磁盘

q # 不保存并退出fdisk交互界面

# 格式化
mkfs.xfs /dev/sdb1   # 将/dev/sdb1盘符格式化

# 挂载目录
[root@A01-R06-I5-230-4000048 --prod-- export]# mkdir -p /export/  # -p 表示，如果目录不存在则新建，如果目录存在，则不创建
[root@A01-R06-I5-230-4000048 --prod-- export]# mount /dev/sdb1 /export/
[root@A01-R06-I5-230-4000048 --prod-- export]# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda3       100G  2.5G   98G   3% /
devtmpfs         63G     0   63G   0% /dev
tmpfs            63G     0   63G   0% /dev/shm
tmpfs            63G   18M   63G   1% /run
tmpfs            63G     0   63G   0% /sys/fs/cgroup
/dev/sda1      1014M  194M  821M  20% /boot
tmpfs            13G     0   13G   0% /run/user/0
/dev/sdb1       8.8T   33M  8.8T   1% /export

# 根据df -h返回的信息可知，已成功完成sdb磁盘的分区与挂载，但此时只是临时的分区与挂载，机器重启后会失效，要想使用永久配置，需要将分区与挂载的信息写入/etc/fstab 文件

[root@A01-R06-I5-230-4000048 --prod-- export]# echo "/dev/sdb1 /export xfs defaults 0 0" >>/etc/fstab
[root@A01-R06-I5-230-4000048 --prod-- export]# cat /etc/fstab 
LABEL=label_boot   /boot                   xfs     defaults        0 0
LABEL=label_swap    swap                    swap                   defaults        0 0
LABEL=label_root    /                       xfs     defaults        0 0
/dev/sdb1 /export xfs defaults 0 0

# 这样机器重启后，分区与挂载信息也不会丢失

# 注意：分区与挂载后，/export 中的数据会被初始化，要谨慎操作。。。
```

#### parted命令：

fdisk -l 命令可以用来查看分区信息

```python
[root@A01-R06-I5-230-4000048 --prod-- export]# fdisk -l

Disk /dev/sda: 299.0 GB, 298999349248 bytes, 583983104 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disk label type: dos
Disk identifier: 0x0003a8e1

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200    35651583    16776192   82  Linux swap / Solaris
/dev/sda3        35651584   245417983   104883200   83  Linux
/dev/sda4       245417984   583983103   169282560    f  W95 Ext'd (LBA)

Disk /dev/sdb: 9595.0 GB, 9594999930880 bytes, 18740234240 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
```

mount 命令可以用来查看挂载信息

```shell
[root@A04-R08-I132-131-8WC4F22 ~]# mount
```

若磁盘空间小于2T，可以用fdisk命令进行分区；

若磁盘空间大于2T，只能用parted命令进行分区

操作步骤：

```python
[root@A01-R06-I5-230-4000048 --prod-- export]# fdisk -l

Disk /dev/sda: 299.0 GB, 298999349248 bytes, 583983104 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disk label type: dos
Disk identifier: 0x0003a8e1

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200    35651583    16776192   82  Linux swap / Solaris
/dev/sda3        35651584   245417983   104883200   83  Linux
/dev/sda4       245417984   583983103   169282560    f  W95 Ext'd (LBA)

Disk /dev/sdb: 9595.0 GB, 9594999930880 bytes, 18740234240 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes

# 从fdisk -l 命令返回的信息来看，sdb磁盘尚没有分区
# 因为sdb磁盘的空间为 9595.0 GB，大于2T，所以需要使用parted命令对于进行分区

[root@A01-R06-I5-230-4000048 --prod-- export]# parted /dev/sdb
GNU Parted 3.1
Using /dev/sdb
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) mklabel gpt
(parted) mkpart primary 0 -1                                              
Warning: The resulting partition is not properly aligned for best performance.
Ignore/Cancel? Ignore                                                     
(parted) p                                                                
Model: LSI Logical Volume (scsi)
Disk /dev/sdb: 9595GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name     Flags
 1      17.4kB  9595GB  9595GB               primary

(parted) q                                                                
Information: You may need to update /etc/fstab.  # 提示现在的分区只是完成了临时的，重启后就会失效，如果要永久生效，需要将分区信息写入 /etc/fstab 文件，这里暂时不用写入，挂载完成后，与挂载操作一起写入
    
# 格式化  -f 参数表示强制格式化
[root@A01-R06-I5-230-4000048 --prod-- export]# mkfs.xfs /dev/sdb1
warning: device is not properly aligned /dev/sdb1
Use -f to force usage of a misaligned device
[root@A01-R06-I5-230-4000048 --prod-- export]# mkfs.xfs -f /dev/sdb1
warning: device is not properly aligned /dev/sdb1
meta-data=/dev/sdb1              isize=256    agcount=9, agsize=268435455 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=0        finobt=0
data     =                       bsize=4096   blocks=2342529031, imaxpct=5
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=0
log      =internal log           bsize=4096   blocks=521728, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0

# 挂载目录
[root@A01-R06-I5-230-4000048 --prod-- export]# mkdir -p /export/  # -p 表示，如果目录不存在则新建，如果目录存在，则不创建
[root@A01-R06-I5-230-4000048 --prod-- export]# mount /dev/sdb1 /export/
[root@A01-R06-I5-230-4000048 --prod-- export]# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda3       100G  2.5G   98G   3% /
devtmpfs         63G     0   63G   0% /dev
tmpfs            63G     0   63G   0% /dev/shm
tmpfs            63G   18M   63G   1% /run
tmpfs            63G     0   63G   0% /sys/fs/cgroup
/dev/sda1      1014M  194M  821M  20% /boot
tmpfs            13G     0   13G   0% /run/user/0
/dev/sdb1       8.8T   33M  8.8T   1% /export

# 根据df -h返回的信息可知，已成功完成sdb磁盘的分区与挂载，但此时只是临时的分区与挂载，机器重启后会失效，要想使用永久配置，需要将分区与挂载的信息写入/etc/fstab 文件

[root@A01-R06-I5-230-4000048 --prod-- export]# echo "/dev/sdb1 /export xfs defaults 0 0" >>/etc/fstab
[root@A01-R06-I5-230-4000048 --prod-- export]# cat /etc/fstab 
LABEL=label_boot   /boot                   xfs     defaults        0 0
LABEL=label_swap    swap                    swap                   defaults        0 0
LABEL=label_root    /                       xfs     defaults        0 0
/dev/sdb1 /export xfs defaults 0 0

# 这样机器重启后，分区与挂载信息也不会丢失

# 注意：分区与挂载后，/export 中的数据会被初始化，要谨慎操作。。。
```

### 50 分区和挂载磁盘配额

**用户磁盘配额（用于限制用户可以用多少磁盘资源）**

- xfs 文件系统的用户磁盘配额 quota
- mkfs.xfs /dev/sdb1
- mkdir /mnt/disk1
- mount -o uquota.gquota /dev/sdb1 /mnt/disk1
- chmod 1777

- xfs_quota -x -c 'report -ugibh' /mnt/disk1
- xfs_quota -x -c 'limit -u isoft=5 ihard=10 user1' /mnt/disk1

需要用的时候看极客时间视频！！！

### 51 交换分区swap的查看与创建

**交换分区**

- 增加交换分区的大小
  - mkswap
  - swapon
- 使用文件制作交换分区
  - dd if=/dev/zero bs=4M count=1024 of=/swapfile

```shell
[root@A04-R08-I132-131-8WC4F22 ~]# free -g
              total        used        free      shared  buff/cache   available
Mem:            125          70           4           1          51          53
Swap:            15           0          15
```

### 52 软件RAID的使用及RAID扩展知识

#### RAID与软件RAID技术

- RAID的常见级别及含义
  - RAID 0 striping条带方式，提高单盘吞吐率
  - RAID 1 mirroring镜像方式，提高可靠性
  - RAID 5 有奇偶校验
  - RAID 10 是RAID 1与RAID 0的结合

【注释】实现 RAID，光靠硬盘是办不到的，在服务器上是有一个raid控制器的，或者称之为raid卡，这个硬件设备。这个硬件设备通过数据的读写会自动计算校验值，自动计算数据是放在那一块硬盘上的。甚至raid卡还带有缓存功能，加速对硬盘的访问。

- 软件 RAID 的使用

  软件实现的raid功能有一个前提条件，就是cpu使用率要有大量的空闲，系统对cpu的开销不能很高。因为当你实现软件raid，当有大量读写的时候，cpu使用率是非常高的。所以一般软件 raid 只用来演示，工作中都是会使用raid控制器（raid卡）这个一个硬件设备

```python
# 如何用软件实现磁盘阵列呢？
需要的时候看极客时间视频！！！
```

### 53 逻辑卷LVM的用途与创建

需要的时候看极客时间视频！！！

### 54 系统综合状态查看命令sar以及第三方命令

系统综合状态查询

- 使用 sar 命令查看系统综合状态，系统默认自带
- 使用第三方命令查看网络流量
  - yum install epel-release
  - yum install iftop
  - iftop -p

**sar命令**

```python
# 查看cpu使用情况
[root@A04-R08-I192-75-6WK0S62 lizhe]# sar -u 1 5
Linux 3.10.0-327.36.4.el7.x86_64 (A04-R08-I192-75-6WK0S62.JCLOUD.COM) 	04/18/2020 	_x86_64_	(32 CPU)

06:23:19 PM     CPU     %user     %nice   %system   %iowait    %steal     %idle
06:23:20 PM     all      5.15      0.00      1.57      0.03      0.00     93.25
06:23:21 PM     all      5.25      0.00      2.07      0.03      0.00     92.65
06:23:22 PM     all      5.16      0.00      2.33      0.13      0.00     92.39
06:23:23 PM     all      6.14      0.00      2.17      0.03      0.00     91.66
06:23:24 PM     all      6.01      0.03      1.92      0.03      0.00     92.01
Average:        all      5.54      0.01      2.01      0.05      0.00     92.39

# 查看内存使用情况
[root@A04-R08-I192-75-6WK0S62 lizhe]# sar -r 1 5
Linux 3.10.0-327.36.4.el7.x86_64 (A04-R08-I192-75-6WK0S62.JCLOUD.COM) 	04/18/2020 	_x86_64_	(32 CPU)

06:25:07 PM kbmemfree kbmemused  %memused kbbuffers  kbcached  kbcommit   %commit  kbactive   kbinact   kbdirty
06:25:08 PM   2646824 129101104     97.99         8  74063440  81277700     54.72  45647488  37385440     70744
06:25:09 PM   2644940 129102988     97.99         8  74066732  81277700     54.72  45647548  37387672     70084
06:25:10 PM   2640964 129106964     98.00         8  74070428  81277700     54.72  45649648  37390272     70220
06:25:11 PM   2628200 129119728     98.01         8  74080080  81277700     54.72  45655540  37397548     72340
06:25:12 PM   2620736 129127192     98.01         8  74089924  81277700     54.72  45660972  37402196     80232
Average:      2636333 129111595     98.00         8  74074121  81277700     54.72  45652239  37392626     72724

    
# 查看磁盘io读写情况
[root@A04-R08-I192-75-6WK0S62 lizhe]# sar -b 1 5
Linux 3.10.0-327.36.4.el7.x86_64 (A04-R08-I192-75-6WK0S62.JCLOUD.COM) 	04/18/2020 	_x86_64_	(32 CPU)

06:26:20 PM       tps      rtps      wtps   bread/s   bwrtn/s
06:26:21 PM    172.00      0.00    172.00      0.00  13614.00
06:26:22 PM   1012.00      0.00   1012.00      0.00  28713.00
06:26:23 PM    313.00      0.00    313.00      0.00  39627.00
06:26:24 PM    157.00      0.00    157.00      0.00  17013.00
06:26:25 PM    149.00      0.00    149.00      0.00  17207.00
Average:       360.60      0.00    360.60      0.00  23234.80

    
# 查看具体磁盘的读写情况
[root@A04-R08-I192-75-6WK0S62 lizhe]# sar -d 1 5
Linux 3.10.0-327.36.4.el7.x86_64 (A04-R08-I192-75-6WK0S62.JCLOUD.COM) 	04/18/2020 	_x86_64_	(32 CPU)

06:27:07 PM       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
06:27:08 PM   dev8-16    132.00      0.00   8781.00     66.52      0.01      0.12      0.03      0.40
06:27:08 PM    dev8-0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

06:27:08 PM       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
06:27:09 PM   dev8-16    134.00      0.00  15723.00    117.34      0.04      0.30      0.09      1.20
06:27:09 PM    dev8-0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

06:27:09 PM       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
06:27:10 PM   dev8-16    117.00      0.00  10771.00     92.06      0.01      0.06      0.03      0.30
06:27:10 PM    dev8-0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

06:27:10 PM       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
06:27:11 PM   dev8-16    216.00      0.00  12308.00     56.98      0.02      0.08      0.05      1.00
06:27:11 PM    dev8-0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

06:27:11 PM       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
06:27:12 PM   dev8-16    240.00      0.00  10598.00     44.16      0.02      0.10      0.05      1.20
06:27:12 PM    dev8-0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

Average:          DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
Average:      dev8-16    167.80      0.00  11636.20     69.35      0.02      0.13      0.05      0.82
Average:       dev8-0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00


# 查看进程的使用情况
[root@A04-R08-I192-75-6WK0S62 lizhe]# sar -q 1 5
Linux 3.10.0-327.36.4.el7.x86_64 (A04-R08-I192-75-6WK0S62.JCLOUD.COM) 	04/18/2020 	_x86_64_	(32 CPU)

06:28:01 PM   runq-sz  plist-sz   ldavg-1   ldavg-5  ldavg-15   blocked
06:28:02 PM         2      1581      2.54      2.59      2.45         0
06:28:03 PM         2      1581      2.54      2.59      2.45         0
06:28:04 PM         5      1581      2.54      2.59      2.45         0
06:28:05 PM         4      1582      2.54      2.59      2.45         0
06:28:06 PM         2      1582      2.54      2.59      2.45         0
Average:            3      1581      2.54      2.59      2.45         0
```

**iftop命令**

使用第三方命令查看网络流量

- yum install epel-release
- yum install iftop
- iftop -p   默认只监听eth0接口

```python
[root@A04-R08-I192-75-6WK0S62 lizhe]# iftop -p
bash: iftop: command not found
# 尚未安装，需要安装一下

[root@A04-R08-I192-75-6WK0S62 users]# yum install epel-release
[root@A04-R08-I192-75-6WK0S62 users]# yum install iftop
[root@A04-R08-I192-75-6WK0S62 users]# iftop -p
```

## 第四章 Shell篇

### 55 什么是shell

- Shell 是命令解释器，用于解释用户对操作系统的操作

```
	一句话来概括Shell，Shell会将用户执行的命令翻译给内核，然后内核根据命令执行的结果反馈给用户。
	那具体流程是怎样的？例如：用Shell解释ls命令，当输入ls回车的时候，首先由Shell接收到用户执行的命令，接收完后对命令的选项和参数进行分析，分析之后知道ls是查看文件的，分析之后会交给文件系统，文件系统在内核层，文件系统将ls要查看的文件和目录翻译成对应硬盘的扇区，当然ssd硬盘是另外的一种结构，硬件会将查询到的结果交给内核，内核返回给Shell，最终再返回给用户。我们可以发现，将Shell写好的话，用户是不需要写底层驱动程序的，也不需要开发复杂的c语言，通过简单的命令就可以控制内核和操作系统，做很多自己想做的事情。
	这就是Shell解释器最主要的功能，用户不需要去了解底层的知识。
```

- Shell 有很多
  
  - cat /etc/shells
  
  ```shell
  [root@A04-R08-I132-131-8WC4F22 ~]# cat /etc/shells 
  /bin/sh
  /bin/bash
  /sbin/nologin
  /usr/bin/sh
  /usr/bin/bash
  /usr/sbin/nologin
  /bin/tcsh
  /bin/csh
  ```
  
- CentOS 7 默认使用的 Shell 是 bash

### 56 Linux的启动过程

- BIOS - MBR - BootLoader(grub) - kernel - systemd - 系统初始化 - shell

待补充！

### 57 Shell脚本的格式

- UNIX 的哲学：一条命令只做一件事
- 为了组合命令和多次执行，使用脚本文件来保存需要执行的命令
- 赋予该文件执行权限（chmod u+rx filename）

**示例**

`vim 1.sh`

```shell
#!/bin/bash
# demo
cd /var/
ls
pwd
du -sh
du -sh *
```

`chomd u+x 1.sh`

`bash 1.sh`

### 58 脚本不同执行方式的影响

**标准的Shell脚本要包含哪些元素**

- Sha-Bang     shell 脚本第一行    `#!/bin/bash`

如果使用 bash 启动脚本，那么这一行就是注释；如果使用 ./ 启动脚本，那这一行就是告诉系统要用 bash 解释器

- 命令
- “#” 号开头的注释
- chmod u+rx filename 可执行权限
- 执行命令
  - `bash ./filename.sh` ，会生成子shell 
  - `./filename.sh`   # 需要有可执行权限   chmod u+x filename.sh，会生成子shell
  - `source ./filename.sh` ，不会生成子shell
  - `. ./filename.sh`   #  等同于`source ./filename.sh`，不会生成子shell

**示例：**

```shell
[root@A04-R08-I132-131-8WC4F22 tmp]# a=100
[root@A04-R08-I132-131-8WC4F22 tmp]# echo $a
100
[root@A04-R08-I132-131-8WC4F22 tmp]# vim test.sh
echo $a
[root@A04-R08-I132-131-8WC4F22 tmp]# chmod +x test.sh
[root@A04-R08-I132-131-8WC4F22 tmp]# bash test.sh 

[root@A04-R08-I132-131-8WC4F22 tmp]# ./test.sh 

[root@A04-R08-I132-131-8WC4F22 tmp]# source test.sh 
100
[root@A04-R08-I132-131-8WC4F22 tmp]# . ./test.sh 
100

# 若想让 bash 和 ./ 也能拿到变量 a, 可以 export 一下，export a, 相当于将 a 设置为环境变量
```

### 59~60 管道与重定向

**管道与管道符**

- 管道和信号一样，也是进程通信的方式之一
- 匿名管道（管道符）是 Shell 编程经常用到的通信工具
- 管道符是 “|”，将前一个命令执行的结果传递给后面的命令
  - `ps | cat`
  - `echo 123 | ps`

**重定向**

- 一个进程默认会打开标准输入、标准输出、错误输出三个文件描述符

- 输入重定向符号  “<”
  
  - `<`
  - `<<`
  
  - `read var < /path/to/a/file`
  
- 输出重定向符号  “>”  ">>"  "2>"  "&>"
  
  - `echo 123 > /path/to/a/file`
  - `> 重定向后会覆盖原有的信息`
  - `>> 追加重定向`
  - `2> 错误信息重定向`
  - `&> 全部信息重定向`
  
- 输入和输出重定向组合使用
  - `cat > /path/to/a/file << EOF`
  - `I am $USER`
  - `EOF`

**示例：**

```shell
[root@lizhe]# wc -l   # 统计输入的行数
123
456
2
[root@lizhe]# wc -l < /etc/passwd  # 统计/etc/passwd 文件的行数
26
[root@lizhe]# read var  # 将输入的内容赋值给变量 var
123
[root@lizhe]# echo $var  # 打印变量 var
123

### 输入和输出重定向结合使用
#vim a.sh
#!/bin/bash
cat > /root/a.sh <<EOF
echo "hello bash"
EOF
```

### 61 变量赋值

变量的定义

- 变量名的命名规则
  - 字母、数字、下划线
  - 不以数字开头

变量的赋值

- 为变量赋值的过程，称为变量替换
  - 变量名=变量值
    - `a=123`
  - 使用let为变量赋值
    - `let a=10+20`
  - 将命令赋值给变量
    - `l=ls`
  - 将命令结果赋值给变量，使用$()或者反引号``
    - `letc=$(ls -l /etc)`
  - 变量值有空格等特殊字符可以包含在双引号“ ”或单引号‘ ’中
  

**示例：**

```shell
[root@python]# a=123
[root@python]# a =123
-bash: a: command not found
[root@python]# a= 123
-bash: 123: command not found
[root@python]# cmd1=`ls ./`
[root@python]# cmd2=$(ls ./)
[root@python]# echo $cmd1
a.sh b.sh
[root@python]# string1="hello bash"
[root@python]# echo $string1
hello bash
```

### 62 变量引用及作用范围

- 变量的引用
  - ${变量名} 称作对变量的引用
  - echo ${变量名} 查看变量的值
  - ${变量名} 在部分情况下可以省略为 $变量名
  
  示例：
  
  ```shell
  # 什么时候用 ${变量名}？ 什么时候用 $变量名
  [root@python]# string1="hello bash"
  [root@python]# echo ${string1}
  hello bash
  [root@python]# echo $string1
  hello bash
  [root@python]# echo $string123
  
  [root@python]# echo ${string1}23
  hello bash23
  ```
  
- 变量的作用范围

  定义好的变量默认只针对当前的终端，即当前的 shell 生效，如果在当前的 shell 下面再去产生新的 子shell，或者是与当前shell平行的shell，或者是当前shell的父进程，该变量都是不生效的。

- 变量的导出

  - export

- 变量的删除

  - unset

**示例：**

```shell
[root@python]# a=1  # 在当前shell定义一个变量a并赋值
[root@python]# bash  # 生成一个子shell并进入
[root@python]# echo $a  # 在子shell中打印shell中定义的变量a，发现找不到

[root@python]# a=2  # 在子shell中定义一个变量a，并赋值2
[root@python]# exit  # 退出子shell
exit
[root@python]# echo $a  # 打印变量a，发现还是当前shell中赋予的值
1
# 变量的作用范围是当前shell
# 问题1：在当前shell中定义的变量，是否可以在shell脚本中进行引用呢？要看执行脚本的方式
## bash test.sh，会生成子shell，不可用
## source test.sh，可以用
[root@python]# demo_var1="hello subshell"
[root@python]# vim 4.sh
[root@python]# chmod u+x 4.sh
[root@python]# bash 4.sh 

[root@python]# ./4.sh 

[root@python]# source 4.sh 
hello subshell
[root@python]# . 4.sh 
hello subshell

# 问题2：能不能扩展一下，让子进程可以得到父进程的变量，即让子shell能够获得父shell的变量
# 在linux中，这个功能已经实现了，就是需要在定义变量的时候增加一个关键子，export
[root@python]# export demo_var1="hello subshell"
[root@python]# vim 4.sh
[root@python]# bash 4.sh
hello subshell
[root@python]# ./4.sh 
hello subshell
[root@python]# unset demo_var1  # 删除变量
```

### 63 环境变量、预定义变量与位置变量

- 环境变量：每个Shell打开都可以获得到的变量
- 所有环境变量都通过 export 进行了导出，所有在shell和子shell中都生效
  - set 和 env 命令
  - $? $$ $0
  - $PATH
  - $PS1
- 位置变量
  - $1 $2 ... ${10}... $n

示例：

```shell
# 环境变量
[root@python]# env | more  # env 查看当前系统中的所有环境变量
[root@python]# set | more  # set 可以查看更多的变量
[root@python]# echo $USER  # 查看某一具体环境变量，和查看普通变量方法一样
root
[root@python]# echo $UID
0
[root@python]# echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/export/work/jdk/bin:/root/bin

# 预定义变量
[root@python]# echo $?  # 返回上一条命令运行的结果， 0表示运行成功，非0表示运行失败
0
[root@python]# echo $$  # 显示当前进程 PID,多用于脚本的检测和脚本运行状态的查看
1111
[root@python]# echo $0  # 显示当前进程的名称
-bash
# 示例
[root@A04-R08-I132-131-8WC4F22 tmp]# vim test.sh
[root@A04-R08-I132-131-8WC4F22 tmp]# cat test.sh 
    #!/bin/bash
    # PID Pname
    echo $$
    echo $0
[root@A04-R08-I132-131-8WC4F22 tmp]# chmod u+x test.sh 
[root@A04-R08-I132-131-8WC4F22 tmp]# bash test.sh 
21848
test.sh
[root@A04-R08-I132-131-8WC4F22 tmp]#

# 位置变量
[root@A04-R08-I132-131-8WC4F22 python]# vim 7.sh
    #!/bin/bash

    # $1 $2 ... $9 ${10}

    post1=$1
    post2=$2

    echo $post1
    echo $post2
[root@A04-R08-I132-131-8WC4F22 python]# chmod u+x 7.sh 
[root@A04-R08-I132-131-8WC4F22 python]# ./7.sh -l -a
-l
-a
# 如果传入的是个空值，就赋予一个默认值 _
    #!/bin/bash

    # $1 $2 ... $9 ${10}

    post1=$1
    post2=${2-_}  # 若传入值，则post2=$2，若不传入值，则post2=_

    echo $post1
    echo $post2
```

### 64 环境变量配置文件

**环境变量配置文件**

- 配置文件（四个文件，一个目录）
  - /etc/profile
  - /etc/profile.d/
  - ~/.bash_profile  # 保存用户特有配置
  - ~/.bashrc  # 保存用户特有配置
  - /etc/bashrc

```shell
# 环境变量配置文件：
# 注意：凡是保存在etc下的，是所有用户通用的文件。
/etc/profile
~/.bash_profile
~/.bashrc
/etc/bashrc

# 问题一：带 ~ 和不带 ~ 的区别：/etc/profile、/etc/bashrc、~/.bash_profile、~/.bashrc
# 不带 ~ 的配置文件，如/etc/profile、/etc/bashrc，是所有用户通用的环境变量配置文件，带 ~ 的配置文件是位于用户家目录下的配置文件，如~/.bash_profile、~/.bashrc，是各用户所特有的环境变量配置文件

# 问题二：我们发现，同一用户级别下的环境变量配置文件又分为 profile 和 bashrc 两种，为什么分为这两类呢？
# 因为我们在登录用户的时候，分为 login shell 和 nologin shell 两种，具体使用的命令，su - admin，这个就是login shell的登录方式，su admin，这个就是nologin shell的登录方式，login shell方式登录su - admin，这四个文件都会被执行，/etc/profile、~/.bash_profile、~/.bashrc、/etc/bashrc。nologin shell方式登录su admin，只会执行 ~/.bashrc、/etc/bashrc这两个配置文件。

# 问题三：这四个配置文件的加载先后顺序是怎样的？
# 案例：
vim /etc/profile
	echo "/etc/profile"
vim /etc/bashrc
	echo "/etc/bashrc"	
vim ~/.bash_profile
	echo ".bash_profile"
vim ~/.bashrc
	echo ".bashrc"	
[root@A01-R15-I104-75-300H0MK --prod-- users]# su - root
Last login: Mon Nov 30 16:41:31 CST 2020 on pts/0
/etc/profile
.bash_profile
.bashrc
/etc/bashrc
[root@A01-R15-I104-75-300H0MK --prod-- ~]# su root
.bashrc
/etc/bashrc
# 为什么要了解加载顺序呢？因为在实际使用中，如果两个配置文件中声明了同样的环境变量，后加载的会将先加载的覆盖掉。

# 手动加载环境变量配置文件
source /etc/profile
```

### 65 数组

- 定义数组
  - IPTS=( 10.0.0.1 10.0.0.2 10.0.0.3 )

- 显示数组的所有元素
  - echo ${IPTS[@]}
- 显示数组元素个数
  - echo ${#IPTS[@]}
- 显示数组的第一个元素
  - echo ${IPTS[0]}

### 66 转义和引用

特殊字符

- 特殊字符：一个字符不仅有字面意义，还有元意（meta-meaning）
  - `# 注释`
  - ; 分号
  - \ 转义符号
  - " 和 ' 引号

转义符号

- 单个字符前的转义符号
  - `\n \r \t` 单个字母的转义
  - `\$ \" \\`单个非字母的转义

引用

- 常用的引用符号
- "" 双引号
- ''  单引号
- ` 反引号

### 67 运算符

- 赋值运算符
  - = 赋值运算符，用于算数赋值和字符串赋值
  - 使用 unset 取消为变量的赋值
  - = 除了作为赋值运算符还可以作为测试操作符
- 算术运算符
  - 基本运算符
    - `+ - * / ** %`
  - 使用 expr 进行运算
    - expr 4 + 5
- 数字常量
  - 数字常量的使用方法
    - let "变量名=变量值"
    - 变量值使用 0 开头为八进制
    - 变量值使用 0x 开头为十六进制
- 双圆括号
  - (( a=10 ))
  - (( a++ ))
  - echo $(( 10+20 ))

### 68 特殊字符大全

引号

- '  完全引用
- "  不完全引用
- `  执行命令

括号

- ()  (())  $() 圆括号
  - 单独使用圆括号会产生一个子shell ( xyz=123 )
  - 数组初始化 IPS=( ip1 ip2 ip3 )
- [] [[]] 方括号
  - 单独使用方括号是测试（test）或数组元素功能
  - 两个方括号表示测试表达式
- <> 尖括号 重定向符号
- {} 花括号
  - 输出范围 echo {0..9}
  - 文件复制 cp /etc/passwd{,.bak}

运算和逻辑符号

-  `+ - * / %` 算数运算符
-  `> < = ` 比较运算符
-  && || ！  逻辑运算符

转义符号

- \ 转义某字符
  - \n 普通字符转义之后有不同的功能
  - \' 特殊字符转义之后，当做普通字符来使用

其他符号

- `# 注释符`
- `; 命令分隔符`
  - case 语句的分隔符要转义;;
- : 空指令
- . 和 source 命令相同
- ~ 家目录
- ，分隔目录
- `* 通配符`
- `? 条件测试 或 通配符`
- `$ 取值符号`
- `* 通配符`
- `? 条件测试 或 通配符`
- `$ 取值符号`
- `| 管道符`
- `& 后台运行`
- `_ 空格`

### 69 test 比较

#### 退出与退出状态

- 退出程序命令
  - exit 默认 exit 0，返回0正常退出
  - exit 10 返回10给Shell，返回值非 0 位不正常退出
  - $? 判断当前 Shell 前一个进程是否正常退出

#### 测试命令 test

- test命令用于检查文件或者比较值

- test可以做以下测试：

  - 文件测试
  - 整数比较测试
  - 字符串测试

- test测试语句可以简化为[]符号（推荐这种写法）

  ​	test EXPRESSION

  ​	[ EXPRESSION ]

- [] 符号还有扩展写法[[]]，支持 &&、||、<、>

#### 整数比较大小

```shell
# 使用[]比较整数大小
-eq  等于
-ne  不等于
-gt  大于
-ge  大于等于
-lt  小于
-le  小于等于
# 使用[[]]比较整数大小
[root@A04-R08-I132-131-8WC4F22 lizhe]# [[ 5 > 4 ]]
[root@A04-R08-I132-131-8WC4F22 lizhe]# echo $?
0
[root@A04-R08-I132-131-8WC4F22 lizhe]# [[ 5 < 4 ]]
[root@A04-R08-I132-131-8WC4F22 lizhe]# echo $?
1
[root@A04-R08-I132-131-8WC4F22 lizhe]# [[ 9 > 5 || 6 < 8 ]]
[root@A04-R08-I132-131-8WC4F22 lizhe]# echo $?
0
[root@A04-R08-I132-131-8WC4F22 lizhe]# [[ 9 > 5 && 6 > 8 ]]
[root@A04-R08-I132-131-8WC4F22 lizhe]# echo $?
1
```

#### 字符串比较

```shell
[root@A04-R08-I132-131-8WC4F22 lizhe]# [ "abc" = "abc" ]
[root@A04-R08-I132-131-8WC4F22 lizhe]# echo $?
0
[root@A04-R08-I132-131-8WC4F22 lizhe]# [ "abc" = "ABC" ]
[root@A04-R08-I132-131-8WC4F22 lizhe]# echo $?
1
```

### 70 if判断的使用

- if-then 语句的基本用法

  ```shell
  if [ 测试条件成立 ] 或 命令返回值是否为0
  then 执行相应命令
  fi 结束
  ```

  示例：

  ```shell
  # 判断当前用户是不是root用户
  ```

### 71 if-else判断的使用

使用 if-then-else 语句

- if-then-else 语句可以在条件不成立时也运行相应的命令

```shell
if [ 测试条件成立 ]
then 执行相应命令
else 测试条件不成立，执行相应命令
fi 结束
```

示例：

```shell
#!/bin/bash
# 判断当前用户是不是root用户
# if else demo

if [ $USER = root ];then
	echo " user root "
	echo $UID
else
	echo " other user "
	echo $UID
fi
```

- if-then-else 语句可以在条件不成立时也运行相应的命令

```shell
if [ 测试条件成立 ]
then 执行相应命令
elif [ 测试条件成立 ]
then 执行相应命令
else 测试条件不成立，执行相应命令
fi 结束
```

示例：

```shell
#!/bin/bash
# root user1 other
if [ $USER = root ]; then
	echo "root"
elif [ $USER = user1 ]; then
	echo "user1"
else
	echo "other user"
fi
```

### 72 嵌套if的使用

- if 条件测试中可以再嵌套 if 条件测试

```shell
if [ 测试条件成立 ]
then 执行相应命令
	if [ 测试条件成立 ]
	then 执行相应命令
	fi
fi
```

示例：

```shell
#!/bin/bash

# demo if then if then fi fi

if [ $UID = 0 ] ; then
	echo " please run "
	if [ -x /tmp/10.sh ] ; then
		/tmp/10.sh
	fi
else
	echo " switch user root "
fi
```

### 73 case分支

- case 语句和 select 语句可以构成分支

```shell
case "$变量" in
	"情况1")
		命令... ;;
	"情况2")
		命令... ;;
	*)
		命令... ;;
esac
```

示例：

```shell
#!/bin/bash

# case demo

case "$1" in
	"start"|"START")
		echo $0 start.....
	;;
	"stop")
		echo $0 stop.....
	;;
	"restart"|"reload")
		echo $0 restart...
	;;
	*)
		echo "Usage: $0 {start|stop|restart|reload}"
	;;
esac
```

### 74 for的基本使用

循环

- 使用 for 循环遍历命令的执行结果
- 使用 for 循环遍历变量和文件的内容
- C 语言风格的 for 命令
- while 循环
- 死循环
- until 循环
- break 和 continue 语句
- 使用循环对命令行参数的处理

**使用 for 循环遍历命令的执行结果**

- for 循环的语法

  for 参数 in 列表

  do 执行的命令

  done 封闭一个循环

- 使用反引号或 $() 方式执行命令，命令的结果当作列表进行处理

**使用 for 循环遍历变量和文本**

- 列表中包含多个变量，变量用空格分隔
- 对文本处理，要使用文本查看命令取出文本内容
  - 默认逐行处理，如果文本出现空格会当做多行处理

示例：修改文件后缀名

```shell
[root@A04-R08-I132-131-8WC4F22 tmp]# touch a.mp3 b.mp3 c.mp3
[root@A04-R08-I132-131-8WC4F22 tmp]# for filename in `ls *.mp3`
> do
>   mv $filename $(basename $filename .mp3).mp4
> done
[root@A04-R08-I132-131-8WC4F22 tmp]# ls *.mp3
ls: cannot access *.mp3: No such file or directory
[root@A04-R08-I132-131-8WC4F22 tmp]# ls *.mp4
a.mp4  b.mp4  c.mp4
```

### 75 c语言风格的 for

格式：

```shell
for ((变量初始化;循环判断条件;变量变化))
do
	循环执行的命令
done
```

示例：

```shell
[root@A04-R08-I132-131-8WC4F22 tmp]# for (( i=1; i<=10; i++  ))
> do
>     echo $i
> done
1
2
3
4
5
6
7
8
9
10
```

### 76 while循环和until循环

while test测试是否成立

do

​	命令

done

示例：

```shell
[root@A04-R08-I132-131-8WC4F22 tmp]# a=1
[root@A04-R08-I132-131-8WC4F22 tmp]# while [ $a -lt 10 ]
> do
>     ((a++))
>     echo $a
> done
2
3
4
5
6
7
8
9
10
```

死循环示例：

```shell
while :; do    echo "死循环"; done
```

until 循环（了解就行）

- until 循环与 while 循环相反，循环测试为假时，执行循环，为真时循环停止

### 77 循环的嵌套和break、continue语句

循环的使用

- 循环和循环可以嵌套
- 循环中可以嵌套判断，反过来也可以嵌套
- 循环可以使用 break 和 continue 语句在循环中退出

示例1：

```shell
for sc_name in /etc/profile.d/*.sh
do
    if [ -x $sc_name ];then
    	. $sc_name
    fi
done
```

示例2：

```shell
[root@A04-R08-I132-131-8WC4F22 tmp]# for num in {1..9}
> do
>     if [ $num -eq 5 ]; then
>         break
>     fi
>     echo $num
> done
1
2
3
4
```

示例3：

```shell
[root@A04-R08-I132-131-8WC4F22 tmp]# for num in {1..9}
> do
>     if [ $num -eq 5 ]; then
>         continue
>     fi
>     echo $num
> done
1
2
3
4
6
7
8
9
```

### 78 使用循环处理位置参数

使用循环处理命令行参数

- 命令行参数可以使用 $1 $2 ... ${10} ... $n 进行读取
- $0 代表脚本名称
- $* 和 $@ 代表所有位置参数
- $# 代表位置参数的数量

示例：

```shell
#!/bin/bash

# help display help help

#for pos in $*
#do 
#    if [ "$pos" = "help" ]; then
#        echo $pos $pos
#    fi
#done

while [ $# -ge 1 ]
do
    if [ "$1" = "help" ]; then
        echo $1 $1
    fi
    shift
done
```

### 79 自定义函数

- 函数用于 ”包含“ 重复使用的命令集合
- 自定义函数

```shell
function fname(){
   命令
}
```

- 函数的执行
  - fname

- 函数作用范围的变量
  - local 变量名
- 函数的参数
  - $1 $2 $3 ... $n

示例：

```shell
#!/bin/bash

# functions

checkpid() {
    local i
    
    for i in $* ; do
        [ -d "/proc/$i" ] && return 0
    done

    return 1
}
```

### 80 系统函数库介绍

系统脚本

- 系统自建了函数库，可以在脚本中引用
  - /etc/init.d/functions
- 自建函数库
  - 使用 source 函数脚本文件”导入“函数

示例：

```shell
[root@A04-R08-I132-131-8WC4F22 ~]vim /etc/init.d/functions
[root@A04-R08-I132-131-8WC4F22 ~]source /etc/init.d/functions
[root@A04-R08-I132-131-8WC4F22 ~]# echo_success
[root@A04-R08-I132-131-8WC4F22 ~]#                         [  OK  ]
```

### 81 脚本资源控制

脚本优先级控制

- 可以使用 nice 和 renice 调整脚本优先级
- 避免出现”不可控的“死循环
  - 死循环导致 cpu 占用过高
  - 死循环导致死机

ulimit -a

fork 炸弹

```shell
# func(){func|func&};func
.(){.|.&};.
```

### 82 信号

捕获信号

- 捕获信号脚本的编写
  - kill 默认会发送15号信号给应用程序
  - ctrl + c 发送2号信号给应用程序
  - 9号信号不可阻塞

示例：

```shell
#!/bin/bash

# signal demo

trap "echo sig 15"  15
trap "echo sig 2"  2

echo $$

while :
do
  :
done
```

### 83 一次性计划任务

- 计划任务：让计算机在指定的时间运行程序
- 计划任务分为：一次性计划任务、周期性计划任务
- 一次性计划任务
  - at

示例：

```shell
[root@A04-R08-I132-131-8WC4F22 ~]# date
Sat Aug  1 15:14:47 CST 2020
[root@A04-R08-I132-131-8WC4F22 ~]# at 15:16
at> echo hello > /tmp/hello.txt
at> <EOT>
job 1 at Sat Aug  1 15:16:00 2020
[root@A04-R08-I132-131-8WC4F22 ~]# atq
1	Sat Aug  1 15:16:00 2020 a root
[root@A04-R08-I132-131-8WC4F22 ~]# date
Sat Aug  1 15:16:02 CST 2020
[root@A04-R08-I132-131-8WC4F22 ~]# atq
[root@A04-R08-I132-131-8WC4F22 ~]# cat /tmp/hello.txt 
hello
```

### 84 周期性计划任务crontab

**周期性计划任务**

- cron
  - 配置方式
    - crontab -e
  - 查看现有的计划任务
    - crontab -l
  - 配置格式：
    - 分钟 小时 日期 月份 星期 执行的命令
    - 注意命令的路径问题

- crontab -e 编辑计划任务文件

- crontab -l 查看计划任务文件

- 计划任务文件所在位置：/var/spool/cron/    会生成一个和当前用户名同名的文件

- 计划任务执行日志：/var/log/cron

**延时计划任务（了解）**

**示例：**

```shell
# 每分钟获取一次系统时间，并将日志存到/tmp/date.txt中
[root@A04-R08-I132-131-8WC4F22 cron]# whoami
root
[root@A04-R08-I132-131-8WC4F22 cron]# crontab -e
[root@A04-R08-I132-131-8WC4F22 cron]# crontab -l
* * * * * /usr/bin/date >> /tmp/date.txt
# 查看周期性计划任务文件所在位置
[root@A04-R08-I132-131-8WC4F22 cron]# cat /var/spool/cron/root
* * * * * /usr/bin/date >> /tmp/date.txt
# 查看周期性计划任务执行日志
tail -f /var/log/cron
# 查看执行日志
[root@A04-R08-I132-131-8WC4F22 cron]# cat /tmp/date.txt
Sat Aug  1 15:38:01 CST 2020
Sat Aug  1 15:39:01 CST 2020
Sat Aug  1 15:40:01 CST 2020
```

### 85 为脚本加锁

执行备份脚本时，为了防止备份脚本多实例运行的情况，对备份脚本加锁。

示例：

```shell
vim a.sh
#!/bin/bash

# long time

sleep 10000
:wq  保存文件并退出

chmod u+x a.sh

flock -xn "/tmp/f.lock" -c "/root/a.sh"
```

## 第五章 文本操作篇

### 86 元字符介绍

**正则表达式与文本搜索**

- 元字符
- 扩展元字符
- 文件的查找命令 find
- 文本内容的过滤（查找）grep

**正则表达式的匹配方式**

- 字符串 Do one thing at a time, and do well.
- 匹配字符 an

**元字符**

- `.`匹配除换行符外的任意单个字符
- `*`匹配任意一个跟在它前面的字符
- `[]`匹配方括号中的字符类中的任意一个
- `^`匹配开头
- `$`匹配结尾
- `\`转义后面的特殊字符

**扩展元字符**

- `+` 匹配前面的正则表达式至少出现一次
- `?` 匹配前面的正则表达式出现零次或一次
- `|` 匹配它前面或后面的正则表达式

示例：

```shell
[root@A01-R15-I104-75-300H0MK --prod-- users]# grep password /root/anaconda-ks.cfg
[root@A01-R15-I104-75-300H0MK --prod-- users]# grep pass.... /root/anaconda-ks.cfg
[root@A01-R15-I104-75-300H0MK --prod-- users]# grep pass /root/anaconda-ks.cfg
[root@A01-R15-I104-75-300H0MK --prod-- users]# grep pass.* /root/anaconda-ks.cfg
[root@A01-R15-I104-75-300H0MK --prod-- users]# grep pass.... /root/anaconda-ks.cfg
[root@A01-R15-I104-75-300H0MK --prod-- users]# grep pass....$ /root/anaconda-ks.cfg
[root@A01-R15-I104-75-300H0MK --prod-- users]# grep pass.* /root/anaconda-ks.cfg
[root@A01-R15-I104-75-300H0MK --prod-- users]# grep [Hh]ello /root/anaconda-ks.cfg
[root@A01-R15-I104-75-300H0MK --prod-- users]# grep ^# /root/anaconda-ks.cfg
[root@A01-R15-I104-75-300H0MK --prod-- users]# grep "\." /root/anaconda-ks.cfg
```

### 87 find 演示

**文件查找命令**

- 文件查找命令 find
  - find 路径 查找条件 【 补充条件 】

```shell
[root@A01-R15-I104-75-300H0MK --prod-- users]# cd /etc/
[root@A01-R15-I104-75-300H0MK --prod-- etc]# find passwd
passwd
[root@A01-R15-I104-75-300H0MK --prod-- etc]# ls passwd*
passwd  passwd-  passwd.bak
[root@A01-R15-I104-75-300H0MK --prod-- etc]# find /etc -name passwd
/etc/passwd
/etc/pam.d/passwd
[root@A01-R15-I104-75-300H0MK --prod-- etc]# find /etc -name pass*
find: paths must precede expression: passwd-
Usage: find [-H] [-L] [-P] [-Olevel] [-D help|tree|search|stat|rates|opt|exec] [path...] [expression]
[root@A01-R15-I104-75-300H0MK --prod-- etc]# find /etc -regex .*wd
/etc/passwd
/etc/pam.d/passwd
/etc/security/opasswd
[root@A01-R15-I104-75-300H0MK --prod-- etc]# find /etc -regex .etc.*wd$
/etc/passwd
/etc/pam.d/passwd
/etc/security/opasswd
[root@A01-R15-I104-75-300H0MK --prod-- etc]# find /etc -name pass.*$
[root@A01-R15-I104-75-300H0MK --prod-- etc]# find /etc -type f -regex .*wd
/etc/passwd
/etc/pam.d/passwd
/etc/security/opasswd
[root@A01-R15-I104-75-300H0MK --prod-- etc]# find /etc -atime 8
[root@A01-R15-I104-75-300H0MK --prod-- etc]# find /etc -ctime 8

[root@A01-R15-I104-75-300H0MK --prod-- tmp]# touch /tmp/{1..9}.txt
[root@A01-R15-I104-75-300H0MK --prod-- tmp]# find *.txt
1.txt
2.txt
3.txt
4.txt
5.txt
6.txt
7.txt
8.txt
9.txt
[root@A01-R15-I104-75-300H0MK --prod-- tmp]# find *.txt -exec rm -v {} \;
removed ‘1.txt’
removed ‘2.txt’
removed ‘3.txt’
removed ‘4.txt’
removed ‘5.txt’
removed ‘6.txt’
removed ‘7.txt’
removed ‘8.txt’
removed ‘9.txt’

[root@A01-R15-I104-75-300H0MK --prod-- tmp]# grep pass /root/anaconda-ks.cfg 
# Root password
[root@A01-R15-I104-75-300H0MK --prod-- tmp]# grep pass /root/anaconda-ks.cfg | cut -d " " -f 1
#
[root@A01-R15-I104-75-300H0MK --prod-- tmp]# grep pass /root/anaconda-ks.cfg | cut -d " " -f 2
Root
[root@A01-R15-I104-75-300H0MK --prod-- tmp]# grep pass /root/anaconda-ks.cfg | cut -d " " -f 3
password

# uniq 会对相临的两行进行统计
[root@A01-R15-I104-75-300H0MK --prod-- tmp]# cut -d ":" -f7 /etc/passwd | uniq -c
      1 /bin/bash
      3 /sbin/nologin
      1 /bin/sync
      1 /sbin/shutdown
      1 /sbin/halt
     16 /sbin/nologin
      2 /bin/bash
[root@A01-R15-I104-75-300H0MK --prod-- tmp]# cut -d ":" -f7 /etc/passwd | sort | uniq -c
      3 /bin/bash
      1 /bin/sync
      1 /sbin/halt
     19 /sbin/nologin
      1 /sbin/shutdown
[root@A01-R15-I104-75-300H0MK --prod-- tmp]# cut -d ":" -f7 /etc/passwd | sort | uniq -c | sort -r
      3 /bin/bash
      1 /sbin/shutdown
      1 /sbin/halt
      1 /bin/sync
     19 /sbin/nologin
```

### 88 sed 和 awk介绍

**行编辑器介绍**

- vim 和 sed、awk 的区别
- sed 的基本用法演示
- awk 的基本用法演示

**vim 和 sed、awk的区别**

- 交互式与非交互式
- 文件操作模式与行操作模式

**sed 基本用法**

- sed 一般用于对文本内容做替换

  ```shell
  sed 's/user1/u1/' /etc/passwd
  ```

**awk 基本用法**

- awk 一般用于对文本内容进行统计、按需要的格式进行输出

  ```shell
  cut  命令： cut -d: -f 1 /etc/passwd
  awk  命令： awk -F: '/wd$/{print $1}' /etc/passwd
  ```

### 89 sed 替换命令讲解

**sed 的替换命令**

- sed 的模式空间
- 替换命令 s

**sed 的模式空间**

- sed 的基本工作方式是：
  - 将文件以行为单位读取到内存（模式空间）
  - 使用 sed 的每个脚本对该行进行操作
  - 处理完成后输出该行

**替换命令 s**

- sed 的替换命令 s：

  ```shell
  sed 's/old/new/' filename
  sed -e 's/old/new/' -e 's/old/new/' filename ...
  sed -i 's/old/new' 's/old/new/' filename ...
  ```

**使用正则表达式**

- 带正则表达式的替换命令 s：

  ```shell
  sed 's/正则表达式/new/' filename
  sed -r 's/扩展正则表达式/new/' filename
  ```

**示例：**

```shell

```

### 90 sed的替换指令加强版

**sed 的替换命令加强版**

- 全局替换
- 标志位
- 寻址
- 分组
- sed 脚本文件

**全局替换**

- s/old/new/g
  - g 为全局替换，用于替换所有出现的次数
  - / 如果和正则匹配的内容冲突可以使用其他符号，如：
    - s@old@new@g

**标志位**

- s/old/new/标志位

  - 数字，第几次出现才进行替换

  - g，每次出现都进行替换

  - p 打印模式空间的内容

    - ```shell
      sed -n 'script' filename 阻止默认输出
      ```

  - w file 将模式空间的内容写入到文件

**寻址**

- 默认对每行进行操作，增加寻址后对匹配的行进行操作
  - /正则表达式/s/old/new/g
  - 行号s/old/new/g
    - 行号可以是具体的行，也可以是最后一行 $ 符号
  - 可以使用两个寻址符号，也可以混合使用行号和正则地址

**分组**

- 寻址可以匹配多条命令
- /regular/{s/old/new/;s/old/new/}

**脚本文件**

- 可以将选项保存为文件，使用 -f 加载脚本文件
- sed -f sedscript filename

### 91 sed的其他常用命令

**sed 的其他命令**

- 删除命令

  - [ 寻址 ]d
    - 删除模式空间内容，改变脚本的控制流，读取新的输入行

  示例：

  ```shell
  
  ```

- 追加、插入、更改

  - 追加命令 a
  - 插入命令 i
  - 更改命令 c

  示例：

  ```shell
  
  ```

- 打印

  - 打印命令 p

  示例：

  ```shell
  
  ```

- 下一行

  - 下一行命令 n
  - 打印行号命令 =

  示例：

  ```shell
  
  ```

- 读文件和写文件

  - 读文件命令 r
  - 写文件命令 w

  示例：

  ```shell
  
  ```

- 退出命令

  - 退出命令 q
  - 哪个效率会更高呢？
    - sed 10q filename
    - sed -n 1,10p filename

  示例：

  ```shell
  
  ```

### 92 sed多行模式空间

**sed 的多行模式**

- 为什么要有多行模式
- 多行模式处理命令 N、D、P

**为什么要有多行模式**

- 配置文件一般为单行出现
- 也有使用 XML 或 JSON 格式的配置文件，为多行出现

**多行匹配命令**

- N 将下一行加入到模式空间
- D 删除模式空间中的第一个字符到第一个换行符
- P 打印模式空间中的第一个字符到第一个换行符

示例：

```shell

```

### 93 什么是sed的保持空间

**sed 的保持空间**

- 什么是保持空间
  - 保持空间也是多行的一种操作方式
  - 将内容暂存在保持空间，便于做多行处理
- 保持空间命令
  - h 和 H 将模式空间内容存放到保持空间
  - g 和 G 将保持空间内容取出到模式空间
  - x 交换模式空间和保持空间内容

示例：

```shell

```

### 94 认识awk

**awk 和 sed 的区别**

- awk 更像是脚本语言
- awk 用于“比较规范”的文本处理，用于统计数量并输出指定字段
- 使用 sed 将不规范的文本，处理为“比较规范”的文本

**awk 脚本的流程控制**

- 输入数据前例程 BEGIN{}
- 主输入循环{}
- 所有文件读取完成例程 END{}

### 95 awk的字段

**记录和字段**

- 每行称作 awk 的记录
- 使用空格、制表符分隔开的的单词称作字段
- 可以自己指定分隔的字段

**字段的引用**

- awk 中使用 $1 $2 ... $n 表示每一个字段
  - awk '{ print $1,$2,$3 }' filename
- awk 可以使用 -F 选项改变字段分隔符
  - awk -F ',' '{ print $1,$2,$3 }' filename
  - 分隔符可以使用正则表达式

示例：

```shell

```

### 96 awk表达式

**awk 的表达式**

- 赋值操作符
  - =  是最常用的赋值操作符
    - var1 = "name"
    - var2 = "hello"  "world"
    - var3 = $1
  - 其他赋值操作符
    - `++  --  +=  -=  *=  /=  %=  ^=`

- 算数操作符
  - `+ - * / % ^`

- 系统变量
  - FS 和 OFS 字段分隔符，OFS 表示输出的字段分隔符
  - RS 记录分隔符
  - NR 和 FNR 行数
  - NF 字段数量，最后一个字段内容可以用 $NF 取出

- 关系操作符
  - `<  >  <=  >=  ==  !=  ~  !~`
- 布尔操作符
  - `<  >  <=  >=  ==  !=  ~  !~`

### 97 awk判断和循环

**条件语句**

- 条件语句使用 if 开头，根据表达式的结果来判断执行哪条语句

```shell
if (表达式)
	awk语句1
[ else
	awk语句2
]  
```

- 如果有多个语句需要执行可以使用 { } 将多个语句括起来 

**循环**

- while 循环

  while( 表达式 )

  ​	awk 语句1

- do 循环

  do{

  ​	awk 语句1

  }while( 表达式 )

- for 循环

  for( 初始值；循环判断条件；累加 )

  ​	awk 语句1

- 影响控制的其他语句

  - break
  - continue

示例：

```shell

```

### 98 awk数组

**awk 的数组**

- 数组的定义
  - 数组：一组有某种关联的数据（变量），通过下标依次访问
    - 数组名[ 下标 ] = 值
    - 下标可以使用数字也可以使用字符串
- 数组的遍历
  - for(变量 in 数组名)
    - 使用 数组名[ 变量 ] 的方式依次对每个数组的元素进行操作
- 删除数组
  - 删除数组
    - delete 数组[ 下标 ]
- 命令行参数数组
  - 命令行参数数组
    - ARGC
    - ARGV

示例：

```shell

```

### 99 awk数组功能的使用

示例：

```shell

```

### 100 awk函数

**awk 的函数**

- 算数函数

  - sin()  cos()
  - int()
  - rand()  srand()

- 字符串函数

  - gsub( r, s, t )
  - index( s, t )
  - length( s )
  - match( s, r )
  - split( s, a, sep )
  - sub( r, s, t )
  - substr( s, p, n )

- 自定义函数

  function 函数名 ( 参数 ) {

  ​	awk语句

  ​	return awk变量

  }

## 第六章 服务管理篇

### 101 防火墙概述

- 防火墙分类
  - 软件防火墙和硬件防火墙
  - 包过滤防火墙和应用层防火墙
    - CentOS 6 默认的防火墙是 iptables
    - CentOS 7 默认的防火墙是 firewallD（底层使用 netfilter）

- iptables 的表和链
  - 规则表
    - filter nat mangle raw
  - 规则链
    - INPUT OUTPUT FORWARD
    - PREROUTING POSTROUTING

### 102 iptables规则的基本使用演示

**iptables 的 filter 表**

- iptables -t filter 命令 规则链 规则
  - 命令
    - -L
    - -A -l
    - -D -F -P
    - -N -X -E
  - 规则
    - -p
    - -s -d
    - -i -o
    - -j

### 103 iptables过滤规则的使用

**示例：**

```shell

```

### 104 iptables nat表的使用

**iptables 的 nat 表**

- iptables -t nat 命令 规则链 规则
  - PREROUTING 目的地址转换
  - POSTROUTING 源地址转换

**iptables 配置文件**

- /etc/sysconfig/iptables
- CentOS6
  - `service iptables save | start | stop | restart`
- CentOS7
  - `yum install iptables-services`

**示例：**

```shell

```

### 105 firewalld

**firewallD 服务**（Centos7中默认防火墙）

- firewallD 的特点
  - 支持区域 “zone” 概念
  - firewall-cmd
- systemctl start | stop | enable | disable firewalld.service

**示例：**

```shell

```

### 106 SSH介绍之Telnet明文漏洞

**SSH 服务**

- SSH 服务介绍

  - 远程管理的必要性
  - telnet 服务的问题

  ```shell
  yum install telnet telnet-server xinetd -y
  ```

- SSH 服务配置文件

- SSH 命令

- SSH 公钥认证

- scp 和 sftp 远程拷贝文件

### 107 SSH服务演示

**SSH 服务配置文件**

- sshd_config
  - /etc/ssh/sshd_config
  - port 22  默认端口
  - PermitRootLogin yes 是否允许 root 登陆
  - AuthorizedKeysFile  .ssh/authorized_keys

**SSH 命令**

- systemctl status | start | stop | restart | enable | disable sshd.service
- 客户端命令
  - ssh [ -p 端口 ] 用户@远程ip
  - SecureCRT
  - Xshell
  - putty

**SSH 公钥认证**

- 密钥认证原理
- 常用命令
  - ssh-keygen -t rsa
  - ssh-copy-id

### 108 FTP服务器vsftpd介绍与软件包安装

**FTP 服务**

- FTP 协议介绍
- vsftpd 服务器安装
- vsftpd 服务配置文件
- FTP 命令
- 使用虚拟用户进行验证

**FTP 服务介绍**

- FTP 协议
  - 主动模式和被动模式

**vsftpd 服务安装和启动**

- yum install vsftpd ftp
- systemctl start vsftpd.service
- 建议将 selinux 改为 permissive
  - getsebool -a | grep ftpd
  - setsebool -P <sebool> l

### 109 vsftpd配置文件介绍

**vsftpd 服务配置文件**

- /etc/vsftpd/vsftp.conf
- /etc/vsftpd/ftpusers
- /etc/vsftpd/user_list

### 110 vsftp 虚拟用户

**使用虚拟用户进行验证**

- guest_enable=YES
- guest_username=vuser
- user_config_dir=/etc/vsftpd/vuserconfig
- allow_writeable_chroot=YES
- pam_service_name=vsftpd.vuser

### 111 samba 服务演示

### 112 NFS 服务

### 113 Nginx 基本配置文件

### 114 使用Nginx配置域名虚拟主机

### 115 LNMP环境搭建

### 116 DNS服务的原理

### 117 NAS 演示

### 118 结果测试&结束语

