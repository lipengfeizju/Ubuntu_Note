# Ubuntu_Note
Some notes about Ubuntu Installation.

[Guide](https://coding.net/help/doc/project/markdown.html) in MarkDown Grammar

[commonly used commands](http://blog.csdn.net/wojiaopanpan/article/details/7286430)

## Disable all the autosuspend mode
```shell
for i in /sys/bus/usb/devices/*/power/autosuspend; do echo -1 >$i; done
```
## Save the passward in Git
use *touch* to create ~/.git-credentials, edit 

``` shell
git config --global user.email "lipengfeizju@gmail.com"
git config --global user.name "Pengfei Li"
touch .git-credentials
vim .git-credentials
https://{username}:{password}@github.com
```

Open a new terminal
``` bash
git config --global credential.helper store
```
Retrieve a former version
```bash
git log
git reset --hard xxxxxxxxxxxxxxxxxxxxxxxxxxxx
git reflog
```
Reference 

[[1]](https://www.cnblogs.com/wanqieddy/archive/2012/08/03/2621027.html)
[[2]](http://www.jianshu.com/p/f54053afecf2)

## Change the kernal 

sudo gedit /etc/default/grub
> GRUB_DEFAULT=saved
>
> GRUB_SAVEDEFAULT=true

sudo update-grub

[GRUB 2 modification](http://blog.csdn.net/lu_embedded/article/details/44353499)

## Copy a file via SSH
```shell
scp /home/test/item.txtroot@192.168.1.129:/etc/test
```
## NetWork Reboot
If the computer can't connect to WWW then try this command
```shell
   sudo /etc/init.d/networking restart
```

## Some important [notes](https://www.cnblogs.com/wangrx/p/5907013.html) about vim

## Build ORB-SLAM
[link](https://github.com/raulmur/ORB_SLAM2)
* install eigen
```shell
    sudo apt-get install libeigen3-dev 
    sudo cp -r /usr/include/eigen3/unsupported  /usr/local/include/

```
* if there is error about opencv, then use this 
```shell
    -DCUDA_USE_STATIC_CUDA_RUNTIME=false
```
# Useful Softwares
## Install the vnc program
```shell
sudo apt install x11vnc -y
sudo x11vnc -storepasswd /etc/x11vnc.pass 
vi  /lib/systemd/system/x11vnc.service
```
content 
```
[Unit]
Description=Start x11vnc at startup.
After=multi-user.target
[Service]
Type=simple
ExecStart=/usr/bin/x11vnc -auth guess -forever -loop -noxdamage -repeat -rfbauth /etc/x11vnc.pass -rfbport 5900 -shared
[Install]
WantedBy=multi-user.target
```
```shell
sudo systemctl daemon-reload
sudo systemctl enable x11vnc.service
sudo systemctl start x11vnc.service
```

系统装好后如果一直闪烁，使用以下命令
```shell

sudo add-apt-repository ppa:bumblebee/stable
sudo apt-get update
sudo apt-get install bumblebee bumblebee-nvidia
sudo reboot
```

## Several Useful DVD writing software
[link](http://www.linuxidc.com/Linux/2013-10/91380.htm)
