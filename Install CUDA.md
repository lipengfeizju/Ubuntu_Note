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

#Edit Path Value
sudo gedit ~/.bashrc
>export PATH=/usr/local/cuda-8.0/bin:$PATH
>
>export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64
>
>export CUDA_HOME=/usr/local/cuda-8.0

A good [tutorial](https://web.stanford.edu/class/cs20si/syllabus.html) in tensorflow and deep learning