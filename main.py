# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date:
# @Last Modified by: CPS
# @Last Modified time: 2021-04-12 03:27:20.556970
# @file_path "D:\CPS\IDE\JS_SublmieText\Data\Packages\CPS\core"
# @Filename "update_channel.py"
# @Description: 下载最新的https://packagecontrol.io/channel_v3.json文件
#

import sublime
import sublime_plugin
import os
import time

from .core import utils
from .core import download_channel_by_url


PLUGIN_NAME = "cps_autopdate_channel_v3"
SETTING_FILE = "cps.sublime-settings"
SETTING_KEY = "auto_update_channel"
SETTINGS = {}

OUTPUT_CHANNEL_V3_PATH = os.path.join(
    sublime.packages_path(), "User", "channel_v3.json"
)


def get_floder_list() -> dict:
    return {
        "package_path": os.path.join(sublime.packages_path(), PLUGIN_NAME),
        "user_path": os.path.join(sublime.packages_path(), "User"),
        "channel_v3_file": os.path.join(
            sublime.packages_path(), PLUGIN_NAME, "channel_v3.json"
        ),
        "default_settings": os.path.join(
            sublime.packages_path(), PLUGIN_NAME, ".sublime", SETTING_FILE
        ),
        "package_settings": os.path.join(
            sublime.packages_path(), "User", "Package Control.sublime-settings"
        ),
    }


def get_settings() -> dict:
    global SETTING_FILE, SETTING_KEY
    return sublime.load_settings(SETTING_FILE).get(SETTING_KEY, {})


def plugin_loaded():
    global SETTING_FILE, SETTINGS

    # 在另一个进程执行该函数( 这样不会阻塞窗口的初始化，造成载入文件卡顿 )
    SETTINGS = get_settings()
    if SETTINGS.get("enable"):
        sublime.set_timeout_async(check_package_control_channel, 1)


def check_update():
    global SETTING_FILE, OUTPUT_CHANNEL_V3_PATH

    SETTINGS = get_settings()
    if not SETTINGS.get("auto_update", False):
        return

    currt_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    need_to_update = False
    if not os.path.exists(OUTPUT_CHANNEL_V3_PATH):
        need_to_update = True

    else:
        update_last_time = os.stat(OUTPUT_CHANNEL_V3_PATH).st_mtime
        update_interval = SETTINGS.get("update_interval", 7)  # 默认间隔7天更新一次

        # 对比时间是否已到
        res = utils.time_compare_time(currt_time, update_last_time)
        if res > update_interval:
            print(f"channel_v3_file距离上次更新已超过{res}天，开始尝试更新")
            need_to_update = True

    if need_to_update:
        download_channel_by_url.run(
            OUTPUT_CHANNEL_V3_PATH, stdout=sublime.status_message
        )
    else:
        print(f"channel_v3_file，不需要更新")


def check_package_control_channel():
    # 将channel_v3_file路径写到配置文件
    global OUTPUT_CHANNEL_V3_PATH
    channel_v3_file_path = OUTPUT_CHANNEL_V3_PATH
    package_control_file_path = os.path.join(
        sublime.packages_path(), "User", "Package Control.sublime-settings"
    )

    # 检查v3文件
    if not os.path.exists(OUTPUT_CHANNEL_V3_PATH):
        download_channel_by_url.run(
            OUTPUT_CHANNEL_V3_PATH, stdout=sublime.status_message
        )

    # 检查 Package Control.sublime-settings
    if not os.path.exists(package_control_file_path):
        create_settings_file(package_control_file_path, OUTPUT_CHANNEL_V3_PATH)
    else:
        # 读取 Package Control.sublime-settings
        with open(package_control_file_path, "r", encoding="utf8") as f:
            currt_settings = sublime.decode_value(f.read())
            need_to_update = False

            # 如果当前配置不存在 channels 这个键，则创建
            if not currt_settings.get("channels", None):
                currt_settings["channels"] = [channel_v3_file_path]
                need_to_update = True
            else:
                # 已存在其他channel，进行追加
                if not channel_v3_file_path in currt_settings["channels"]:
                    currt_settings["channels"].append(channel_v3_file_path)
                    need_to_update = True

        # 更新 Package Control.sublime-settings
        if need_to_update:
            with open(package_control_file_path, "w", encoding="utf8") as f:
                f.write(sublime.encode_value(currt_settings, pretty=True))

        check_update()


def create_settings_file(file_name: str, channel_v3_parh: str):
    try:
        with open(file_name, "w", encoding="utf8") as f:
            f.write(
                sublime.encode_value(
                    {"channels": [channel_v3_parh]},
                    pretty=True,
                )
            )
            return True
    except Exception as e:
        print("create_settings_file failed: ", e)
        return False


class CpsUpdateChannelCommand(sublime_plugin.TextCommand):
    def run(self, view) -> None:
        sublime.set_timeout_async(check_package_control_channel, 1)
