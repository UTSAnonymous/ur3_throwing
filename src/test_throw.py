#!/usr/bin/env python
import rospy
import time
import roslib; roslib.load_manifest('ur_driver')
import actionlib
from control_msgs.msg import *
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from sensor_msgs.msg import JointState
from math import *

JOINT_NAMES = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint',
               'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']

STARTING_POSITION = [radians(90), radians(-135), radians(-70), radians(-100), radians(90), 0]
#STARTING_POSITION = [radians(90), radians(-100), radians(-70), radians(-100), radians(0), 0]

client = None
joint_speed_pub = None
trajectory = JointTrajectory()

"""
def ThrowTrajectory_movement():

	rate = rospy.Rate(130)
	trajectory = JointTrajectory()

	trajectory.header.stamp=rospy.Time.now()
	trajectory.joint_names = JOINT_NAMES

	count = 0
	i = 0

	# working speed = 2, wrist_speed = 1.5
	# working speed = 2.5, wrist_speed = 2
	# working speed = 3, wrist_speed = 2.5
	# working speed = 4.5, wrist_speed = 2.5

	speed = 4.5
	wrist_speed = 2.5

	while True:
		if count < 100:
			trajectory.points = [JointTrajectoryPoint(positions=[0]*6, velocities=[0, 0, wrist_speed, speed, 0, 0])]
		else:
			speed -= 0.06
			if wrist_speed > 0.04:
				wrist_speed -= 0.04
			else:
				wrist_speed = 0
			trajectory.points = [JointTrajectoryPoint(positions=[0]*6, velocities=[0, 0, wrist_speed, speed, 0, 0])]
		joint_speed_pub.publish(trajectory)
		count += 1

	  	if speed < 0.05:
			break

        rate.sleep()

def BackHandThrowTrajectory():

	rate = rospy.Rate(130)
	trajectory = JointTrajectory()

	trajectory.header.stamp=rospy.Time.now()
	trajectory.joint_names = JOINT_NAMES

	count = 0

	speed = -2
	wrist_speed = -1.5

	while True:
		if count < 300:
			trajectory.points = [JointTrajectoryPoint(positions=[0]*6, velocities=[0, 0, wrist_speed, speed, 0, 0])]
		else:
			speed += 0.06
			if wrist_speed < -0.04:
				wrist_speed += 0.04
			else:
				wrist_speed = 0
			trajectory.points = [JointTrajectoryPoint(positions=[0]*6, velocities=[0, 0, wrist_speed, speed, 0, 0])]
		joint_speed_pub.publish(trajectory)
		count += 1

	  	if speed > -0.05:
			break

        rate.sleep()
"""

def MoveToStartPosition():
    global joints_pos
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    try:
        joint_states = rospy.wait_for_message("joint_states", JointState)
        joints_pos = joint_states.position
        g.trajectory.points = [
        JointTrajectoryPoint(positions=joints_pos, velocities=[0]*6, time_from_start=rospy.Duration(3.0)),
        JointTrajectoryPoint(positions=STARTING_POSITION ,velocities=[0]*6, time_from_start=rospy.Duration(6.0))]

        client.send_goal(g)
        client.wait_for_result()
    except:
        raise

def ThrowTrajectory(rate):
    trajectory.header.stamp=rospy.Time.now()
    trajectory.joint_names = JOINT_NAMES

    count = 0
    i = 0
    speed = 1.5
    wrist_speed = 2

    while True:
        if count < 100:
            trajectory.points = [JointTrajectoryPoint(positions=[0]*6, velocities=[0, 0, wrist_speed, speed, 0, 0])]
        else:
            speed -= 0.04
            if wrist_speed > 0.04:
                wrist_speed -= 0.04
            else:
                wrist_speed = 0
            trajectory.points = [JointTrajectoryPoint(positions=[0]*6, velocities=[0, 0, wrist_speed, speed, 0, 0])]
        joint_speed_pub.publish(trajectory)
        count += 1

        if speed < 0.05:
            break

        rate.sleep()

def main():
    global client, joint_speed_pub

    # create node
    rospy.init_node("throwing_trajectory_planning", anonymous=True, disable_signals=True)

    # create the client to move the arm to the starting position
    client = actionlib.SimpleActionClient('follow_joint_trajectory', FollowJointTrajectoryAction)

    print("Waiting for server...")
    client.wait_for_server()
    print("Connected to server")

    # create publisher to publish to the ur_driver/joint_speed
    joint_speed_pub = rospy.Publisher('ur_driver/joint_speed',JointTrajectory, queue_size=30)
    rate = rospy.Rate(125)

    #---------------Moving the arm------------------#
    MoveToStartPosition()

    time.sleep(3)

    #ThrowTrajectory(rate)


if __name__ == '__main__': main()
