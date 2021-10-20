#!/bin/bash
export ROS_MASTER_URI=http://localhost:11311  
. ~/ros1_bridge-dashing/install/setup.bash 
ros2 run ros1_bridge dynamic_bridge 
 
