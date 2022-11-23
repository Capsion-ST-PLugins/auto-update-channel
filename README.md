# 简介|Introductions

sublimeText每次打开插件市场都要重新下载channel_v3.json文件，这是一个可以自动更新channel_v3.json，同时自动关联到配置的插件。

<div>
    <img flex="left" src="https://img.shields.io/badge/python-%3E%3D3.8.0-3776AB"/>
    <img flex="left" src="https://img.shields.io/badge/Sublime%20Text-FF9800?style=flat&logo=Sublime%20Text&logoColor=white"/>
    <img flex="left" src="https://img.shields.io/github/license/caoxiemeihao/electron-vite-vue?style=flat"/>
</div>

[English](README.en.md) | 简体中文





# 起因

全世界都知道sublimetext国内访问插件市场时，有一些地区基本时连不上的，因为sublimetext每次搜索插件，安装插件前都会访问一次`https://packagecontrol.io/channel_v3.json`，下载`channel_v3.json`文件。

由于packagecontrol.io是国外服务器，访问很慢，有些同事下载只有几kb每秒。而且`channel_v3.json`由于存储了所有插件对应的项目地址，文件自身越来越大（截至2022年1月该文件为3.7mb），特意写一个后台下载该文件的插件，下载完成后文件会保存在User文件夹中。

同时插件可以设置更新周期，一般默认7天更新一次。





# 主要功能

- 后台下载最新的`channel_v3.json`
- 自动更新文件路径到`Package Control.sublime-settings`的`"channels"`字段中

使用演示：

![step1](1.gif)



# 插件配置

`${Packages}\User\cps.sublime-settings`

```js
{ 
    "auto_update_channel":{
        "enable":true,        // 插件开关
        "auto_update": true,  // 是否更新
        "update_interval": 7, // 多少天更新一次
      }
}
```

