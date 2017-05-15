from ftplib import FTP
import os

ftp = FTP('192.168.5.31')
ftp.login('cnlab', 'cnlab')
print("Before upload")
ftp.retrlines("LIST")
os.system("ls")
fname = raw_input("Enter filename to upload:")
ftp.storlines("STOR " + fname, open(fname, "r"))
print("After upload")
ftp.retrlines("LIST")
