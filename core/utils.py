# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 
# @Last Modified by: CPS
# @Last Modified time: 2021-08-06 11:16:54.145176
# @file_path "Z:\CPS\IDE\SublimeText\sublime_text_4113.21_win64_test\Data\Packages\testt_comments_creater\core"
# @Filename "utils.py"
# @Description: 功能描述
#

import time, datetime

def time_compare_time(time1, time2, time_format='%Y-%m-%d %H:%M:%S') -> int:
    '''
    - Description 对比`time1`和`time2`的大小，支持时间戳、字符串格式、`time.struct_time`

    - time1 {str:`time_format` | `time.struct_time` | float:`时间戳`}
    - time2 {str:`time_format` | `time.struct_time` | float:`时间戳`}
    
    - time_format {str: `'%Y-%m-%d %H:%M:%S'` } 指定当前的时间格式

    - return { int } 返回大于0，则time1 大于time2, 反之

    - example

    ```py
    time1 = time.localtime()
    time2 = "1990-08-12 15:16:44"
    if time_compare_time(time1, time2) > 0: 
        print(f'time1 日期比 time2 日期新，相差：{res}天')
    ```
    '''
    t1 = time1
    t2 = time2
    # 将字符串转换为时间戳
    if isinstance(time1, str):
        t1 = time.mktime(time.strptime(time1, time_format))

    if isinstance(time2, str):
        t2 = time.mktime(time.strptime(time2, time_format))

    if isinstance(time1, time.struct_time):
        t1 = time.mktime(time1)

    if isinstance(time2, time.struct_time):
        t2 = time.mktime(time2)

    if isinstance(t1, float) and isinstance(t2, float):
        return int((t1 - t2) / 3600 / 24)
    
    return 0

def args_to_lower(func):
    def tes(*args,**kwargs):
        nargs = []
        for each in args:
            nargs.append(each.lower().strip())

        func(*nargs)
    return func

@args_to_lower
def is_stylus(filename):
    #通过 file_name 判断 stylus
    if filename.endswith('.stylus') or filename.endswith('.styl'):
        return True

@args_to_lower
def is_vue(filename):
    #通过 file_name 判断 vue
    if filename.endswith('.vue'):
        return True

@args_to_lower
def is_html(filename):
    #通过 file_name 判断 html
    if filename.endswith('.html') or filename.endswith('.xml'):
        return True

@args_to_lower
def is_pug(filename):
    #通过 file_name 判断 pug
    if filename.endswith('.pug'):
        return True

@args_to_lower
def is_js(filename):
    for each in ['.cjs','.mjs','.js']:
        if filename.endswith(each):
            return True

@args_to_lower
def is_ts(filename):
    for each in ['.ts']:
        if filename.endswith(each):
            return True

@args_to_lower
def is_json(filename):
    for each in ['.json']:
        if filename.endswith(each):
            return True

@args_to_lower
def is_python(filename):
    for each in ['.py']:
        if filename.endswith(each):
            return True


@args_to_lower
def sublime_syntax_check(syntax):
    for each in ['typescript','javascript','json','css','html']:
        if(syntax.lower().rfind(each)>0):
            return each
    return False


"""
Description

: param filename:{string} paramDescription
: returns {string} returnsDescription
"""
def check_stynax(filename):    
    if is_stylus(filename):
        return 'stylus'
    if is_vue(filename):
        return 'vue'
    if is_html(filename):
        return 'html'
    if is_pug(filename):
        return 'pug'
    if is_js(filename):
        return 'javascript'
    if is_ts(filename):
        return 'typescript'
    if is_json(filename):
        return 'json'
    if is_python(filename):
        return 'python'

    res = sublime_syntax_check(filename)

    return res if res else False

def get_date_now(self,fmat):
    try:
        if not fmat:
            fmat = r'%Y-%m-%d %H:%M:%S'
        return datetime.datetime.now().__format__(fmat)
    except Exception as e:
        return datetime.datetime.now().__format__(r'%Y-%m-%d %H:%M:%S')

def recursive_update(dict1:dict, dict2:dict) -> dict:
    '''
    - 递归更新字典对象，`dict2`的属性会更新到`dict1`内，
    - dict1 {dict} 
    - dict2 {dict}
    - return { dict }
    '''
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError('Params of recursive_update should be dicts')

    for key in dict2:
        if isinstance(dict2[key], dict) and isinstance(
                dict1.get(key), dict):
            dict1[key] = recursive_update(dict1[key], dict2[key])
        else:
            dict1[key] = dict2[key]

    return dict1

if (__name__ == "__main__"):
    print(check_stynax('Packages/Python/Python.sublime-syntax'))
