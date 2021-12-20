# NoneBot-Plugin-Astrologian

## 介绍

兼容NoneBot2的FF14占卜插件，每日（从北京时间23：00）获取固定占卜结果

可以有一次重抽的机会

建议有一定Python基础的用户使用，需要参考Nonebot2[官方文档](https://v2.nonebot.dev/)

## 用法

发送命令`/luck`，`/zhanbu`，或者`/占卜`

后面加`r`，`重抽`，或者`redraw`来重抽

后面加`help`来获得帮助，如`/zhanbu help`

## 第一次使用Nonebot2的用户

1. 阅读[官方文档](https://v2.nonebot.dev/)来了解基础操作
2. 参考官方文档里的[基本配置](https://v2.nonebot.dev/guide/basic-configuration.html)
3. 建议创建`.env`和`.env.dev`在目录，并参考上面的基本配置来写入配置
4. 接下来参考下面的部分，运行机器人

### 附录
如果参考[官方步骤](https://v2.nonebot.dev/guide/installation.html)进行安装后，并看[开始使用](https://v2.nonebot.dev/guide/getting-started.html)进行一个`nb create`后，可参考如下步骤使用本插件

1. 参考官方文档里的[基本配置](https://v2.nonebot.dev/guide/basic-configuration.html)修改`.env`和`.env.dev`或保留配置不动
2. 将clone本项目的`nonebot_plugin_astrologian`复制到你创建机器人的位置
3. 添加`nonebot.load_plugins("nonebot_plugin_astrologian/plugins")`在`bot.py`里的第7行`nonebot.load_builtin_plugins()`后，第10行`nonebot.run()`前
4. 然后执行`pip install pydantic`(注意：这里默认你已经安装了python以及nonebot2，没有的话可以参考)(这里等效`狒狒也能看懂的占卜插件部署指南`的第三步)
5. 从`狒狒也能看懂的占卜插件部署指南`的第四步开始执行
## 狒狒也能看懂的占卜插件部署指南

1. 安装[python](https://www.python.org/downloads/)

3. 将所有文件下载并解压

      如果不会操作，顶部绿色按钮 CODE里选择Download Zip
  
3. 打开install.bat安装前置

4. 打开run.bat运行bot

5. 配置你的机器人添加一个 *ws://127.0.0.1:8080/* 的配置

      我相信看这个的应该都是已经领养好獭獭的用户了吧？如果不是看[文档](https://yimo0908.github.io/easy-build-otterbot/)
  
      Mirai示例如下：
  
          ws_reverse: 
          - enable: true
            postMessageFormat: string
            reverseHost: 【獭窝地址】
            reversePort: 80
            accessToken: 【你的token】
            reversePath: '/ws'
            reverseApiPath: '/api'
            reverseEventPath: '/event'
            useUniversal: true
            useTLS: false
            reconnectInterval: 3000
          - enable: true
            postMessageFormat: string
            reverseHost: 127.0.0.1
            reversePort: 8080
            accessToken: ''
            reversePath: '/ws'
            reverseApiPath: '/api'
            reverseEventPath: '/event'
            useUniversal: true
            useTLS: false
            reconnectInterval: 3000
6. 启动你的机器人
7. 测试占卜
