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
@Name: tty.py
@Author: wenyu xu
@Mail: wenyu__xu@163.com

@Description:

'''

import time
import serial


class tty:
    """
    """

    def __init__(self, port, bps="115200"):
        """

        :param port:
        """
        self.ser = serial.Serial(port=port,
                                 baudrate=bps,
                                 bytesize=8,
                                 parity='N',
                                 stopbits=1,
                                 timeout=0.5)

    def send(self, cmd):
        """

        :param cmd:
        :return:
        """
        self.ser.write(cmd.encode())
        # print(cmd.encode())
        time.sleep(0.3)
        self.ser.flush()

    def send_file(self, file):
        """
        发送文件
        :param flash_file:
        :return:
        """
        with open(file, "r") as f:
            if self.ser.isOpen():
                print("program the image : %s ", file)

                count = 0
                for line in f.readlines():
                    if not line:
                        print("%s send over!" % file)
                        break
                    self.ser.write(line.encode())
                    # print(i, "：", flash_line.encode())
                    time.sleep(0.001)
                    self.ser.flush()

                    count = count + 1
                    if count % 100 == 0:
                        # print('count = ', count)
                        print('.', end='', flush=True)

                print('')
                print("program %s successfully !", file)
            else:
                print("The device serial port is not open")

    def recv(self):
        """

        :return:
        """
        while True:
            data = self.ser.readlines()
            if not data:
                continue
            else:
                break
        return data


if __name__ == '__main__':
    pass
