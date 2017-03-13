# coding: utf-8
from ftplib import FTP


# !/usr/local/bin/python
# -*- coding: utf-8 -*-


def ftp_connect(host, username, password):
    ftp = FTP()
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp


def ftp_upload(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR'+remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


if __name__=="__main__":
    ftp = ftp_connect("101.6.58.142", "grad", "1003-2")
    ftp_upload(ftp, "C:/Users/starrysky/Desktop/ip_now.txt", "\\101.6.58.142\grad\柳铮")

    ftp.quit()

