//创建ROS功能包
//ros2 pkg create --build-type ament_cmake demo1_cpp --dependencies rclcpp std_msgs
//在src目录下创建功能包

//1.包含ROS的头文件
#include "rclcpp/rclcpp.hpp"
using namespace std;

//2.编写main函数
int main(int argc, char **argv){
    rclcpp::init(argc, argv);           //3.初始化ROS节点

    auto node = make_shared<rclcpp::Node>("hello");  //4.创建一个节点对象

    RCLCPP_INFO(node->get_logger(),"Hello ROS2！");     //5.输出日志信息

    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}

//修改CmakeLists.txt文件
/*
1.添加可执行文件
add_executable(my_node src/hello.cpp)
2.添加依赖库
ament_target_dependencies(my_node rclcpp)
3.安装可执行文件
install(TARGETS
  my_node
  DESTINATION lib/${PROJECT_NAME}
)
*/

//编译功能包
//colcon build --packages-select demo1_cpp

//运行功能包
//ros2 run demo1_cpp my_node

