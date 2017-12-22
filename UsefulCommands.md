## tar命令
```
压缩分卷
tar czf - ****.tar |split -b 100m - ***.tar.gz
解压缩分卷
cat test1.tar.gza* >myzip.tar.gz
tar xzvf myzip.tar.gz 
合并分卷
tar czvf test.tar.gz example_1.py example_2.py test1.py 
解压缩
tar zxvf FileName.tar.gz
打包
tar cvf FileName.tar DirName
解包
tar xvf FileName.tar
```
## ssh自动登录
安装except解释器
sudo apt-get install tcl tk expect
```shell
#!/usr/bin/expect
spawn ssh root@192.168.22.194
expect "*password:"
send "123\r"
expect "*$"
interact
```

## 重要文件存放位置
/usr/local/bin/  用户可执行文件，可使用如下命令创建软链接
```shell
sudo ln -s /xxx/xxx/xxx.sh /usr/local/bin/xxx
```
/var/cache/apt/archives 存放已经缓存的文件