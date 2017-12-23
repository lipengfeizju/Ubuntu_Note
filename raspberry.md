edit config file in TF card
```
max_usb_current=1
hdmi_group=2
hdmi_mode=1
hdmi_mode=87
hdmi_cvt 1024 600 60 6 0 0 0
```
or 
```
sudo vi /boot/config.txt
```
If you can't launch the roscore, then try this 
```shell
sudo killall -9 roscore
sudo killall -9 rosmaster
```

[Install OpenCV](http://blog.csdn.net/xukai871105/article/details/41084949)