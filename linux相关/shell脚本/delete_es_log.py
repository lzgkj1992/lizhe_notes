#!/usr/bin/env python
import os
import commands
import logging

logging.basicConfig(
    filename="/tmp/delete_log.log",
    filemode="w",
    format="%(asctime)s|%(levelname)s|%(message)s",
    level=logging.INFO
)

def GetPath():
    os.chdir("/export/Instances")
    dirs = []
    dir_list = os.listdir(os.getcwd())
    for dir in dir_list:
        path = os.getcwd() + "/" + dir
        os.chdir(path)  # app_path
        for dir2 in os.listdir(os.getcwd()):
            path_2 = os.getcwd() + "/" + dir2
            os.chdir(path_2)  # instance_path
            dirs.append(path_2)
            os.chdir(path)
    return dirs


def GetLogPath():
    logs_path_list = []
    dir_res = GetPath()
    for path in dir_res:
        es_config = path + "/runtime/elasticsearch/config/elasticsearch.yml"
        with open(es_config) as f:
            for line in f.readlines():
                line = line.strip()
                if line.startswith("logs:"):
                    logs_path = line.split(":")
                    logs_path_list.append(logs_path[1].strip())
    return logs_path_list


def ShellCmd(cmd):
    status, output = commands.getstatusoutput(cmd)
    res = "cmd: %s\n" \
          "exec status: %s\n" \
          "exec result: %s\n" % (cmd, status, output)
    logging.info(res)


if __name__ == "__main__":
    logs_conf_path = GetLogPath()
    for i in logs_conf_path:
        # cmd = "find " + i + " -regex  \".*log.gz\" -atime +3 |xargs rm -rf"
        cmd = "find " + i + " -regex  \".*log.gz\" -atime +3"
        ShellCmd(cmd=cmd)