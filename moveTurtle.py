#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist

def moveTurtle():
    
    # Initialize node
    rospy.init_node('moveTurtle', anonymous=True)
    velPub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    # Initialize Twist msg object
    velFwd = Twist()
    velFwd.linear.x = 1
    velFwd.linear.y = 0
    velFwd.linear.z = 0
    velFwd.angular.x = 0
    velFwd.angular.y = 0
    velFwd.angular.z = 0

    velTrn = Twist()
    velTrn.linear.x = 0
    velTrn.linear.y = 0
    velTrn.linear.z = 0
    velTrn.angular.x = 0
    velTrn.angular.y = 0
    velTrn.angular.z = 0.5

    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        
        i = 0
        while i < 4:
            velPub.publish(velFwd)
            i=i+1

        j = 0
        while j < 2:
            velPub.publish(velTrn)
            j=j+1
        
        rate.sleep()

if __name__ == '__main__':
    try:
        moveTurtle()
    except rospy.ROSInterruptException:
        pass
