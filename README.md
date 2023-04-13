## 简介|Introductions

<div>
    <img flex="left" src="https://img.shields.io/badge/python-%3E%3D3.8.0-3776AB"/>
    <img flex="left" src="https://img.shields.io/badge/Sublime%20Text-FF9800?style=flat&logo=Sublime%20Text&logoColor=white"/>
    <img flex="left" src="https://img.shields.io/github/license/caoxiemeihao/electron-vite-vue?style=flat"/>
</div>
SublimeText 每次打开插件市场都要重新下载 `channel_v3.json` 文件，由于国内网络原因，有些时候无法正确下载，或者速度太慢被ST判断为下载超时无法使用。本插件可以定期自动或者手动触发更新`channel_v3.json` 文件，并将其下载到本地进行离线关联，从此秒开`Ctrl + Shfit + P`。

> - 本插件为团队内部打造使用，不对外更新负责，
> - 2023年了，前端建议采用**VSCode**。
> 


## 功能|Feature

![1](/screenshot/sublimeTextPlugs/cps-auto-update-channel/cps-auto-update-channel.gif)
![cps-auto-update-channel](http://localhost:45462/image/cps-auto-update-channel.gif)

- 快捷键：`alt+u`，此时后台下会自动载最新的`channel_v3.json`，具体进度会在最下方的`statusBar`显示。
- 自动更新文件路径到`Package Control.sublime-settings`的`"channels"`字段中



## 安装|Install

```bash
# 打开 SublimeText3的插件目录，并在该目录下打开shell
菜单栏 > Preferences > Browse Packages...

# 在插件目录运行shell，下载插件
# gitee
git clone --depth=1 git@gitee.com:Capsion-ST-PLugins/auto-update-channel.git auto-update-channel
# or github
git clone --depth=1 git@github.com:Capsion-ST-PLugins/auto-update-channel.git auto-update-channel

# 打开控制台查看更新进度
Ctrl + `

# 重启ST 通过快捷键调用（前提要打开一个有效文件）
Ctrl + u
```



## 从此告别

![2](/screenshot/sublimeTextPlugs/cps-auto-update-channel/auto-update-channel2.png)![auto-update-channel2](http://localhost:45462/image/auto-update-channel2.png)

全世界都知道 sublimetext 国内访问插件市场时，有一些地区基本时连不上的，因为 sublimetext 每次搜索插件，安装插件前都会访问一次`https://packagecontrol.io/channel_v3.json`，下载`channel_v3.json`文件。

由于 packagecontrol.io 是国外服务器，访问很慢，有些同事下载只有几 kb 每秒。而且`channel_v3.json`由于存储了所有插件对应的项目地址，文件自身越来越大（截至 2022 年 1 月该文件为 3.7mb），特意写一个后台下载该文件的插件，下载完成后文件会保存在 User 文件夹中。

同时插件可以设置更新周期，一般默认 7 天更新一次。



## **配置文件|Configure**

### 快捷键

- `alt +u`：手动触发更新`channel_v3.json`文件

```js
[
  {
    "keys": ["alt+u"],
    "command": "cps_update_channel"
  }
]
```

### 插件配置

- `Packages/User/cps.sublime-settings`

```js
{
    "auto_update_channel":{
        "enable":true,        // 插件开关
        "auto_update": true,  // 是否更新
        "update_interval": 7, // 多少天更新一次
    }
}
```



## 项目架构|Tree

```ini
DIR:cps-auto-update-channel                  # 
   |-- .sublime/                             # 
   |   |-- Default.sublime-keymap            # 
   |   |-- CpsUpdateChannel.sublime-commands # 
   |   `-- Context.sublime-menu              # 
   |-- core/                                 # 「core」
   |   |-- utils.py                          # 
   |   `-- download_channel_by_url.py        # 通过urllib来下载channel_v3.json文件
   |-- screenshot/                           # 「screenshot」
   |   |-- auto-update-channel2.png          # 
   |   `-- auto-update-channel1.gif          # 
   |-- README.md                             # 
   |-- main.py                               # 核心代码
   `-- .python-version                       # 

```



## 联系方式|Contact

- **373704015 (qq、wechat、email)**
