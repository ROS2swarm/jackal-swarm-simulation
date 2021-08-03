# multi_jackal_simulation_rob
Multi Jackal Simulation from University of Luebeck

## 1. Install ROS kinetic or melodic
For kinetic follow: http://wiki.ros.org/kinetic/Installation/Ubuntu
For meldoic follow: http://wiki.ros.org/melodic/Installation/Ubuntu
## 2. Install additional Jackal packages
```
sudo apt-get install ros-kinetic-jackal-simulator ros-kinetic-jackal-desktop ros-kinetic-jackal-navigation
```
or
```
sudo apt-get install ros-melodic-jackal-simulator ros-melodic-jackal-desktop ros-melodic-jackal-navigation
```

## 3. Create catkin workspace
In your home folder open a terminal and create your workspace:
```
mkdir catkin_ws
cd catkin_ws
mkdir src
cd src
```

## 4. Clone repos
Clone following repos into your src folder
```
git clone https://github.com/l-schilling/multi_jackal_simulation_rob.git
git clone https://github.com/wilselby/ouster_example
```

## 5. Build your workspace
```
cd ..
catkin_make
```

If needed source your workspace (in your catkin_ws: source devel/setup.bash)

## 6. Run simulation
```
roslaunch multi_jackal_base two_jackal.launch
```


ZED Camera currently not supported in Gazebo.
For a quick fix you can change the argument config in the file base_jackal.launch to "front_bumblebee2"
