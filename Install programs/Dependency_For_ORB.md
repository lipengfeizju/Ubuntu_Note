## Install `Eigen3`
```
sudo apt-get install libeigen3-dev
sudo cp -r  /usr/include/eigen3/Eigen  /usr/local/include/
sudo cp -r  /usr/include/eigen3/unsupported/ /usr/local/include/
```
## Install `OpenCV 2`
```
sudo apt-get install build-essential libgtk2.0-dev libavcodec-dev libavformat-dev libjpeg62-dev libtiff5-dev cmake libswscale-dev libjasper-dev
mkdir build
cmake -j8 ..
make -j8
sudo make install
```
## Install GLEW
```
sudo apt-get install libglew-dev
```
## install [Pangolin](https://github.com/stevenlovegrove/Pangolin)
```
git clone https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
mkdir build
cd build
cmake ..
cmake --build .
```
## Install ROS
### Setup your sources.list and list
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo proxy apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
```
### Installation
```
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
apt-cache search ros-kinetic
```


### Initialize rosdep
```
sudo rosdep init
rosdep update
```
### Evironment Setup
```
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential
```
## Final Steps
```
sudo apt-get install clang
echo "export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:/media/harddrive/github/Onging/Object-SLAM/Examples/ROS" >> ~/.bashrc
chmod +x build_ros.sh build.sh
./build.sh
./build_ros.sh
```
#### KITTI example
```
./Examples/Monocular/mono_kitti Vocabulary/ORBvoc.txt Examples/Monocular/KITTI00-02.yaml /media/harddrive/dataset/KITTI/dataset/sequences/01
```
#### Ros Example
```
rosrun ORB_SLAM2 Mono Vocabulary/ORBvoc.txt  Examples/Monocular/KITTI00-02.yaml 
rosrun ORB_SLAM2 Convert
```
### Some possible problems
* Opencv errore, add these lines to `build*.sh`
```
-DROS_BUILD_TYPE=Release -DCUDA_USE_STATIC_CUDA_RUNTIME=false
```
* Errors like ` _ZN5boost6system15system_categoryEv`
Please edit Cmake file
```
find_package( Boost COMPONENTS thread system filesystem REQUIRED ) #whatever libs you need
include_directories( ${Boost_INCLUDE_DIRS} )
find_package( Threads )

set( LIBS_TO_LINK
    ${Boost_LIBRARIES}
    ${CMAKE_THREAD_LIBS_INIT}
)

target_link_libraries( myApp
    ${LIBS_TO_LINK}
)
```
## If you are using ORB-SLAM1
### Solve the undefined `FAST` algorithm
```
#include <opencv2/opencv.hpp>
```
### Some error about `Eigen`
```
error: ‘YOU_MIXED_DIFFERENT_NUMERIC_TYPES__YOU_NEED_TO_USE_THE_CAST_METHOD_OF_MATRIXBASE_TO_CAST_NUMERIC_TYPES_EXPLICITLY’ is not a member of ‘Eigen::internal::static_assertion<false>
```
Use this link to [download](https://launchpad.net/ubuntu/trusty/amd64/libeigen3-dev/3.2.0-8) the former version
Then follow the above-mentioned steps 

### Some errors abour `Opencv`
some possible solutions

change link_libraries
```
target_link_libraries(
'''
${OpenCV_LIBRARIES} 
'''
)
```
Set opencv DIR
```
set ( OpenCV_DIR   "/media/harddrive/software/opencv-2.4.13.4/build")
find_package(OpenCV REQUIRED)
```
If you encounter `No rule to make target 'opencv_calib3d-NOTFOUND', needed by '../devel/lib/cv_pose/cv_qt_ros'`
It is caused by the opencv 3 in ROS couldn't be found in this way.
Try to modify the `/opt/ros/kinetic/share/OpenCV-3.3.1/OpenCVConfig.cmake`
```
...
#set(OpenCV_LIBS ${OpenCV_LIBS} "${__cvcomponent}")
set(OpenCV_LIBS ${OpenCV_LIBS} "${OpenCV_INSTALL_PATH}/lib/lib${__cvcomponent}3.so")
...
```
If you want to build this in Cmake instead of rosbuild, you should comment all the `rosbuild` args
then add this
```
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  cv_bridge
  image_transport
  sensor_msgs
  pcl_conversions
  pcl_ros
)
```
[reference1](https://github.com/raulmur/ORB_SLAM2)
[reference2](https://stackoverflow.com/questions/13919128/cmake-set-linker-flags-for-boost)
