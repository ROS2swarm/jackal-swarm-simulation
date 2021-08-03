import roslaunch
import sys
import time

# start gazebo
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
cli_args = ['/home/user/catkin_ws/src/launch_jackal_gazebo/launch/jackal.launch']
roslaunch_args = cli_args[1:]
roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], roslaunch_args)]
gazebo = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_file)
gazebo.start()
time.sleep(3)

# spawn jackals
roslaunch_files = []
for num in range(0, int(sys.argv[1])):
    cli_args = ['/home/user/catkin_ws/src/multi_jackal_simulation_rob/multi_jackal_base/launch/base_jackal.launch',
                'ns:=robot_namespace_' + str(num), 'y:='+str(num)]
    roslaunch_args = cli_args[1:]
    node = roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], roslaunch_args
    roslaunch_files.append(node)

parent = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_files)
parent.start()

try:
    parent.spin()
finally:
    parent.shutdown()



   

