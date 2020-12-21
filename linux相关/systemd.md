# systemd

## 参考资料

- 参考资料一：http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-commands.html
- 参考资料二：http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-part-two.html
- 参考资料三：https://wiki.archlinux.org/index.php/systemd_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)
- 参考资料四：https://blog.csdn.net/weixin_37766296/article/details/80192633

## 常用命令

```shell
systemctl list-units --all --type=service

```

jmiss-redis-agent.service

```shell
[Unit]
Description=jmiss-redis-agent daemon

[Service]
Type=forking
ExecStart={JMISS_REDIS_PATH}/jmiss-redis-agent/bin/start.sh
ExecStop={JMISS_REDIS_PATH}/jmiss-redis-agent/bin/stop.sh
ExecReload={JMISS_REDIS_PATH}/jmiss-redis-agent/bin/start.sh
Restart=on-failure
RestartSec=10s
LimitNOFILE=102400

[Install]
WantedBy=multi-user.target
```

示例：

```shell
$ systemctl cat sshd.service

[Unit]
Description=OpenSSH server daemon
Documentation=man:sshd(8) man:sshd_config(5)
After=network.target sshd-keygen.service
Wants=sshd-keygen.service

[Service]
EnvironmentFile=/etc/sysconfig/sshd
ExecStart=/usr/sbin/sshd -D $OPTIONS
ExecReload=/bin/kill -HUP $MAINPID
Type=simple
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target
```

lf-monitor集群开机自启动设置：

```shell
[Unit]
Description=Elasticsearch
Documentation=http://www.elastic.co
Wants=network-online.target
After=network-online.target

[Service]
RuntimeDirectory=elasticsearch
Environment=ES_HOME=/usr/share/elasticsearch
Environment=ES_PATH_CONF=/etc/elasticsearch/node-0
Environment=PID_DIR=/var/run/elasticsearch/node-0
EnvironmentFile=-/etc/sysconfig/elasticsearch

WorkingDirectory=/usr/share/elasticsearch

User=elasticsearch
Group=elasticsearch

ExecStart=/usr/share/elasticsearch/bin/elasticsearch -p ${PID_DIR:q：elasticsearch.pid --quiet

# StandardOutput is configured to redirect to journalctl since
# some error messages may be logged in standard output before
# elasticsearch logging system is initialized. Elasticsearch
# stores its logs in /var/log/elasticsearch and does not use
# journalctl by default. If you also want to enable journalctl
# logging, you can simply remove the "quiet" option from ExecStart.
StandardOutput=journal
StandardError=inherit

LimitMEMLOCK=infinity

# Specifies the maximum file descriptor number that can be opened by this process
LimitNOFILE=65536

# Specifies the maximum number of processes
LimitNPROC=4096

# Specifies the maximum size of virtual memory
LimitAS=infinity

# Specifies the maximum file size
LimitFSIZE=infinity

# Disable timeout logic and wait until process is stopped
TimeoutStopSec=0

# SIGTERM signal is used to stop the Java process
KillSignal=SIGTERM

# Send the signal only to the JVM rather than its control group
KillMode=process

# Java process is never killed
SendSIGKILL=no

# When a JVM receives a SIGTERM signal it exits with code 143
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target
```

### **自己写哒 elasticsearch.service：**

```shell
[Unit]
Description=elasticsearch
After=network.target
[Service]
Type=simple
Environment=JAVA_HOME=/export/work/jdk
ExecStart=/export/Instances/hb-es-qkh/50.hb-es-qkh/runtime/elasticsearch/bin/elasticsearch --quiet
RestartSec=60s
Restart=on-failure
LimitNOFILE=65536
LimitNPROC=204800
LimitMEMLOCK=infinity
User=admin
[Install]
WantedBy=multi-user.target
```

### **control:**

