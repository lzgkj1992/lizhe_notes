# python知识总结

## linux环境下安装python3和pip3

Centos 7.X版本自带python2.7.5开发环境

![1567242165597](C:\Users\lizhe427\AppData\Roaming\Typora\typora-user-images\1567242165597.png)

**如何在linux环境下安装python3呢？**

视频教程链接：https://www.bilibili.com/video/av49267728?from=search&seid=915343169020784258

```shell
[root@A01-R06-I178-162-5001727 tmp][DBA]# python3 --version
-bash: python3: command not found
```

这台机器上没有安装python3，进行安装：

首先创建一个文件夹用来下载python3

进入tmp文件夹，下载安装包。

官网：[www.python.org](http://www.python.org)

点击Download。

复制链接地址：

```shell
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
tar -zxvf Python-3.7.4.tgz
cd Python-3.7.4
```

编译一下，目录是可以选择的：

```shell
./configure --prefix=/usr/local/python3    
```

如果这里报错的话，需要安装gcc和g++

```shell
yum install gcc
yum install g++
```

编译成功（提示如下）:

执行make命令。

然后执行make install命令。

编译完成后，退回上一级目录：

要想在任意地方都可以执行python3命令，需要创建软连接。

```shell
# ln -s 源路径 目标路径
cd /usr/local/python3/bin
ln -s /usr/local/python3/bin/python3 /bin/python3

# 验证
[root@A01-R06-I178-162-5001727 bin][DBA]# python3 --version
Python 3.7.4
```

这样python3就安装好了！

Python3安装好后，一般自带pip3(也有的不带)

可以查看一下：

```shell
[root@A01-R06-I178-162-5001727 python3][DBA]# cd bin/
[root@A01-R06-I178-162-5001727 bin][DBA]# ll
total 27332
lrwxrwxrwx 1 root root        8 Sep 19 18:10 2to3 -> 2to3-3.7
-rwxr-xr-x 1 root root      109 Sep 19 18:10 2to3-3.7
lrwxrwxrwx 1 root root        7 Sep 19 18:10 idle3 -> idle3.7
-rwxr-xr-x 1 root root      107 Sep 19 18:10 idle3.7
lrwxrwxrwx 1 root root        8 Sep 19 18:10 pydoc3 -> pydoc3.7
-rwxr-xr-x 1 root root       92 Sep 19 18:10 pydoc3.7
lrwxrwxrwx 1 root root        9 Sep 19 18:10 python3 -> python3.7
-rwxr-xr-x 2 root root 13982889 Sep 19 18:09 python3.7
lrwxrwxrwx 1 root root       17 Sep 19 18:10 python3.7-config -> python3.7m-config
-rwxr-xr-x 2 root root 13982889 Sep 19 18:09 python3.7m
-rwxr-xr-x 1 root root     2910 Sep 19 18:10 python3.7m-config
lrwxrwxrwx 1 root root       16 Sep 19 18:10 python3-config -> python3.7-config
lrwxrwxrwx 1 root root       10 Sep 19 18:10 pyvenv -> pyvenv-3.7
-rwxr-xr-x 1 root root      449 Sep 19 18:10 pyvenv-3.7
```

可以看到，这个版本的python3是不带pip3的，建议选择一个带pip3的版本，如3.6.6版本，因为方便。

创建一个软连接：

```shell
ln -s /usr/local/python3/bin/pip3 /bin/pip3
```

## linux环境下安装ipython

Ipython是一个python的交互式shell，比默认的`python shell`好用的多

版本：

- python 2.x使用的解释器式ipython
- python 3.x使用的解释器式ipython3
- 要退出解释器可以有以下两种方式：
  1. 直接输入exit
  2. 使用热键ctrl+d退出解释器，`Ipython`会询问是否退出解释器

安装：

```
sudo apt install ipython
sudo apt install ipython3
```

## windows环境下安装python3

1. 进入官网：https://www.python.org/downloads/

2. 选择安装环境，下载安装包

   ![1567240880889](C:\Users\lizhe427\AppData\Roaming\Typora\typora-user-images\1567240880889.png)

点击，进去。选择window环境下的64位版本，并下载。

![1567241006970](C:\Users\lizhe427\AppData\Roaming\Typora\typora-user-images\1567241006970.png)

双击可执行文件，进行安装。

![1567241208834](C:\Users\lizhe427\AppData\Roaming\Typora\typora-user-images\1567241208834.png)

**1.若选择Install Now，会将python3默认安装在c盘；若选择Customize installation，可以自定义安装目录。文件并不大，可以选择默认安装路径(方便)。**

![1567241560501](C:\Users\lizhe427\AppData\Roaming\Typora\typora-user-images\1567241560501.png)

Install launcher for all users(recommended)：该计算机下的所有用户都可以使用

Add Python 3.7 to PATH：配置环境变量

**2.Installing...**

![1567241610259](C:\Users\lizhe427\AppData\Roaming\Typora\typora-user-images\1567241610259.png)

**3.安装成功，close...**

![1567241691086](C:\Users\lizhe427\AppData\Roaming\Typora\typora-user-images\1567241691086.png)



**4.验证**

![1567241774188](C:\Users\lizhe427\AppData\Roaming\Typora\typora-user-images\1567241774188.png)

## windows环境下安装pycharm

**注意：**要先安装python3，不然pycharm没法运行

卖家阿里旺旺账号：星空网游竞技

群号：jetbrains初学

网站实时获取激活码（因激活码太长，请务必用电脑打开网址）

 http://www.100c1.com/portal/page/index/id/2.html 

打开网址，输入订单号，获取激活码。订单编号:517650241805679753

凭订单号  终身享受获取激活资格

网站激活码下方有下载，安装，汉化，教程的链接

\---------------------------------------------------------------------

\---------------------------------------------------------------------

（如果您以前破解过或者安装过盗版，会导致激活不成功，请看这里解决

 http://www.100c1.com/portal/article/index/id/30.html ）

记得再来哦~

**Pycharm 激活码** 

```
T3ACKYHDVF-eyJsaWNlbnNlSWQiOiJUM0FDS1lIRFZGIiwibGljZW5zZWVOYW1lIjoi5bCP6bifIOeoi+W6j+WRmCIsImFzc2lnbmVlTmFtZSI6IiIsImFzc2lnbmVlRW1haWwiOiIiLCJsaWNlbnNlUmVzdHJpY3Rpb24iOiIiLCJjaGVja0NvbmN1cnJlbnRVc2UiOmZhbHNlLCJwcm9kdWN0cyI6W3siY29kZSI6IklJIiwiZmFsbGJhY2tEYXRlIjoiMjAxOS0wNi0xMyIsInBhaWRVcFRvIjoiMjAyMC0wNi0xMiJ9LHsiY29kZSI6IkFDIiwiZmFsbGJhY2tEYXRlIjoiMjAxOS0wNi0xMyIsInBhaWRVcFRvIjoiMjAyMC0wNi0xMiJ9LHsiY29kZSI6IkRQTiIsImZhbGxiYWNrRGF0ZSI6IjIwMTktMDYtMTMiLCJwYWlkVXBUbyI6IjIwMjAtMDYtMTIifSx7ImNvZGUiOiJQUyIsImZhbGxiYWNrRGF0ZSI6IjIwMTktMDYtMTMiLCJwYWlkVXBUbyI6IjIwMjAtMDYtMTIifSx7ImNvZGUiOiJHTyIsImZhbGxiYWNrRGF0ZSI6IjIwMTktMDYtMTMiLCJwYWlkVXBUbyI6IjIwMjAtMDYtMTIifSx7ImNvZGUiOiJETSIsImZhbGxiYWNrRGF0ZSI6IjIwMTktMDYtMTMiLCJwYWlkVXBUbyI6IjIwMjAtMDYtMTIifSx7ImNvZGUiOiJDTCIsImZhbGxiYWNrRGF0ZSI6IjIwMTktMDYtMTMiLCJwYWlkVXBUbyI6IjIwMjAtMDYtMTIifSx7ImNvZGUiOiJSUzAiLCJmYWxsYmFja0RhdGUiOiIyMDE5LTA2LTEzIiwicGFpZFVwVG8iOiIyMDIwLTA2LTEyIn0seyJjb2RlIjoiUkMiLCJmYWxsYmFja0RhdGUiOiIyMDE5LTA2LTEzIiwicGFpZFVwVG8iOiIyMDIwLTA2LTEyIn0seyJjb2RlIjoiUkQiLCJmYWxsYmFja0RhdGUiOiIyMDE5LTA2LTEzIiwicGFpZFVwVG8iOiIyMDIwLTA2LTEyIn0seyJjb2RlIjoiUEMiLCJmYWxsYmFja0RhdGUiOiIyMDE5LTA2LTEzIiwicGFpZFVwVG8iOiIyMDIwLTA2LTEyIn0seyJjb2RlIjoiUk0iLCJmYWxsYmFja0RhdGUiOiIyMDE5LTA2LTEzIiwicGFpZFVwVG8iOiIyMDIwLTA2LTEyIn0seyJjb2RlIjoiV1MiLCJmYWxsYmFja0RhdGUiOiIyMDE5LTA2LTEzIiwicGFpZFVwVG8iOiIyMDIwLTA2LTEyIn0seyJjb2RlIjoiREIiLCJmYWxsYmFja0RhdGUiOiIyMDE5LTA2LTEzIiwicGFpZFVwVG8iOiIyMDIwLTA2LTEyIn0seyJjb2RlIjoiREMiLCJmYWxsYmFja0RhdGUiOiIyMDE5LTA2LTEzIiwicGFpZFVwVG8iOiIyMDIwLTA2LTEyIn0seyJjb2RlIjoiUlNVIiwiZmFsbGJhY2tEYXRlIjoiMjAxOS0wNi0xMyIsInBhaWRVcFRvIjoiMjAyMC0wNi0xMiJ9XSwiaGFzaCI6IjEzMzgwMDA0LzAiLCJncmFjZVBlcmlvZERheXMiOjcsImF1dG9Qcm9sb25nYXRlZCI6ZmFsc2UsImlzQXV0b1Byb2xvbmdhdGVkIjpmYWxzZX0=-nTBuZDiAOuM4IHXNkS7GbCvZVZFo4EcHf9hHzfhaPYsaCGQjuCVJFEboopbPuEHn16yT9Zvf7yRuM5WGlGmpcOJnWLpCmGm65S6wHtZdX0kfSNIqnqdS1MhIHpftsAGxSswuQksrm09tltbO4nATeavGs1BIMafsCJVen+BvDFvYL7+3crkRI7AwdyMb2miLLYJcEVPhiVKZnzJUzT9uA8/4Q02BqsvX5oSJg8cLw3w7Cd0ISrn1i8uENe/1z3T/Ede0STM7eOekFaVEdO9cgzYME3iIFzi2TZXMSqIuBpJqF4NFb6M0039tEGy6EHqcksMyDTdCAASquqcDcHrUUA==-MIIElTCCAn2gAwIBAgIBCTANBgkqhkiG9w0BAQsFADAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBMB4XDTE4MTEwMTEyMjk0NloXDTIwMTEwMjEyMjk0NlowaDELMAkGA1UEBhMCQ1oxDjAMBgNVBAgMBU51c2xlMQ8wDQYDVQQHDAZQcmFndWUxGTAXBgNVBAoMEEpldEJyYWlucyBzLnIuby4xHTAbBgNVBAMMFHByb2QzeS1mcm9tLTIwMTgxMTAxMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxcQkq+zdxlR2mmRYBPzGbUNdMN6OaXiXzxIWtMEkrJMO/5oUfQJbLLuMSMK0QHFmaI37WShyxZcfRCidwXjot4zmNBKnlyHodDij/78TmVqFl8nOeD5+07B8VEaIu7c3E1N+e1doC6wht4I4+IEmtsPAdoaj5WCQVQbrI8KeT8M9VcBIWX7fD0fhexfg3ZRt0xqwMcXGNp3DdJHiO0rCdU+Itv7EmtnSVq9jBG1usMSFvMowR25mju2JcPFp1+I4ZI+FqgR8gyG8oiNDyNEoAbsR3lOpI7grUYSvkB/xVy/VoklPCK2h0f0GJxFjnye8NT1PAywoyl7RmiAVRE/EKwIDAQABo4GZMIGWMAkGA1UdEwQCMAAwHQYDVR0OBBYEFGEpG9oZGcfLMGNBkY7SgHiMGgTcMEgGA1UdIwRBMD+AFKOetkhnQhI2Qb1t4Lm0oFKLl/GzoRykGjAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBggkA0myxg7KDeeEwEwYDVR0lBAwwCgYIKwYBBQUHAwEwCwYDVR0PBAQDAgWgMA0GCSqGSIb3DQEBCwUAA4ICAQAF8uc+YJOHHwOFcPzmbjcxNDuGoOUIP+2h1R75Lecswb7ru2LWWSUMtXVKQzChLNPn/72W0k+oI056tgiwuG7M49LXp4zQVlQnFmWU1wwGvVhq5R63Rpjx1zjGUhcXgayu7+9zMUW596Lbomsg8qVve6euqsrFicYkIIuUu4zYPndJwfe0YkS5nY72SHnNdbPhEnN8wcB2Kz+OIG0lih3yz5EqFhld03bGp222ZQCIghCTVL6QBNadGsiN/lWLl4JdR3lJkZzlpFdiHijoVRdWeSWqM4y0t23c92HXKrgppoSV18XMxrWVdoSM3nuMHwxGhFyde05OdDtLpCv+jlWf5REAHHA201pAU6bJSZINyHDUTB+Beo28rRXSwSh3OUIvYwKNVeoBY+KwOJ7WnuTCUq1meE6GkKc4D/cXmgpOyW/1SmBz3XjVIi/zprZ0zf3qH5mkphtg6ksjKgKjmx1cXfZAAX6wcDBNaCL+Ortep1Dh8xDUbqbBVNBL4jbiL3i3xsfNiyJgaZ5sX7i8tmStEpLbPwvHcByuf59qJhV/bZOl8KqJBETCDJcY6O2aqhTUy+9x93ThKs1GKrRPePrWPluud7ttlgtRveit/pcBrnQcXOl1rHq7ByB8CFAxNotRUYL9IF5n3wJOgkPojMy6jetQA5Ogc8Sm7RG6vg1yow==
```

**Pycharm官方典范使用教程：**https://www.bilibili.com/video/av22939579?from=search&seid=2752703597368870175

## pip安装第三方模块

拷贝文件。。。



## Pycharm常用快捷键

```python
ctrl d  #复制一行
ctrl y  #删除一行
ctrl /  #添加注释
ctrl f  #查找

```



