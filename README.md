# smart-lock

class Servo():
  コンストラクタ(pin)
    PIN=pin
    内部状態
    セットアップ
    open用デューティ比 
    close用デューティ比
    
  角度変更():
    start
    if 内部状態 = open:
      close()
    else:
      open()
    stop
  
  open():
    duty比変更
    内部状態変更
    sleep
  
  close():
    duty比変更
    内部状態変更
    sleep
  
  
