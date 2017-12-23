# Beginner Level
## Navigating the file system
```
rospack = ros + pack(age)
roscd = ros + cd
rosls = ros + ls
```
## Creating a ROS Package
This file structure is preferred
```
workspace_folder/        -- WORKSPACE
  src/                   -- SOURCE SPACE
    CMakeLists.txt       -- 'Toplevel' CMake file, provided by catkin
    package_1/
      CMakeLists.txt     -- CMakeLists.txt file for package_1
      package.xml        -- Package manifest for package_1
    ...
    package_n/
      CMakeLists.txt     -- CMakeLists.txt file for package_n
      package.xml        -- Package manifest for package_n
```
This command is convenient to add some dependency to the package
```shell
    catkin_create_pkg <package_name> std_msgs rospy roscpp
```
Find dependency
```shell
    rospack depends1 <package_name>
```
Source the workspace
```shell
    source /opt/ros/kinetic/setup.bash
```
[Customizing the package.xml](http://wiki.ros.org/ROS/Tutorials/CreatingPackage#ROS.2BAC8-Tutorials.2BAC8-catkin.2BAC8-CreatingPackage.Customizing_the_package.xml)
```
<description>The beginner_tutorials package</description>
<buildtool_depend>catkin</buildtool_depend>
<build_depend>roscpp</build_depend>
<exec_depend>roscpp</exec_depend>
```

## Building a ROS Package
Cmake command example
```shell
# In a CMake project
$ mkdir build
$ cd build
$ cmake ..
$ make
$ make install  # (optionally)
```
An example of catkin_make
```
cd ~/catkin_ws/
catkin_make
```
## Understanding ROS Nodes
```
rosnode list
rosnode info <node_name>
rosrun [package_name] [node_name]
rosrun [package_name] [node_name] __name:=[your name]
rosnode ping <node_name>
```

* Note: If you still see former node in the list, it might mean that you stopped the node in the terminal using ctrl-C instead of closing the window, or that you don't have the $ROS_HOSTNAME environment variable defined as described in [Network Setup - Single Machine](http://wiki.ros.org/ROS/NetworkSetup#Single_machine_configuration) Configuration. You can try cleaning the rosnode list with: $ rosnode cleanup

