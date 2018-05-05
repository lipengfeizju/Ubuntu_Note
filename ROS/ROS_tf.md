

# 1. TF in Python


### 1) Writing a tf broadcaster
``` Python
#!/usr/bin/env python  

import rospy
import tf
import turtlesim.msg

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')# node name
    turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/%s/pose' % turtlename,turtlesim.msg.Pose,
                     handle_turtle_pose,turtlename)#callback function
    rospy.spin()
```

### 2) Writing a tf listener
```python
#!/usr/bin/env python  
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')
    listener = tf.TransformListener()
    # Other items ...
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        #To Do ...
        rate.sleep()
```

### 3) Wait for transforms
When a broadcaster sends out a transform, it takes some time before that transform gets into the buffer (usually a couple of milliseconds). So, when you request a frame transform at time "now", you should wait a few milliseconds for that information to arrive. 

```Python
    listener.waitForTransform("/turtle2", "/carrot1", rospy.Time(), rospy.Duration(4.0))
    while not rospy.is_shutdown():
        try:
            now = rospy.Time.now()
            listener.waitForTransform("/turtle2", "/carrot1", now, rospy.Duration(4.0))
            (trans,rot) = listener.lookupTransform("/turtle2", "/carrot1", now)
```

### 4)Advanced API for lookupTransform
The advanced API for lookupTransform() takes six arguments:

    1. Give the transform from this frame,
    2. at this time ...
    3. ... to this frame,
    4. at this time.
    5. Specify the frame that does not change over time, in this case the "/world" frame, and 
    6. the variable to store the result in. 

```Python
        try:
            now = rospy.Time.now()
            past = now - rospy.Duration(5.0)
            listener.waitForTransformFull("/turtle2", now,
                                      "/turtle1", past,
                                      "/world", rospy.Duration(1.0))
            (trans, rot) = listener.lookupTransformFull("/turtle2", now,
                                      "/turtle1", past,
                                      "/world")
```



# TF in C++

### 1) Writing a tf broadcaster
``` C++
#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <turtlesim/Pose.h>

std::string turtle_name;

void poseCallback(const turtlesim::PoseConstPtr& msg){
  static tf::TransformBroadcaster br;
  tf::Transform transform;
  transform.setOrigin( tf::Vector3(msg->x, msg->y, 0.0) );
  tf::Quaternion q;
  q.setRPY(0, 0, msg->theta);
  transform.setRotation(q);
  br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "world", turtle_name));
}

int main(int argc, char** argv){
  ros::init(argc, argv, "my_tf_broadcaster");
  if (argc != 2){ROS_ERROR("need turtle name as argument"); return -1;};
  turtle_name = argv[1];

  ros::NodeHandle node;
  ros::Subscriber sub = node.subscribe(turtle_name+"/pose", 10, &poseCallback);

  ros::spin();
  return 0;
};

```

### 2) Writing a tf listener
``` C++
#include <ros/ros.h>
#include <tf/transform_listener.h>

int main(int argc, char** argv){
  ros::init(argc, argv, "my_tf_listener");
  ros::NodeHandle node;

  tf::TransformListener listener;

  ros::Rate rate(10.0);
  while (node.ok()){
    tf::StampedTransform transform;
    try{
      listener.lookupTransform("/turtle2", "/turtle1",  
                               ros::Time(0), transform);
    }
    catch (tf::TransformException ex){
      ROS_ERROR("%s",ex.what());
      ros::Duration(1.0).sleep();
    }
    //To Do ...
    rate.sleep();
  }
  return 0;
};
```

### 3) Wait for transforms
When a broadcaster sends out a transform, it takes some time before that transform gets into the buffer (usually a couple of milliseconds). So, when you request a frame transform at time "now", you should wait a few milliseconds for that information to arrive. 

```C++
 try{
    ros::Time now = ros::Time::now();
    listener.waitForTransform("/turtle2", "/turtle1",
                              now, ros::Duration(3.0));
    listener.lookupTransform("/turtle2", "/turtle1",
                             now, transform);
 }
```

### 4)Advanced API for lookupTransform
The advanced API for lookupTransform() takes six arguments:

    1. Give the transform from this frame,
    2. at this time ...
    3. ... to this frame,
    4. at this time.
    5. Specify the frame that does not change over time, in this case the "/world" frame, and 
    6. the variable to store the result in. 

```Python
    try{
        ros::Time now = ros::Time::now();
        ros::Time past = now - ros::Duration(5.0);
        listener.waitForTransform("/turtle2", now,
                                "/turtle1", past,
                                "/world", ros::Duration(1.0));
        listener.lookupTransform("/turtle2", now,
                                "/turtle1", past,
                                "/world", transform);
    }
```