```shell
#!/usr/bin/env bash

[ $USER = admin ] || {
        echo 'Need to be admin'
        exit 1
}

source /etc/profile
cd "$(dirname $0)"/.. || exit 1

source ./default_env.sh

SYSTEMD_NAME="elasticsearch"
PROC_NAME=java # 进程名
PROC_PORT=${SKYWING_PORT} # 没有可不写
WAIT_TIME=150 # 等待启动/停止时间


help(){
    echo "${0} <start|stop|restart|status>"
    exit 1
}
checkhealth(){
    echo ${PROC_PORT}
    if [[ -n "$PROC_PORT" ]] ; then
        PORT_PROC=$(/usr/sbin/ss -nltp "( sport = :$PROC_PORT )" |sed 1d |awk '{print $NF}' |grep -oP "\"\w+\"" |sed "s/\"//g" |uniq)
        if [ X"$PORT_PROC" = X"$PROC_NAME" ] ; then
                echo "running"
            return 0
        fi
        echo "not running"
        return 1
    else
	ps -eo comm,pid |grep -P  "^$PROC_NAME\b"
	if [ "$?" = 0 ] ; then
	echo "running"
	    return 0
	fi
	echo "not running"
	return 1
    fi
}
start(){
    checkhealth
    if [ $? = 0 ]; then
        echo "[WARN] $PROC_NAME is aleady running!"
        return 0
    fi
    mkdir -p log

    es_workspace=`pwd`
    echo ${es_workspace}
    echo ${SKYWING_PORT}
    echo ${PROC_PORT}
    sed -i 's#{WORKSPACE}#'${es_workspace}'#g' ./elasticsearch/config/elasticsearch.service;
    sudo rm -f /usr/lib/systemd/system/${SYSTEMD_NAME}_${PROC_PORT}.service;
    sudo cp -r ./elasticsearch/config/elasticsearch.service /usr/lib/systemd/system/${SYSTEMD_NAME}_${PROC_PORT}.service;
    echo ${SYSTEMD_NAME}_${PROC_PORT}.service
    sudo systemctl daemon-reload;
    sudo systemctl restart ${SYSTEMD_NAME}_${PROC_PORT}.service;
    # ./elasticsearch/bin/elasticsearch -d

    for i in $(seq $WAIT_TIME) ; do
        sleep 1
        checkhealth
        if [ $? = 0 ]; then
            echo "Start $PROC_NAME success"
            return 0
        fi
    done
    echo "[ERROR] Start $PROC_NAME failed"
    return 1
}
stop(){
    if [[ -n "$PROC_PORT"  ]] ; then
        PROC_ID=$(  /usr/sbin/ss -nltp "( sport = :$PROC_PORT )" |sed 1d  | awk '{print $NF}' |  grep -oP '\,.*\,' | grep -oP "\d+" |  uniq )
    else
        PROC_ID=$(ps -eo comm,pid  | grep "^$PROC_NAME\b" |awk '{print $2}')
    fi
    if [[ -z "$PROC_ID" ]] ; then
        echo "[WARN] $PROC_NAME is aleady exit, skip stop"
        return 0
    fi
    checkhealth
    if [ "$?" != "0" ] ; then
        echo "[WARN] $PROC_NAME is aleady exit, skip stop"
        return 0
    fi
    #$TOMCAT_HOME/bin/shutdown.sh
    kill $PROC_ID
    for i in $(seq $WAIT_TIME) ; do
        sleep 1
        checkhealth
        if [ "$?" != "0" ] ; then
            echo "Stop $PROC_NAME success"
            return 0
        fi
    done
    kill -9 $PROC_ID
    sleep 1
    checkhealth
    if [ "$?" != "0" ] ; then
        echo "Stop $PROC_NAME success"
        return 0
    fi
    echo "[ERROR] Stop $PROC_NAME failed"
    return 1
}
case "${1}" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    status|health|checkhealth)
        checkhealth
        ;;
    restart)
        stop && start
        ;;
    *)
        help
        ;;
esac

```

### healthcheck.sh

```shell
#!/bin/bash

# 0. test healthy
# 1. once test_healthy return true, we report the node is healthy
# 2. if test_healthy return false 6 times, we report the node is unhealthy

# test passed in 6.8.0

cd "$(dirname $0)" || exit 1

LOG_FILE=./health.log
COUNT_FILE=./retry.count
NODE_PORT=$(tail -n 1 ./node.port)
WAIT_TIME=10 # 等待停止时间

function do_log(){
   cur_time=`TZ=Asia/Shanghai date "+%Y-%m-%d %H:%M:%S"`
   echo  "[$1] "$cur_time" $2" >> $LOG_FILE
}

function test_port() {
  c=`netstat -ntpul | grep ":$NODE_PORT" |wc -l`
  if [[ "$c" != "1"  ]]; then
    do_log WARN "es port no exit"
    echo 0 > "$COUNT_FILE"
    exit 1
  fi
}

function test_healthy(){
  resp=`curl -i -X GET --connect-timeout 3 --max-time 3 --retry 0 "http://admin:jcloud-es@127.0.0.1:$NODE_PORT"`
  # connection error
  if [[ $? -ne 0 ]]; then
    do_log WARN "http connection failed: "${resp}
    return 1
  fi

  # if the port is opened, then we take es node as running fine

  # log if http error, give us chance learn more about es response
  http_code=`echo "$resp" | head -n 1|cut -d$' ' -f2`
  if [[ "$http_code" != "200" ]]; then
    do_log WARN "http error, content: "
    echo "$resp" >> $LOG_FILE
  fi
}

# init count file
if [ ! -f "$COUNT_FILE" ]; then
  echo 0 > "$COUNT_FILE"
fi

# if port not exit, don't exect test
test_port

if test_healthy; then
  do_log INFO "healthy"
  echo 0 > "$COUNT_FILE"
  exit 0
fi

# when retriedCount is illegal, reported unhealthy
retriedCount=$(tail -n 1 "$COUNT_FILE")
if ! echo "$retriedCount" | grep '^[0-2]\{1\}$'; then
  do_log ERROR "because unhealthy.retriedCount is:$retriedCount,so node need to restart"
  # 获取进程id
  PROC_ID=$( /usr/sbin/ss -nltp "( sport = :$NODE_PORT )" |sed 1d  | awk '{print $NF}' |  grep -oP '\,.*\,' | grep -oP "\d+" |  uniq )
  # 杀死进程
  kill $PROC_ID
  for i in $(seq $WAIT_TIME) ; do
     sleep 1
     c=`netstat -ntpul | grep ":$NODE_PORT" |wc -l`
     if [[ "$c" != "1"  ]]; then
        do_log INFO "Stop $NODE_PORT success"
        echo 0 > "$COUNT_FILE"
        exit 0
     fi
  done
  kill -9 $PROC_ID
  sleep 3
  c=`netstat -ntpul | grep ":$NODE_PORT" |wc -l`
  if [[ "$c" != "1"  ]]; then
  	do_log WARN "Stop $NODE_PORT success by kill -9"
  	echo 0 > "$COUNT_FILE"
  	exit 0
  fi
  do_log ERROR "Stop $NODE_PORT failed"
  exit 1
fi

cnt=$((retriedCount + 1))
do_log WARN "unhealthy.retriedCount is:$cnt"
echo "${cnt}" > "$COUNT_FILE"
exit 0
```

