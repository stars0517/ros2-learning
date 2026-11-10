from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demo1_cpp',
            executable='my_node',  # 这里必须和你 CMakeLists 里起的名字一模一样！
            name='hello_node',
            output='screen'
        )
    ])