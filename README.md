# Simple-Telegram-bot
simple telegram bot to send images replying to name of image!

This is a tutorial for setting up an FTP server with a telegram bot.

## How to setup a FTP Server
1. Install vsftpd
```
sudo apt update && sudo apt upgrade
sudo apt install vsftpd
```
2. Backup from default config file
```
mv /etc/vsftpd.conf /etc/vsftpd.conf.bu
```
3. Create new config `vim /etc/vsftpd.conf` and copy the following base configuration into it
 ```
listen=NO
listen_ipv6=YES
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
use_localtime=YES
xferlog_enable=YES
connect_from_port_20=YES
chroot_local_user=YES
secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=vsftpd
rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
ssl_enable=NO
pasv_enable=Yes
pasv_min_port=10000
pasv_max_port=10100
allow_writeable_chroot=YES
 ```
 4. Set firewall rules and restart vsftpd service
 ```
ufw allow from any to any port 20,21,10000:10100 proto tcp
systemctl restart vsftpd
 ```
5. Create a User for FTP Server and set its password
```
useradd -m ftpuser
passwd ftpuser
```
FTP Server is ready now!
