```shell
# export lib for CUDA
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:/home/lipengfei/torch/install/lib/:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/:$LD_LIBRARY_PATH

#include torch
. /home/lipengfei/torch/install/bin/torch-activate


# source for ros
source /opt/ros/kinetic/setup.bash
source /media/harddrive/github/Onging/catkin_ws_pengfei/devel/setup.bash

# export ORB-SLAM2 Package
export ROS_PACKAGE_PATH=/media/harddrive/github/Onging/Object-SLAM/Examples/ROS:$ROS_PACKAGE_PATH;

# export PYTHON packages for SSD
export HOME_SSD=/media/harddrive/github/caffe_ssd
export PYTHONPATH=$HOME_SSD/python:$PYTHONPATH

#alias rm='echo "Pleas use "trash"!!!"'

# TeX Live 2015
PATH=/usr/local/texlive/2017/bin/x86_64-linux:$PATH; export PATH
MANPATH=/usr/local/texlive/2017/texmf-dist/doc/man:$MANPATH; export MANPATH
INFOPATH=/usr/local/texlive/2017/texmf-dist/doc/info:$INFOPATH; export INFOPATH

# Include Matlab Runtime Dir
#export LD_LIBRARY_PATH=/media/harddrive/Matlab/MATLAB_Runtime/v901/runtime/glnxa64:$LD_LIBRARY_PATH;

# Include ORB-SLAM-ros Package
export ROS_PACKAGE_PATH=/media/harddrive/github/OpenSource/ROS_PACKAGE/orb_slam_ros:$ROS_PACKAGE_PATH;
#Include ROS_KITTI
export ROS_PACKAGE_PATH=/media/harddrive/github/OpenSource/ROS_PACKAGE/ROS_KITTI:$ROS_PACKAGE_PATH;

# export JAVA home
export JAVA_HOME=/opt/jvm/jdk1.8.0_151
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH

# export Android home
export ANDROID_HOME=/home/lipengfei/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools/
export PATH=$PATH:$ANDROID_HOME/platform-tools/ 


export DEMON_DIR=/media/harddrive/github/OpenSource/demon
export PYTHONPATH=$DEMON_DIR/lmbspecialops/python:$PYTHONPATH
```

