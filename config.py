from nonebot.default_config import *

# CQHTTP网络通信
# NoneBot 的 HTTP 和 WebSocket 服务端监听的 IP／主机名。
HOST = '127.0.0.1'
# NoneBot 的 HTTP 和 WebSocket 服务端监听的端口。
PORT = 8080
# 需要和 CQHTTP 插件的配置中的 access_token 相同。
ACCESS_TOKEN = ''

COMMAND_START = {'/', '!', '／', '！'}

SUPERUSERS = [12345]  # 管理员（你）的QQ号

DEBUG = False
