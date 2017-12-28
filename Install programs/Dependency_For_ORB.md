## Install `Eigen3`
sudo apt-get install libeigen3-dev
sudo cp -r  /usr/include/eigen3/Eigen  /usr/local/include/
sudo cp /usr/local/include/eigen3/unsupported/ /usr/local/include/
## Install `OpenCV 2`
sudo apt-get install build-essential libgtk2.0-dev libavcodec-dev libavformat-dev libjpeg62-dev libtiff5-dev cmake libswscale-dev libjasper-dev

mkdir build
cmake -j8 ..
make -j8
sudo make install


sudo apt-get install libglew-dev
mkdir build
cd build
cmake ..
cmake --build .


## Setup your sources.list and list
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo proxy apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
## Installation
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
apt-cache search ros-kinetic

## Initialize rosdep
sudo rosdep init
rosdep update

## Evironment Setup
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential



sudo apt-get install clang
