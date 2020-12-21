# sh脚本





```shell

#!/bin/bash
set -e
echo 'downloads es packages'
curl -O http://storage-jd-local-jcloud-admin.proxy.jd.com/software-package1/elasticsearch-6.8.0.tar.gz
ls -l ./
echo 'unzip tar package'
#cd packages
tar -zxvf elasticsearch-6.8.0.tar.gz

echo 'copy packages file'
# mkdir output
mkdir -pv output/elasticsearch
mkdir -pv output/bin
cp -r ./elasticsearch-6.8.0/* output/elasticsearch
cp -r ./skywing/control_container output/bin/control
cp -r ./conf/elasticsearch.service output/elasticsearch/config/
cp -r ./conf/elastic-certificates.p12 output/elasticsearch/config/
cp -r ./plugins/ik  output/elasticsearch/plugins/
```



**upload_package_anlian.sh**

```yaml
#! /bin/bash

set -o nounset
set -o errexit

readonly NGINX_HOST="10.12.242.5"
readonly DEST_PKG="package.ark.jdcloud.local"
readonly DEST_VER="prod.ark.jdcloud.local"
readonly TRANSFER_HOST="36.110.152.1"

readonly TENANT="jcloud"

if [ $# != 3 ]
then
    echo "bash $(basename $0) <module_name> <version> <donwload_url>"
    exit 1
fi

SRC_PKG_URL=$3
MODULE=$1
MODULE_GROUP="$(echo $MODULE | awk -F '/' '{print $1}')"
MODULE_NAME="$(echo $MODULE | awk -F '/' '{print $2}')"
VERSION=$2

PACKAGE=$MODULE_NAME-$VERSION.tar.gz

PKG_CHECK=$(curl -I $SRC_PKG_URL | grep HTTP | awk '{print $3}' | tr -d '\r')
echo $PKG_CHECK
if [ X"${PKG_CHECK}" = X"OK" ]
then
    echo "Check Download URL Successfully"
    curl -o /tmp/$PACKAGE $SRC_PKG_URL
else
    echo "Check Download URL Failed"
    exit 1
fi

rsync -avP /tmp/$PACKAGE root@${TRANSFER_HOST}:/tmp/
ssh root@${TRANSFER_HOST} "bash /export/servers/skywing/package_init.sh $MODULE $VERSION $SRC_PKG_URL"

```





