
### Install torch7 from github
```
git clone https://github.com/torch/distro.git ~/torch --recursive
cd ~/torch; bash install-deps;
./install.sh
```
### Install other dependency
```
sudo apt-get install libprotobuf-dev protobuf-compiler
```
### Install cuda for torch
```
luarocks install cutorch
luarocks install cunn
```
### Install HDF5
```
sudo apt-get install libhdf5-serial-dev hdf5-tools
git clone https://github.com/deepmind/torch-hdf5
cd torch-hdf5
luarocks make hdf5-0-0.rockspec LIBHDF5_LIBDIR="/usr/lib/x86_64-linux-gnu/"
```
### Install cudnn 6.0 for torch

```
git clone https://github.com/soumith/cudnn.torch -b R6
cd cudnn.torch
luarocks make
```


### Other problems
If there are some errors about `CUDNN_STATUS_INTERNAL_ERROR`, try
```
sudo rm -rf ~/.nv
```

[Reference1](http://blog.csdn.net/hungryof/article/details/51557666)