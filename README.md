# NoneBot-Plugin-Astrologian

## 介绍

NoneBot2-beta版本的FF14占卜插件，本身基于Onebot适配器编写，因为Nonebot2本身原因，不兼容Nonebot2-alpha版本，请切换分支

每日（从北京时间23：00）获取固定占卜结果

可以有一次重抽的机会

建议有一定Python基础的用户使用，需要参考Nonebot2[官方文档](https://v2.nonebot.dev/)

## 用法

发送命令`/luck`，`/zhanbu`，或者`/占卜`

后面加`r`，`重抽`，或者`redraw`来重抽

后面加`help`来获得帮助，如`/zhanbu help`

## 第一次使用Nonebot2的用户

1. 阅读[官方文档](https://v2.nonebot.dev/)来了解如何安装
2. 参考官方文档里的[基本配置](https://v2.nonebot.dev/docs/tutorial/configuration)
3. 建议创建`.env`和`.env.dev`在目录，并参考上面的基本配置来写入配置
4. 接下来参考下面的部分，运行机器人

### 附录
如果参考[官方步骤](https://v2.nonebot.dev/docs/start/installation)进行安装后，并看[创建项目](https://v2.nonebot.dev/docs/tutorial/create-project)进行`nb create`后，可参考如下步骤使用本插件，请根据你的QQ机器人情况进行选择，本项目中使用了`onebot`适配器

1. 参考官方文档里的[基本配置](https://v2.nonebot.dev/guide/basic-configuration.html)修改`.env`和`.env.dev`或保留配置不动
2. 将clone本项目的`nonebot_plugin_astrologian`复制到你创建机器人的位置
3. 添加`nonebot.load_plugins("nonebot_plugin_astrologian/plugins")`在`bot.py`里的第22行`driver.register_adapter(ONEBOT_V11Adapter)`后，第10行`nonebot.run(app="__mp_main__:app")`前
4. 然后执行`pip install pydantic`(注意：这里默认你已经安装了python以及nonebot2，没有的话可以参考)(这里等效`狒狒也能看懂的占卜插件部署指南`的第三步)
5. 从`狒狒也能看懂的占卜插件部署指南`的第四步开始执行
## 狒狒也能看懂的占卜插件部署指南

1. 安装[python](https://www.python.org/downloads/)

3. 将所有文件下载并解压

      如果不会操作，顶部绿色按钮 CODE里选择Download Zip
  
3. 打开install.bat安装前置

4. 打开run.bat运行bot

5. 配置你的机器人添加一个 *ws://127.0.0.1:8080/onebot/v11/ws* 的配置

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
            reversePath: '/onebot/v11/ws'
            reverseApiPath: '/onebot/v11/api'
            reverseEventPath: '/onebot/v11/event'
            useUniversal: true
            useTLS: false
            reconnectInterval: 3000
6. 启动你的机器人
7. 测试占卜
