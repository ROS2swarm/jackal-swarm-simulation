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

To turn on LIDAR visualisation change visualize tag of LIDAR in OS1-64urdf.xacro to true

**To run with the swarm package in simulation:**

Install [ROS bridge](https://github.com/ros2/ros1_bridge) either from source or binaries:
```
sudo apt install ros-dashing-ros1-bridge
```
Make sure to source ROS versions directly and not have anything sourced preciously from the .bashrc. 

Run the ROS bridge. The Run2.sh script can be used for that. It starts the master and the bridge in separate terminals and takes care of sourcing the ROS distros.
```
bash Master_bridge.sh
```

Start the Jackal Simulation with the number of robots as an argument    
```
python2 Jackal_launch_multi.launch.py 5
```

Run the ROS2Swarm package with -v 1 argument in the restart.sh script and the correct amount of robots from the simulation.

**To run with the swarm package on real Jackals:**     

Connect to Jackal administrator via ssh. Replace _ with Jackal identifier number.
```
ssh administrator@192.169.131.1_1
```
Install ROS2 and ROS bridge on Jackal. Follow [this](https://docs.ros.org/en/dashing/Installation/Ubuntu-Install-Debians.html) guide for ROS2.
Bridge like above.
Clone ROS2swarm repo, checkout branch JackalTests. This branch has the changes in the topic names included. 
Master on real Jackal is already started, only needed to start the bridge. Bridge.sh script included in JackalTests branch.
```
bash Bridge.sh
```
LIDAR needs to be turned on manually. All the Jackals have a os1_lidar.launch script that starts the LIDAR nodes and includes the remapping to a 2D scan. Script is on the Nvidia Jetson. Access seperately and launch script:
```
ssh nvidia@192.168.131.1_2
roslaunch os1_lidar.launch
```
IP address of LIDAR changes sometimes and the launch won't work. Check IP address of LIDAR with:
```
ping -c1 os1-[number printed on the LIDAR].local
```
and adjust in "os1_lidar.launch".

If LIDAR and the bridge are running the ROS2swarm package can be started on each Jackal.  Make sure again that -v tag is 1 and -n tag is 1 as well. Open another terminal of the administrator and run:
```
cd ROS2swarm
bash restart.sh
```

