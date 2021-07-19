# NoneBot-Plugin-Astrologian

## 介绍

兼容NoneBot2的FF14占卜插件，每日（从北京时间23：00）获取固定占卜结果

可以有一次重抽的机会

## 用法

发送命令`/luck`，`/zhanbu`，或者`/占卜`

后面加`r`，`重抽`，或者`redraw`来重抽

后面加`help`来获得帮助，如`/zhanbu help`

## 部署
TODO
1. 创建`.env.dev`在目录，并写入配置
2. run your bot using `nb run` .    

## 狒狒也能看懂的占卜插件部署指南

1. 安装[python](https://www.python.org/downloads/)

3. 将所有文件下载并解压

      如果不会操作，顶部绿色按钮 CODE里选择Download Zip
  
3. 打开install.bat安装前置

4. 打开run.bat运行bot

5. 配置你的机器人添加一个 *ws://127.0.0.1:8080/* 的配置

      我相信看这个的应该都是已经领养好獭獭的用户了吧？如果不是看[文档](https://yimo0908.github.io/easy-build-otterbot/)
  
      示例如下：
  
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
