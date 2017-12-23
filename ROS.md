# Beginner Level
## Navigating the file system
```
rospack find [package_name]
roscd [locationname[/subdir]]
rosls [locationname[/subdir]]
rosed [package_name] [filename]
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

* Note: If you still see former node in the list, it might mean that you stopped the node in the terminal using ctrl-C instead of closing the window, or that you don't have the `$ROS_HOSTNAME` environment variable defined as described in [Network Setup - Single Machine](http://wiki.ros.org/ROS/NetworkSetup#Single_machine_configuration) Configuration. You can try cleaning the rosnode list with: $ rosnode cleanup

## Understanding ROS Topics
Install the rqt-graph
```shell
$ sudo apt-get install ros-<distro>-rqt
$ sudo apt-get install ros-<distro>-rqt-common-plugins
$ rosrun rqt_graph rqt_graph
```
Find the detail of the topic
```
rostopic -h
    rostopic bw     display bandwidth used by topic
    rostopic echo   print messages to screen
    rostopic hz     display publishing rate of topic    
    rostopic list   print information about active topics
    rostopic pub    publish data to topic
    rostopic type   print topic type
```
publishes data on to a topic currently advertised
```shell
rostopic pub [topic] [msg_type] [args]
```
e.g.
```
once:
$ rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
repeatedly:
$ rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]'
```

## Understanding ROS Services and Parameters
### `rosservice` allows nodes to send a request and receive a response:
```
rosservice list         print information about active services
rosservice call         call the service with the provided args
rosservice type         print service type
rosservice find         find services by service type
rosservice uri          print service ROSRPC uri
```
Example
```shell
$ rosservice type /spawn | rossrv show
$ rosservice call /spawn 2 2 0.2 ""
```
### <i>rosparam</i> allows you to store and manipulate data on the ROS Parameter Server.
```
rosparam set            set parameter
rosparam get            get parameter
rosparam load           load parameters from file
rosparam dump           dump parameters to file
rosparam delete         delete parameter
rosparam list           list parameter names
```
Example
```shell
$ rosparam set /background_r 150
$ rosservice call /clear
```
Save and load param
```
rosparam dump [file_name] [namespace]
rosparam load [file_name] [namespace]
$ rosparam dump params.yaml
```

## Using rqt_console and roslaunch
Install the dependencies
```
sudo apt-get install ros-<distro>-rqt ros-<distro>-rqt-common-plugins ros-<distro>-turtlesim
```
### rqt_console
`rqt_console`attaches to ROS's logging framework to display output from nodes. 
`rqt_logger_level`allows us to change the verbosity level (DEBUG, WARN, INFO, and ERROR) of nodes as they run.
```shell
$ rosrun rqt_console rqt_console
$ rosrun rqt_logger_level rqt_logger_level
```
### roslaunch
roslaunch starts nodes as defined in a launch file.
```shell
roslaunch [package] [filename.launch]
```
An example of launch file
```
<launch>

  <group ns="turtlesim1">
    <node pkg="turtlesim" name="sim" type="turtlesim_node"/>
  </group>

  <group ns="turtlesim2">
    <node pkg="turtlesim" name="sim" type="turtlesim_node"/>
  </group>

  <node pkg="turtlesim" name="mimic" type="mimic">
    <remap from="input" to="turtlesim1/turtle1"/>
    <remap from="output" to="turtlesim2/turtle1"/>
  </node>

</launch>
````


