#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
# from ros_gz_bridge.actions import RosGzBridge

def generate_launch_description():
	bridge_params = os.path.join(
	    "/home/snkt/ros2_ws/src/mavros/mavros/config",
	    'cam.yaml'
	)

	start_gazebo_ros_bridge_cmd = Node(
	    package='ros_gz_bridge',
	    executable='parameter_bridge',
	    arguments=["/camera/image_raw@sensor_msgs/msg/Image@gz.msgs.Image",
	    			"/camera/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo",
	    			"/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock"],
	    output='screen',
	)

	ld = LaunchDescription()

	ld.add_action(start_gazebo_ros_bridge_cmd)
	return ld