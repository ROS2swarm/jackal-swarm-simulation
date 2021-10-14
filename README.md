**ROS2Swarm Jackal Extension Simulation**

Simulation Environment from [Lars Schilling](https://github.com/l-schilling/multi_jackal_simulation_rob)   
Follow Instructions, leave multi_jackal_simulation out     
Clone multi_jackal_simulation here       

catkin_make   

Run Jackal_launch_multi.launch.py with argument of amount of robots



To run with the swarm package:

Install [ROS bridge](https://github.com/ros2/ros1_bridge)
Make sure to source ROS versions directly and not have anything sourced preciously from the .bashrc. Especially with the setup.bash of the swarm package problems can occur.

Run the ROS bridge. The Run2.sh script can be used for that.
```cd ros-bridge bash Run2.sh```

Start the Jackal Simulation with the number of robots as an argument    
``python2 Jackal_launch_multi.launch.py 5``

Run the ROS2Swarm package with -v 1 argument in the restart.sh script
