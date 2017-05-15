from ftplib import FTP
import os
import sys

ftp = ftplib.FTP('192.168.5.31','cnlab','cnlab')
ftp.login()
print("Listing parent directory")
ftp.retrlines("LIST")
fname = raw_input("Enter filename to be copied: ")
opfile = open(fname,"wb+")
ftp.retrbinary("RETR " + fname, opfile.write)
opfile.close()
ftp.close()
