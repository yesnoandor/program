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
@Name: fsm.py
@Author: wenyu xu
@Mail: wenyu__xu@163.com

@Description:

'''

import threading

lock = threading.Lock()


class fsm:
    # 默认类的属性,不是对象的属性
    __state = None
    __state_list_set = ['idle', 'mot', 'bootparam', 'bl2', 'cert_header', 'bl31', 'tee', 'uboot', 'end']

    def __init__(self):
        pass

    @property                     # 用装饰器实现私有变量作为读属性
    def state(self):
        return self.__state

    @state.setter                 # 用装饰器实现私有变量作为写属性
    def state(self, x):
        print("x = ", x)
        if x not in self.__state_list_set:
            return

        try:
            lock.acquire(True)      # 锁定
            self.__state = x
        finally:
            lock.release()          # 释放


if __name__ == '__main__':
    pass
