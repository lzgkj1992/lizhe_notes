# 极客时间shell篇

## 什么是shell

- Shell 是命令解释器，用于解释用户对操作系统的操作

```
	一句话来概括Shell，Shell会将用户执行的命令翻译给内核，然后内核根据命令执行的结果反馈给用户。
	那具体流程是怎样的？例如：用Shell解释ls命令，当输入ls回车的时候，首先由Shell接收到用户执行的命令，接收完后对命令的选项和参数进行分析，分析之后知道ls是查看文件的，分析之后会交给文件系统，文件系统在内核层，文家系统将ls要查看的文件和目录翻译成对应硬盘的扇区，当然ssd硬盘是另外的一种结构，硬件会将查询到的结果交给内核，内核返回给Shell，最终再返回给用户。我们可以发现，将Shell写好的话，用户是不需要写底层驱动程序的，也不需要开发复杂的c语言，通过简单的命令就可以控制内核和操作系统，做很多自己想做的事情。
	这就是Shell解释器最主要的功能，用户不需要去了解底层的知识。
```

- Shell 有很多
  - cat /etc/shells
- CentOS 7 默认使用的 Shell 是 bash

## Linux的启动过程

- BIOS-MBR-BootLoader(grub) - kernel - systemd - 系统初始化 - shell

待补充！

## Shell脚本的格式

- UNIX 的哲学：一条命令只做一件事
- 为了组合命令和多次执行，使用脚本文件来保存需要执行的命令
- 赋予该文件执行权限（chmod u+rx filename）

**标准的Shell脚本要包含哪些元素**

- Sha-Bang     shell脚本第一行    #!/bin/bash

如果使用bash 启动脚本，那么这一行就是注释；如果使用./启动脚本，那这一行就是告诉系统要用bash解释器

- 命令
- “#” 号开头的注释
- chmod u+rx filename 可执行权限
- 执行命令
  - bash ./filename.sh
  - ./filename.sh   # 需要有可执行权限   chomd u+x filename.sh
  - source ./filename.sh
  - . ./filename.sh   #  等同于source ./filename.sh

**示例：**

vim 1.sh

```shell
#!/bin/bash
# demo
cd /var/
ls
pwd
du -sh
du -sh *
```

chomd u+x 1.sh

bash 1.sh

## 脚本不同执行方式的影响

执行脚本时，bash命令和./命令不会对当前环境造成影响，而sourc命令会对当前环境造成影响。

待补充！

## 管道与重定向

### 管道与管道符

- 管道和信号一样，也是进程通信的方式之一
- 匿名管道（管道符）是 Shell 编程经常用到的通信工具
- 管道符是 “|”，将前一个命令执行的结果传递给后面的命令
  - ps | cat
  - echo 123 | ps

### 重定向

- 一个进程默认会打开标准输入、标准输出、错误输出三个文件描述符
- 输入重定向符号  “<”
  - read var < /path/to/a/file
- 输出重定向符号  “>”  ">>"  "2>"  "&>"
  - echo 123 > /path/to/a/file
- 输入和输出重定向组合使用
  - cat > /path/to/a/file << EOF
  - I am $USER
  - EOF

示例：

```shell
#!/bin/bash

cat > /root/a.sh <<EOF
echo "hello bash"
EOF
```

## 变量赋值

变量的定义

- 变量名的命名规则
  - 字母、数字、下划线
  - 不以数字开头

变量的赋值

- 为变量赋值的过程，称为变量替换
  - 变量名=变量值
    - a=123
  - 使用let为变量赋值
    - let a=10+20
  - 将命令赋值给变量
    - l=ls
  - 将命令结果赋值给变量，使用$()或者反引号``
    - letc=$(ls -l /etc)
  - 变量值有空格等特殊字符可以包含在双引号“ ”或单引号‘ ’中

## 变量引用及作用范围

- 变量的引用
  - ${变量名} 称作对变量的引用
  - echo ${变量名} 查看变量的值
  - ${变量名} 在部分情况下可以省略为 $变量名
- 变量的作用范围
- 变量的导出
  - export
- 变量的删除
  - unset

## 环境变量、预定义变量与位置变量

- 环境变量：每个Shell打开都可以获得到的变量
  - set和 env命令
  - $? $$ $0
    - $PATH
    - $PS1
- 位置变量
  - $1 $2 ... ${10}... $n

## 环境变量配置文件

待补充！

## 数组

- 定义数组
  - IPTS=( 10.0.0.1 10.0.0.2 10.0.0.3 )

- 显示数组的所有元素
  - echo ${IPTS[@]}
- 显示数组元素个数
  - echo ${#IPTS[@]}
- 显示数组的第一个元素
  - echo ${IPTS[0]}

## 转义和引用

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

## 运算符

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

## 特殊字符大全

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
- `> < = ` 比较运算符
- && || ！  逻辑运算符

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

## test 比较

**退出与退出状态**

- 退出程序命令
  - exit
  - exit 10 返回10给Shell，返回值非 0 位不正常退出
  - $? 判断当前 Shell 前一个进程是否正常退出

**测试命令 test**

- test命令用于检查文件或者比较值

- test可以做以下测试：

  - 文件测试
  - 整数比较测试
  - 字符串测试

- test测试语句可以简化为[]符号（推荐这种写法）

  ​	test EXPRESSION

  ​	[ EXPRESSION ]

- [] 符号还有扩展写法[[]]，支持 &&、||、<、>

整数比较大小：

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

字符串比较：

```shell
[root@A04-R08-I132-131-8WC4F22 lizhe]# [ "abc" = "abc" ]
[root@A04-R08-I132-131-8WC4F22 lizhe]# echo $?
0
[root@A04-R08-I132-131-8WC4F22 lizhe]# [ "abc" = "ABC" ]
[root@A04-R08-I132-131-8WC4F22 lizhe]# echo $?
1
```

## if判断的使用

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

## if-else判断的使用

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

## 嵌套if的使用

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

## case分支

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

## for的基本使用

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

## c语言风格的 for

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

## while循环和until循环

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

## 循环的嵌套和break、continue语句

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

## 使用循环处理位置参数

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

## 自定义函数

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

## 系统函数库介绍

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

## 脚本资源控制

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

## 信号

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

## 计划任务

### 一次性计划任务

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

### 周期性计划任务crontab

- cron
  - 配置方式
    - crontab -e
  - 查看现有的计划任务
    - crontab -l
  - 配置格式：
    - 分钟 小时 日期 月份 星期 执行的命令
    - 注意命令的路径问题

crontab -e 编辑计划任务文件

crontab -l 查看计划任务文件

计划任务文件所在位置：/var/spool/cron/    会生成一个和当前用户名同名的文件

计划任务执行日志：/var/log/cron

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

### 延时计划任务（了解）



### 脚本锁

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

## 案例

### 案例1：打包部署elasticsearch6.8.0版本安装包

skywing

