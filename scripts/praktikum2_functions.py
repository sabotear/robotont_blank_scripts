#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

velocity_publisher = rospy.Publisher(
    '/robotont/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()


def closing():
    # After the loop, stops the robot
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    # Force the robot to stop
    velocity_publisher.publish(vel_msg)

#######################
# YOUR FUNCTIONS HERE #
#######################

def forward(speed,duration):
    for i in range(0,duration):
        vel_msg.linear.x = speed
        vel_msg.linear.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def turning(speed,duration):
    for i in range(0,duration):
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.angular.z = speed
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def side(speed,duration):
    for i in range(0,duration):
        vel_msg.linear.x = 0
        vel_msg.linear.y = speed
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def drive(x,y,z,duration):
    for i in range(0,duration):
        vel_msg.linear.x = x
        vel_msg.linear.y = y
        vel_msg.angular.z = z
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def loop():
    drive(0,0.8,1.6,20)

def move_turning():
    drive(0.5,0,0.8,20)

def figure_eight():
    drive(0.4,0,1,55)
    drive(0.5,0,0,15)
    drive(0.4,0,-1,55)
    drive(0.5,0,0,15)

###########################
# YOUR FUNCTIONS HERE END #
###########################


def move():
    # Starts a new node
    rospy.init_node('robotont_velocity_publisher', anonymous=True)

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        ########################
        # YOUR CODE HERE START #
        ########################
        figure_eight()
        ######################
        # YOUR CODE HERE END #
        ######################


if __name__ == '__main__':
    try:
        rospy.on_shutdown(closing)
        move()
    except rospy.ROSInterruptException:
        pass
