#!/usr/bin/env python

###Random exploration for jackal robot


#additional imports
import rospy
from geometry_msgs.msg import Twist
import random
import sys
import threading

class velo_publisher():
    def __init__(self, topic):
        rospy.init_node('random_explore')
        self.pub = rospy.Publisher(topic, Twist, queue_size=10)
        self.vel_msg=Twist()
        self.vel_msg.linear.x = 0
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0
        self.reset_time=3.0

    def publish(self):
        # self.vel_msg.linear.x = random.random()
        # self.vel_msg.angular.z = random.uniform(-1, 1)
        self.pub.publish(self.vel_msg)

    def reset_var(self):
        #resets variables randomly after 
        self.vel_msg.linear.x = 0.5 #random.random()
        self.vel_msg.angular.z = random.uniform(-1, 1)
        threading.Timer(self.reset_time, self.reset_var).start()

if __name__ == '__main__':
    try:
        ns=sys.argv[1]
        topic=ns+"/cmd_vel"
        vp = velo_publisher(topic)
        vp.reset_var()
        while True:
            vp.publish()
            rospy.sleep(0.2)

    except rospy.ROSInterruptException or KeyboardInterrupt: pass

