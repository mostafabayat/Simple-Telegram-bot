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

## How to start a telegram bot service
1. Create a Bot in `@BotFather`
    1. Start the Bot
    2. Send `/newbot`
    3. Choose a name for your bot
    4. Choose a username that ends with "bot"
    5. Pick your Token!\
    ![6](https://user-images.githubusercontent.com/45286878/128627276-55fe052a-8b27-400d-8d2e-525bc9215b3a.jpg)
2. Deploy `telegram_bot.py`
    1. Download the `telegram_bot.py` to on your Desktop
    2. Replace `botToken` string in the `telegram_bot.py` with the Token that BotFather gave you
    3. copy `telegram.py` to your server (in /opt directory)
    ```
    scp /mnt/c/Users/Mosi/Desktop/telegram_bot.py root@65.21.21.21:/opt
    ```
    4. Download and copy `telegram_bot.service` to `/lib/systemd/system` directory
    ```
    scp /mnt/c/Users/Mosi/Desktop/telegram_bot.service root@65.21.21.21:/lib/systemd/system/
    ```
    5. ssh to your server and install dependencies
    ```
    sudo apt install python3-pip
    pip install pyTelegramBotAPI
    ```
    6. Enable and start telegram service
    ```
    systemctl daemon-reload
    systemctl enable telegram_bot.service
    systemctl start telegram_bot.service
    ```
    Enjoy!
