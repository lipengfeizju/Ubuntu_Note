# Install `CAFFE` from github

### Install dependency
```shell
sudo apt-get install libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler 
sudo apt-get install --no-install-recommends libboost-all-dev
sudo apt-get install libopenblas-dev liblapack-dev libatlas-base-dev
sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev
```
### Clone the project
```
git clone https://github.com/BVLC/caffe.git
```
### Edit Makefile.config
```
USE_CUDNN := 1
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial
LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/hdf5/serial      
```
### Edit Makefile
```
NVCCFLAGS += -D_FORCE_INLINES -ccbin=$(CXX) -Xcompiler -fPIC $(COMMON_FLAGS)
```
### Final steps
To crack the limitation in caffe, comment this line in `/usr/local/cuda/include/host_config.h `
```shell
//#error-- unsupported GNU version! gcc versions later than 4.9 are not supported!
```
If it reports some errors like this, "libcudart.so.8.0 cannot open shared object file: No such file or directory", then try these commands
```
# pay attention to your version of CUDA
sudo cp /usr/local/cuda-8.0/lib64/libcudart.so.8.0 /usr/local/lib/libcudart.so.8.0 && sudo ldconfig
sudo cp /usr/local/cuda-8.0/lib64/libcublas.so.8.0 /usr/local/lib/libcublas.so.8.0 && sudo ldconfig
sudo cp /usr/local/cuda-8.0/lib64/libcurand.so.8.0 /usr/local/lib/libcurand.so.8.0 && sudo ldconfig
```
Make `caffe` and run the test
```shell
make all -j8
sudo make runtest
```
If you encounter some errors like `'google::protobuf::Message::DebugString[abi:cxx11]() const' undefined`
Please try this:

**Notice: DO NOT download the newest version from the github, it won't work now**
```shell
wget https://github.com/google/protobuf/releases/download/v2.6.1/protobuf-2.6.1.tar.gz
tar -zxvf protobuf-2.6.1.tar.gz
cd protobuf-2.6.1/
./configure
make
make check
sudo make install
```

### Other possible Solutions
You can try to downgrade the g++ and gcc, but it doesn't work currently
```shell
cd /usr/bin/
sudo rm gcc
sudo ln -s gcc-4.9 gcc
sudo rm g++
sudo ln -s g++-4.9 g++
cd /media/harddrive/github/caffe/
```
You can also try this in CMAKE, but it is not the key problem currently.
```shell
add_definitions(-D_GLIBCXX_USE_CXX11_ABI=0)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D_FORCE_INLINES")
```

### References


[Reference1](http://blog.csdn.net/xuzhongxiong/article/details/52717285)

[Reference2](https://github.com/BVLC/caffe/issues/4949#issuecomment-258510439)

[Reference3](http://blog.csdn.net/blue_it/article/details/53996216)

[Reference4](http://coldmooon.github.io/2015/07/09/caffe/)
