#! /usr/bin/env python3
#指定解释器路径

#1.导包
import rclpy
from rclpy.node import Node

#2.编写主入口
def main(args=None):
    #3.初始化ROS节点
    rclpy.init(args=args)
    #创建节点对象
    node = Node("hello")

    #4.输出日志
    node.get_logger().info("Hello ROS2!")

    #保持节点运行
    rclpy.spin(node)

    #关闭节点
    node.destroy_node()
    #关闭ROS客户端库
    rclpy.shutdown()

#5.判断是否是主程序入口
if __name__ == '__main__':
    main()


#修改setup.py文件，添加入口点
#entry_points={
#        'console_scripts': [
#            'hello = demo1_py.hello:main',
#        ],


#编译并运行
#colcon build --packages-select demo1_py
#source install/setup.bash
#ros2 run demo1_py hello