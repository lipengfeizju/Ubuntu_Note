# Edit some config files
sudo vi /etc/modprobe.d/blacklist-nouveau.conf
>blacklist nouveau
>
>blacklist lbm-nouveau
>
>options nouveau modeset=0
>
>alias nouveau off
>
>alias lbm-nouveau off

sudo vi /etc/modprobe.d/nouveau-kms.conf
>options nouveau modeset=0
sudo update-initramfs -u
# Install new cores
```shell
sudo apt-get install build-essential
sudo apt-get install linux-source
sudo apt-get install linux-headers-4.4.0-101-generic
sudo apt-get install linux-images-4.4.0-101-generic
sudo apt-get install linux-image-4.4.0-101-generic
sudo reboot
```
# Stop the grphic interface
sudo service lightdm stop
 
sudo chmod 777 cuda_8.0.61_375.26_linux-run 
# Run the compiled source-code
sudo ./cuda_8.0.61_375.26_linux-run --no-opengl-lib --kernel-source-path=/usr/src/linux-headers-4.4.0-101-generic

sudo service lightdm start
# Install a new driver
sudo apt-get install nvidia-367

# Edit Path Value
sudo gedit ~/.bashrc
>export PATH=/usr/local/cuda-8.0/bin:$PATH
>
>export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64
>
>export CUDA_HOME=/usr/local/cuda-8.0

# step 3: install the cudnn
tar xf cudnn-8.0-linux-x64-v6.0.tgz
cd cuda/include
sudo cp cudnn.h /usr/local/cuda/include/
cd ..
cd /lib64
sudo cp lib* /usr/local/cuda/lib64/
sudo rm -rf libcudnn.so libcudnn.so.6
sudo ln -s libcudnn.so.6.0.21 libcudnn.so.6
sudo ln -s libcudnn.so.6 libcudnn.so


# If there are some problems when running the cudnn, please try:
[Reference1](http://blog.csdn.net/hungryof/article/details/51557666)

A good [tutorial](https://web.stanford.edu/class/cs20si/syllabus.html) in tensorflow and deep learning
