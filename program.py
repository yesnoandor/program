#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
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
@Name: program.py
@Author: wenyu xu
@Mail: wenyu__xu@163.com

@Description:

"""


from tty import *
from config import *
from fsm import *
import time


def program_wait(ser, sub_respond):
    """

    :param ser:
    :param sub_respond:
    :return:
    """
    lines = ser.recv()
    # print("lines = ", lines)
    for line in lines:
        try:
            respond = line.decode()
            # print("line = ", line)
            # print("respond = ", respond)

            if sub_respond in respond:
                return True
        except:
            print("except decode (%s)" % str(line))

    return False


def program_file(ser, start, end, file):
    """

    :param ser:
    :param start:
    :param end:
    :param file:
    :return:
    """
    ser.send("XLS2\r\n")
    time.sleep(0.1)

    while True:
        sub_respond = "Select (1-3)"
        program_ready = program_wait(ser, sub_respond)
        if program_ready:
            ser.send("3\r\n")
            break

        '''
        data = ser.recv()
        print(data)
        respond = [str(i) for i in data]
        respond = "".join(respond)
        print(respond)

        time.sleep(0.1)
        if "Select (1-3)" in respond:
            ser.send("3\r\n")
            break
        '''

    while True:
        sub_respond = "Setting OK? (Push Y key)"
        program_ready = program_wait(ser, sub_respond)
        if program_ready:
            ser.send("Y\r\n")
            break

        '''
        data = ser.recv()
        print(data)
        respond = [str(i) for i in data]
        respond = "".join(respond)
        print(respond)

        time.sleep(0.1)
        if "Setting OK? (Push Y key)" in respond:
            ser.send("Y\r\n")
            break
        '''

    while True:
        sub_respond = "Setting OK? (Push Y key)"
        program_ready = program_wait(ser, sub_respond)
        if program_ready:
            ser.send("Y\r\n")
            break

        '''
        data = ser.recv()
        print(data)
        respond = [str(i) for i in data]
        respond = "".join(respond)
        print(respond)

        time.sleep(0.1)
        if "Setting OK? (Push Y key)" in respond:
            ser.send("Y\r\n")
            break
        '''

    while True:
        sub_respond = "Please Input Program Top Address"
        program_ready = program_wait(ser, sub_respond)
        if program_ready:
            ser.send(start + "\r\n")
            break

        '''
        data = ser.recv()
        print(data)
        respond = [str(i) for i in data]
        respond = "".join(respond)
        print(respond)
        time.sleep(0.1)
        if "Please Input Program Top Address" in respond:
            ser.send(start + "\r\n")
            break
        '''

    while True:
        sub_respond = "Please Input Qspi/HyperFlash Save Address"
        program_ready = program_wait(ser, sub_respond)
        if program_ready:
            ser.send(end + "\r\n")
            break

        '''    
        data = ser.recv()
        print(data)
        respond = [str(i) for i in data]
        respond = "".join(respond)
        print(respond)
        time.sleep(0.1)

        if "Please Input Qspi/HyperFlash Save Address" in respond:
            ser.send(end + "\r\n")
            break
        '''

    while True:
        sub_respond = "Work RAM"
        program_ready = program_wait(ser, sub_respond)
        if program_ready:
            ser.send_file(file)
            break

        '''
        data = ser.recv()
        print(data)
        respond = [str(i) for i in data]
        respond = "".join(respond)
        print(respond)
        time.sleep(0.1)

        if "Work RAM" in respond:
            ser.send_file(file)
            break
        '''

    while True:
        sub_respond = "Clear OK?(y/n)"
        program_ready = program_wait(ser, sub_respond)
        if program_ready:
            ser.send("y\r\n")
            break

        '''    
        data = ser.recv()
        print(data)
        respond = [str(i) for i in data]
        respond = "".join(respond)
        print(respond)
        time.sleep(0.1)
        if "Clear OK?(y/n)" in respond:
            ser.send("y\r\n")
            break
        '''


def program_images():
    config = get_config("config.json")

    port = config["serial_port"]
    bps = config["serial_bps"]

    ddr_mot = config["mot"]
    ddr_mot_respond = config["mot_respond"]

    bootparam_srec = config["bootparam"]
    bootparam_address_start = config["bootparam_address_start"]
    bootparam_address_end = config["bootparam_address_end"]
    bootparam_respond = config["bootparam_respond"]

    bl2_srec = config["bl2"]
    bl2_address_start = config["bl2_address_start"]
    bl2_address_end = config["bl2_address_end"]
    bl2_respond = config["bl2_respond"]

    cert_header_srec = config["cert_header"]
    cert_header_address_start = config["cert_header_address_start"]
    cert_header_address_end = config["cert_header_address_end"]
    cert_header_respond = config["cert_header_respond"]

    bl31_srec = config["bl31"]
    bl31_address_start = config["bl31_address_start"]
    bl31_address_end = config["bl31_address_end"]
    bl31_respond = config["bl31_respond"]

    tee_srec = config["tee"]
    tee_address_start = config["tee_address_start"]
    tee_address_end = config["tee_address_end"]
    tee_respond = config["tee_respond"]

    uboot_srec = config["u-boot"]
    uboot_address_start = config["u-boot_address_start"]
    uboot_address_end = config["u-boot_address_end"]
    uboot_respond = config["u-boot_respond"]

    print("ddr_mot = ", ddr_mot)
    print("ddr_mot_respond", ddr_mot_respond)
    print("bootparam_srec = ", bootparam_srec)
    print("bootparam_address_start = ", bootparam_address_start)
    print("bootparam_address_end = ", bootparam_address_end)
    print("bootparam_respond = ", bootparam_respond)

    print("bl2_srec = ", bl2_srec)
    print("bl2_address_start = ", bl2_address_start)
    print("bl2_address_end = ", bl2_address_end)
    print("bl2_respond = ", bl2_respond)

    print("cert_header_srec = ", cert_header_srec)
    print("cert_header_address_start = ", cert_header_address_start)
    print("cert_header_address_end = ", cert_header_address_end)
    print("cert_header_respond = ", cert_header_respond)

    print("bl31_srec = ", bl31_srec)
    print("bl31_address_start = ", bl31_address_start)
    print("bl31_address_end = ", bl31_address_end)
    print("bl31_respond = ", bl31_respond)

    print("tee_srec = ", tee_srec)
    print("tee_srec_address_start = ", tee_address_start)
    print("tee_srec_address_end = ", tee_address_end)
    print("tee_respond = ", tee_respond)

    print("uboot_srec = ", uboot_srec)
    print("uboot_srec_address_start = ", uboot_address_start)
    print("uboot_srec_address_end = ", uboot_address_end)
    print("uboot_respond = ", uboot_respond)

    print("serial port = ", port)
    print("serial baudrate = ", bps)

    ser = tty(port, bps)

    fsm.state = 'idle'

    while True:
        print("fsm.state = ", fsm.state)
        if fsm.state == 'idle':
            program_ready = program_wait(ser, ddr_mot_respond)
            if program_ready:
                ser.send_file(ddr_mot)
                time.sleep(0.1)
                fsm.state = 'bootparam'

            '''    
            lines = ser.recv()
            print("lines = ", lines)
            for line in lines:
                respond = line.decode()
                print("line = ", line)
                print("respond = ", respond)

                if ddr_mot_respond in respond:
                    ser.send_file(ddr_mot)
                    time.sleep(0.1)
                    fsm.state = 'bootparam'
            '''

            '''
            respond = ser.recv_wait().decode()
            print(respond)
            if ddr_mot_respond in respond:
                ser.send_file(ddr_mot)
                time.sleep(0.1)
                fsm.state = 'bootparam'
            '''
        elif fsm.state == 'bootparam':
            program_ready = program_wait(ser, bootparam_respond)
            if program_ready:
                program_file(ser, bootparam_address_start, bootparam_address_end, bootparam_srec)
                time.sleep(0.1)
                fsm.state = 'bl2'

        elif fsm.state == 'bl2':
            program_ready = program_wait(ser, bl2_respond)
            if program_ready:
                program_file(ser, bl2_address_start, bl2_address_end, bl2_srec)
                time.sleep(0.1)
                fsm.state = 'cert_header'

        elif fsm.state == 'cert_header':
            program_ready = program_wait(ser, cert_header_respond)
            if program_ready:
                program_file(ser, cert_header_address_start, cert_header_address_end, cert_header_srec)
                time.sleep(0.1)
                fsm.state = 'bl31'

        elif fsm.state == 'bl31':
            program_ready = program_wait(ser, bl31_respond)
            if program_ready:
                program_file(ser, bl31_address_start, bl31_address_end, bl31_srec)
                time.sleep(0.1)
                fsm.state = 'uboot'

        elif fsm.state == 'uboot':
            program_ready = program_wait(ser, uboot_respond)
            if program_ready:
                program_file(ser, uboot_address_start, uboot_address_end, uboot_srec)
                time.sleep(0.1)
                fsm.state = 'end'

        elif fsm.state == 'end':
            print("\033[1;34m 烧录成功! \033[0m")  # 设置高亮,字体为蓝色显示
            break


def setenv_cmd(ser, cmd):
    ser.send(cmd + "\r\n")
    time.sleep(0.1)
    print('.', end='', flush=True)
    pass


def setenv_uboot():
    config = get_config("config.json")

    port = config["serial_port"]
    bps = config["serial_bps"]

    ser = tty(port, bps)

    # ser.send("printenv\r\n")
    # time.sleep(2.0)

    baudrate = config["setenv_baudrate"]
    bootdelay = config["setenv_bootdelay"]
    ipaddr = config["setenv_ipaddr"]
    serverip = config["setenv_serverip"]
    ethaddr = config["setenv_ethaddr"]
    img_gaea = config["setenv_img-gaea"]
    dtb_gaea = config["setenv_dtb-gaea"]
    bootargs_udisk = config["setenv_bootargs_udisk"]
    bootcmd_udisk = config["setenv_bootcmd_udisk"]
    booti_cmd = config["setenv_booti_cmd"]
    bootcmd = config["setenv_bootcmd"]

    print("baudrate = ", baudrate)
    print("bootdelay = ", bootdelay)
    print("ipaddr = ", ipaddr)
    print("serverip = ", serverip)
    print("ethaddr = ", ethaddr)
    print("img_gaea = ", img_gaea)
    print("dtb_gaea = ", dtb_gaea)
    print("bootargs_udisk = ", bootargs_udisk)
    print("bootcmd_udisk = ", bootcmd_udisk)
    print("booti_cmd = ", booti_cmd)
    print("bootcmd = ", bootcmd)

    setenv_cmd(ser, baudrate)
    setenv_cmd(ser, bootdelay)
    setenv_cmd(ser, ipaddr)
    setenv_cmd(ser, serverip)
    setenv_cmd(ser, ethaddr)
    setenv_cmd(ser, img_gaea)
    setenv_cmd(ser, dtb_gaea)
    setenv_cmd(ser, bootargs_udisk)
    setenv_cmd(ser, bootcmd_udisk)
    setenv_cmd(ser, booti_cmd)
    setenv_cmd(ser, bootcmd)

    ser.send("saveenv\r\n")
    time.sleep(1.0)
    print("\033[1;34m 设置成功! \033[0m")  # 设置高亮,字体为蓝色显示
    pass


if __name__ == '__main__':
    # program_images()
    setenv_uboot()
    pass
