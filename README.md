## ROS2Swarm Jackal Extension Simulation

**To run the simulation:**    
Simulation Environment from [Lars Schilling](https://github.com/l-schilling/multi_jackal_simulation_rob) and adapted

Install Jackal packages and pointcloud_to_laserscan package:
```
sudo apt-get install ros-melodic-jackal-simulator ros-melodic-jackal-desktop ros-melodic-jackal-navigation ros-melodic-pointcloud-to-laserscan
```
Clone ouster_examples and this repo into catkin_ws/src:
```
git clone https://github.com/wilselby/ouster_example
git clone https://gitlab.iti.uni-luebeck.de/plattenteich/jackal-swarm-addition.git
```
Build:
```
cd catkin_ws
catkin_make   
```
Run Jackal_launch_multi.launch.py with amount of robots:
```
python2 Jackal_launch_multi.launch.py 5
```

**To run with the swarm package:**

Install [ROS bridge](https://github.com/ros2/ros1_bridge) either from source or binaries:
```
sudo apt install ros-dashing-ros1-bridge
```
Make sure to source ROS versions directly and not have anything sourced preciously from the .bashrc. 

Run the ROS bridge. The Run2.sh script can be used for that. It starts the master and the bridge in separate terminals and takes care of sourcing the ROS distros.
```
bash Run2.sh
```

Start the Jackal Simulation with the number of robots as an argument    
```
python2 Jackal_launch_multi.launch.py 5
```

Run the ROS2Swarm package with -v 1 argument in the restart.sh script and the correct amount of robots from the simulation.

To turn on LIDAR visualisation change visualize tag of LIDAR in OS1-64urdf.xacro to true
