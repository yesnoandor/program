#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---=' 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         佛祖保佑       永无BUG 



@Date: 2020/8/1
@Name: config.py
@Author: wenyu xu
@Mail: wenyu__xu@163.com

@Description:

'''

import json
import os


def get_config(name="config.json"):
    """

    :return:
    """
    print(os.getcwd())
    path = os.getcwd() + "/" + name
    print(path)
    with open(path, 'r', encoding='utf-8') as f:
        cfg = json.load(f)
        return cfg


if __name__ == '__main__':
    config = get_config("config.json")
    print(config)
    print(type(config))
    pass
