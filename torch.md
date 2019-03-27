lua安装
wget https://www.lua.org/ftp/lua-5.2.4.tar.gz
tar zxf lua-5.2.4.tar.gz
cd lua-5.2.4
make linux test
make install

wget http://luarocks.org/releases/luarocks-2.2.2.tar.gz
tar zxvf luarocks-2.2.2.tar.gz
cd luarocks-2.2.2
./configure --prefix=/usr/local/luarocks-2.2.2 --with-lua=/usr/local/lua

在conda中安装torch
conda create --name torch7
conda install -c conda-forge lua=5.2.4
git clone https://github.com/torch/distro.git ~/torch --recursive
TORCH_LUA_VERSION=LUA52 ./install.sh

luarocks install image
luarocks install hdf5
(gcc should be 4.8)
luarocks install luabitop
luarocks install MobDebug

remember to install cudnn 

find / -name libcudnn* 

debug插件
lua -e "require('mobdebug').listen()"

SETB %FILE% %LINE%  #Sets breakpoint
DELB %FILE% %LINE% #Delete breakpoint
SETW %EXPRESSION% #Sets a watcher (gives the result of an expression)
DELW %EXPRESSION% #Deletes a watcher
DONE #Finish debugging
EXIT #Finish debugging and quit

RUN #Runs the program?
SUSPEND #Does nothing?

EXEC %CHUNK% #?
OVER #?
OUT #?
BASEDIR %DIRECTORY% #?
STACK #?
OUTPUT %STREAM% %MODE% #?
LOAD %SIZE% %NAME% #?
