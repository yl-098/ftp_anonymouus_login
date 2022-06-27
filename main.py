#import the ftp module 
import ftplib
hostname=input("Please enter the IP address of the FTP server: ")
Domain=input("Enter the domain name: ")

try:
  ftp =ftplib.FTP(hostname)
  ftp.login('anonymous',Domain)
  print (f"FTP anonymous logon succeeded") 
  ftp:quit() 
except Exception as e:
  print(e)
