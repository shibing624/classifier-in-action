# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief:

import os


def read_lines(path):
    lines = []
    with open(path, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if line:
                lines.append(line)
    return lines


def get_file_list(path, postfix, file_list):
    """
    get postfix filename under path
    :param path:
    :param postfix:
    :param file_list:
    :return:
    """
    temp_list = os.listdir(path)
    for f in temp_list:
        f_d = os.path.join(path, f)
        if os.path.isdir(f_d):  # directory need recursion
            get_file_list(f_d, postfix, file_list)
        else:
            if f_d.endswith(postfix):
                file_list.append(f_d)
    return None


def clear_directory(path):
    """
    clear the dir of path
    :param path:
    :return:
    """
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        cmd = 'rm %s/*' % path
        print(cmd)
        os.popen(cmd)
    except Exception as e:
        print("error: %s" % e)
        return False
    return True