# port = 80
debug = True
logging = 'info'
# log_file_prefix = 'logs/access.log'
# log_rotate_mode = 'time'
# log_rotate_when = 'D'
# log_file_num_backups = 3

# 改成 oauth2 返回的 email 格式，或指定 email
# https://flower.readthedocs.io/en/latest/config.html?highlight=auth#auth
auth = '.*@xxx.com'

# https://github/chenlb/flower 实现的自定义 oauth2 认证。
# https://github.com/chenlb/flower/commit/4de36ffb86b858e9d95828e4f2cf3c3b5d0a5e2f
auth_provider = 'flower.views.auth.CustomOauth2LoginHandler'

# 可以用 https://sa-token.cc/doc.html#/oauth2/oauth2-server 按示例，自己搭建 mock oauth2 服务
oauth2_key = '1001'
# 只用于本机 demo。可以用 openssl rand -hex 32 生成
oauth2_secret = 'aaaa-bbbb-cccc-dddd-eeee'
oauth2_redirect_uri = 'http://localhost:5555/login'