自己写的 healthcheck.sh

```shell
#!/bin/bash

# 0. test healthy
# 1. once test_healthy return true, we report the node is healthy
# 2. if test_healthy return false 6 times, we report the node is unhealthy

# test passed in 6.8.0

LOG_FILE=./health.log
COUNT_FILE=./retry.count
NODE_PORT=$(tail -n 1 ./node.port)
WAIT_TIME=10 # 等待停止时间

function do_log(){
   cur_time=`TZ=Asia/Shanghai date "+%Y-%m-%d %H:%M:%S"`
   echo  "[$1] "$cur_time" $2" >> $LOG_FILE
}

function test_port() {
  c=`netstat -ntpul | grep ":$NODE_PORT" |wc -l`
  if [[ "$c" != "1"  ]]; then
    do_log WARN "es port no exit"
    echo 0 > "$COUNT_ FILE"
    exit 1
  fi
}

function test_healthy(){
  resp=`curl -i -X GET --connect-timeout 3 --max-time 3 --retry 0 "http://admin:jcloud-es@127.0.0.1:$NODE_PORT"`
  # connection error
  if [[ $? -ne 0 ]]; then
    do_log WARN "http connection failed: "${resp}
    return 1
  fi

  # if the port is opened, then we take es node as running fine

  # log if http error, give us chance learn more about es response
  http_code=`echo "$resp" | head -n 1|cut -d$' ' -f2`
  if [[ "$http_code" != "200" ]]; then
    do_log WARN "http error, content: "
    echo "$resp" >> $LOG_FILE
  fi
}

# init count file
if [ ! -f "$COUNT_FILE" ]; then
  echo 0 > "$COUNT_FILE"
fi

# if port not exit, don't exect test
test_port

if test_healthy; then
  do_log INFO "healthy"
  echo 0 > "$COUNT_FILE"
  exit 0
fi

# when retriedCount is illegal, reported unhealthy
retriedCount=$(tail -n 1 "$COUNT_FILE")
if ! echo "$retriedCount" | grep '^[0-2]\{1\}$'; then
  do_log ERROR "because unhealthy.retriedCount is:$retriedCount,node need to restart"
  # 获取进程id
  PROC_ID=$( /usr/sbin/ss -nltp "( sport = :$NODE_PORT )" |sed 1d  | awk '{print $NF}' |  grep -oP '\,.*\,' | grep -oP "\d+" |  uniq )
  # 杀死进程
  kill $PROC_ID
  for i in $(seq $WAIT_TIME) ; do
     sleep 1
     c=`netstat -ntpul | grep ":$NODE_PORT" |wc -l`
     if [[ "$c" != "1"  ]]; then
        do_log ERROR "Stop $NODE_PORT success"
        echo 0 > "$COUNT_FILE"
        exit 0
     fi
  done
  kill -9 $PROC_ID
  sleep 3
  c=`netstat -ntpul | grep ":$NODE_PORT" |wc -l`
  if [[ "$c" != "1"  ]]; then
  	do_log ERROR "Stop $NODE_PORT success"
  	echo 0 > "$COUNT_FILE"
  	exit 0
  fi
  do_log ERROR "Stop $NODE_PORT failed"
  exit 1
fi

cnt=$((retriedCount + 1))
do_log WARN "unhealthy.retriedCount is:$cnt"
echo "${cnt}" > "$COUNT_FILE"
exit 1
```

sudo sed -i 's/#Defaults requiretty/Defaults requiretty/g' /etc/sudoers