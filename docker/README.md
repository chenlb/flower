# 构建 flower docker

镜像说明：
* 使用 [langfarm/python:3.12.9](https://github.com/langfarm/docker-image-python/releases) 基础镜像
* python 安装在 /home/admin/.local 目录下
* 使用 uv 安装源码安装 flower
* admin 用户，当前目录为 /home/admin/flower


## docker-compose 运行

```bash
# 在项目目录下执行
# sh scripts/start-docker-compose.sh

# 或直接用 docker 运行
docker compose -f docker/docker-compose.yml -p flower up
```

## 使用自定义 oauth2 认证

1. 先了解 oauth2 服务，可以用 https://sa-token.cc/doc.html#/oauth2/oauth2-server 按示例，自己搭建 mock oauth2 服务
2. 使用 sa-token 服务实现 profile email 的 scope 实现 userinfo 接口返回 email
3. 修改主 docker/.env.docker 配置你的 oauth2 服务地址和 scope；配置使用 h5 的 oauth2 服务地址，跳转才顺畅。
4. 配置 flower 使用自定义 oauth2 认证，看 docker/flowerconfig.py 文件。
5. 在 docker/docker-compose.yml 修改 flower 的 volumes 配置，把 flowerconfig.py 文件挂载到容器中。

准备好以上事项。运行 docker compose 启动 flower。

浏览器打开：http://localhost:5555
