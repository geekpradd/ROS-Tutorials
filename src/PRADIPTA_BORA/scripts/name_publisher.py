#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def name_publisher():
	pub = rospy.Publisher("name_listener", String, queue_size=10)
	rospy.init_node("name_publisher")
	rate = rospy.Rate(5)
	while not rospy.is_shutdown():
		name = "Pradipta Bora"
		rospy.loginfo(name)
		pub.publish(name)
		rate.sleep()

if __name__ == '__main__':
	try:
		name_publisher()
	except rospy.ROSInterruptException:
		pass

