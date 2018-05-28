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
