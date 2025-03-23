#!/bin/sh

if [ -z "$PORT" ]; then
  PORT=5555
  export PORT
fi

# 设置 admin 登录的环境
source /home/admin/.bashrc

# 设置 flower 环境变量

if [ -z "$URL_PREFIX" ]; then
  # 没有 URL_PREFIX, 就直接启动
  echo "celery flower --port=${PORT}"
  celery flower --port=${PORT}
else
  # 有 URL_PREFIX, 加上参数启动
  echo "celery flower --port=${PORT} --url_prefix=${URL_PREFIX}"
  celery flower --port=${PORT} --url_prefix=${URL_PREFIX}
fi
