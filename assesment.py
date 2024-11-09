import rospy
from geometry_msgs.msg import Twist
import time

def move_turtle():
    # Initialize the ROS node
    rospy.init_node('move_turtle_in_rectangle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Create the Twist message for velocity commands
    move_cmd = Twist()
    rate = rospy.Rate(1)

    # Define rectangle dimensions (length, width)
    length = 4.0
    width = 2.0

    while not rospy.is_shutdown():
        # Move in a straight line (forward)
        move_cmd.linear.x = 2.0  # Set speed
        move_cmd.angular.z = 0.0  # No turning
        pub.publish(move_cmd)
        time.sleep(length / 2.0)  # Time to travel the length
        
        # Stop and wait
        move_cmd.linear.x = 0.0
        pub.publish(move_cmd)
        time.sleep(1)

        # Turn 90 degrees to change direction
        move_cmd.angular.z = 1.57  # 90 degrees in radians
        pub.publish(move_cmd)
        time.sleep(1)

        # Move in a straight line (width)
        move_cmd.linear.x = 2.0
        move_cmd.angular.z = 0.0
        pub.publish(move_cmd)
        time.sleep(width / 2.0)  # Time to travel the width
        
        # Stop and wait
        move_cmd.linear.x = 0.0
        pub.publish(move_cmd)
        time.sleep(1)

        # Turn 90 degrees to change direction
        move_cmd.angular.z = 1.57
        pub.publish(move_cmd)
        time.sleep(1)

        # Repeat the process for the rectangular path
        move_cmd.angular.z = 0.0
        pub.publish(move_cmd)

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
