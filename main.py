# -*- coding: utf-8 -*-
import nfc
import pandas as pd
import numpy as np
import time
from time import sleep
from servo import Servo

def read_card():
    clf = nfc.ContactlessFrontend('usb') # デバイスの中から１番最初に見つかったものに接続
    print(clf) #デバイスを表示
    servo = Servo()

    while True:
        tag = clf.connect(rdwr={'on-connect': lambda tag: False})
        tag_print = str(tag).split()

        print(tag_print)

        df = pd.read_csv("~/Desktop/name.csv")
        df_id = list(df["ID"])

        user_id = tag_print[4].replace("ID=","")
        print(user_id)

        if user_id in df_id:
            servo.change_angle()
            print('tempo')
        else:
            print('tanpo')
        time.sleep(2)

    del servo

if __name__ == '__main__':
    read_card()
