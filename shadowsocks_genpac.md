#Install shadowsocks in Ubuntu
sudo apt-get install python-pip
sudo apt-get install git
pip install git+https://github.com/shadowsocks/shadowsocks.git@master
sudo vim /etc/shadowsocks.json 

#Install autoproxy in Ubuntu
sudo apt-get install python-pip
pip install git+https://github.com/shadowsocks/shadowsocks.git@master

sudo pip install genpac
genpac --proxy="SOCKS5 127.0.0.1:1080" --gfwlist-proxy="SOCKS5 127.0.0.1:1080" -o autoproxy.pac --gfwlist-url="https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt"
>if that doesn't work, try this one
>genpac --proxy="SOCKS5 127.0.0.1:1080" -o autoproxy.pac --gfwlist-url="https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt"

#Start
nohup sslocal -c /etc/shadowsocks.json &

#Set a forward module in command line
sudo apt-get install privoxy -y
sudo gedit /etc/privoxy/config 
>forward-socks5 / localhost:1080 .
>listen-address localhost:8118
sudo gedit /usr/local/bin/proxy
>#!/bin/bash
>export http_proxy=http://localhost:8118
>export https_proxy=http://localhost:8118
>$*
sudo chmod +x /usr/local/bin/proxy 

#Test the proxy
proxy wget google.com


