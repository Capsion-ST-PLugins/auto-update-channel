# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-11-22 22:41:11.106612
# @Last Modified by: CPS
# @Last Modified time: 2022-11-22 22:41:11.106612
# @file_path "D:\CPS\IDE\JS_SublmieText\Data\Packages\testt_update_channel\core"
# @Filename "download_channel_by_url.py"
# @Description: 下载最新的channel_v3.json
#
import shutil
import tempfile

from os import path
from urllib.request import urlretrieve, urlopen, urlcleanup

# url = "https://packagecontrol.io/channel_v3.json"
# header = {
#     "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
# }


def check_url(url) -> bool:
    res = urlopen(url)

    return bool(res.getcode() == 200)


def run(
    output: str, *, stdout=None, url: str = "https://packagecontrol.io/channel_v3.json"
) -> str:
    if check_url(url):

        def download_report(count, block_size, total_size):
            downloaded = count * block_size
            percent = 100.0 * downloaded / total_size
            percent = round(min(100, percent), 2)
            msg = f"【channel_v3.json】 downloading: {downloaded}/{total_size}, {percent}% completed;"
            print(msg)
            if stdout:
                stdout(msg)

        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                temp_file = path.join(tmpdir, "channel_v3.json")
                # temp_file = "channel_v3.json"
                print("开始下载channel_v3.json文件:", temp_file)
                res = urlretrieve(url, temp_file, reporthook=download_report)
                shutil.copyfile(temp_file, output)
                print("下载channel_v3.json文件完成:", output)
                urlcleanup()
        except Exception as e:
            print("下载失败： ", e)

    else:
        print("检查url不通过，请稍后再试")


# if __name__ == "__main__":
#     run("./channel_v3.json")
