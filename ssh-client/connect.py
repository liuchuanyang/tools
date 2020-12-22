#coding:utf8
from config import host, port, username, password
import paramiko
def connect():
    t = paramiko.Transport((host,port))
    t.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(t)
    remotepath='/data/yangtianyun/dataset/coco_synthetic/splicing_mask/310807_553179_cup.png'
    localpath='/Users/huan/Desktop/310807_553179_cup.png'
    sftp.get(remotepath, localpath)
    t.close()
connect()