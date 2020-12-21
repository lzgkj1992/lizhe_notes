# linux环境下安装javaJDK

## 方法一：yum在线安装

```shell
# 检查一下是否有java安装
java -version

# 卸载已经安装的jdk
yum remove java-1.8.0*

# 查看可以通过yum安装的jdk版本
yum list java-1.*

# 安装1.8.0版本
yum install java-1.8.0-openjdk.x86_64 -y

# 查看是否安装成功
[root@A01-R06-I29-98-7C8BT92 --prod-- jre]# java -version
Error occurred during initialization of VM
java.lang.Error: Properties init: Could not determine current working directory.
	at java.lang.System.initProperties(Native Method)
	at java.lang.System.initializeSystemClass(System.java:1166)
# 发现有问题

[root@A01-R06-I29-98-7C8BT92 --prod-- jre]# echo $JAVA_HOME
/export/work/jdk
# 发现JAVA_HOME的环境变量有问题，不是我们想要的，这个路径下并没有jdk
# 找到jdk的安装目录
[root@A01-R06-I29-98-7C8BT92 --prod-- jre]# whereis java
java: /usr/bin/java /usr/lib/java /etc/java /usr/share/java /usr/share/man/man1/java.1.gz
[root@A01-R06-I29-98-7C8BT92 --prod-- jre]# ll /usr/bin/java
lrwxrwxrwx 1 root root 22 Jul 22 17:03 /usr/bin/java -> /etc/alternatives/java
[root@A01-R06-I29-98-7C8BT92 --prod-- jre]# ll /etc/alternatives/java
lrwxrwxrwx 1 root root 72 Jul 22 17:03 /etc/alternatives/java -> /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.71-2.b15.el7_2.x86_64/jre/bin/java

# 下面这个路径才是我们的安装目录
/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.71-2.b15.el7_2.x86_64/jre/bin/java  

# 上面那个环境变量没有找到配置位置，但是我们可以将上面的环境变量覆盖掉
su - elasticsearch   # 切换到elasticsearch用户
vim ~/.bashrc
# 添加如下环境变量配置
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.71-2.b15.el7_2.x86_64/jre
export PATH=$PATH:$JAVA_HOME/bin

# 注意：修改完成后，要source ~/.bashrc 才会立即生效
sourc ~/.bashrc

# 查看当前JAVA_HOME环境变量
[elasticsearch@A01-R06-I29-98-7C8BT92 --prod-- ~]$ echo $JAVA_HOME
/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.71-2.b15.el7_2.x86_64/jre

# 至此，使用yum方式安装JDK，成功！
```

## 方法二：使用安装包安装

到官方网站下载JDK安装包：https://www.oracle.com/java/technologies/javase-downloads.html

我个人习惯到kaige123.com网站下载：http://kaige123.com

```shell
wget  --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie"  http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz

# 下载好安装包后
[root@A01-R06-I29-40-J8PKD92 java]# cd /usr/java
[root@A01-R06-I29-40-J8PKD92 java]# ll
total 8
-rw-r--r-- 1 root root 5307 Jul 22 18:22 jdk-8u131-linux-x64.tar.gz

# 解压
tar -zxvf jdk-8u131-linux-x64.tar.gz

[root@A01-R06-I29-40-J8PKD92 java]# ll
total 181196
drwxr-xr-x 8   10  143      4096 Mar 15  2017 jdk1.8.0_131
-rw-r--r-- 1 root root 185540433 Mar 16  2017 jdk-8u131-linux-x64.tar.gz

[root@A01-R06-I29-40-J8PKD92 jdk1.8.0_131]# ll
total 25872
drwxr-xr-x 2 10 143     4096 Mar 15  2017 bin
-r--r--r-- 1 10 143     3244 Mar 15  2017 COPYRIGHT
drwxr-xr-x 4 10 143      115 Mar 15  2017 db
drwxr-xr-x 3 10 143      125 Mar 15  2017 include
-rwxr-xr-x 1 10 143  5097105 Mar 15  2017 javafx-src.zip
drwxr-xr-x 5 10 143     4096 Mar 15  2017 jre
drwxr-xr-x 5 10 143     4096 Mar 15  2017 lib
-r--r--r-- 1 10 143       40 Mar 15  2017 LICENSE
drwxr-xr-x 4 10 143       44 Mar 15  2017 man
-r--r--r-- 1 10 143      159 Mar 15  2017 README.html
-rw-r--r-- 1 10 143      526 Mar 15  2017 release
-rw-r--r-- 1 10 143 21115141 Mar 15  2017 src.zip
-rwxr-xr-x 1 10 143    63933 Mar 15  2017 THIRDPARTYLICENSEREADME-JAVAFX.txt
-r--r--r-- 1 10 143   177094 Mar 15  2017 THIRDPARTYLICENSEREADME.txt

# 配置环境变量
vim /etc/profile

export JAVA_HOME=/usr/java/jdk1.8.0_131
export PATH=$PATH:$JAVA_HOME/bin

# 使修改后的配置文件生效
[root@A01-R06-I29-40-J8PKD92 jdk1.8.0_131]# source /etc/profile
[root@A01-R06-I29-40-J8PKD92 jdk1.8.0_131]# echo $JAVA_HOME
/usr/java/jdk1.8.0_131

# 验证jdk是否安装成功
[root@A01-R06-I29-40-J8PKD92 jdk1.8.0_131]# java -version
java version "1.8.0_131"
Java(TM) SE Runtime Environment (build 1.8.0_131-b11)
Java HotSpot(TM) 64-Bit Server VM (build 25.131-b11, mixed mode)
```

