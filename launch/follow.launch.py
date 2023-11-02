from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, LogInfo

def generate_launch_description():
    oak_detect_node = Node(
            package="mini_pupper_follow",
            namespace="",
            executable="oak_detect",
            name="oak_detect",
        )
    return LaunchDescription([
	    oak_detect_node
    ])
