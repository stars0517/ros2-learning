cmake_minimum_required(VERSION 3.8)
# 这里改成了 demo1_cpp，和你的包名一致
project(demo1_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 1. 找依赖包 (必须有 ament_cmake 和你用的 rclcpp)
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

# 2. 生成可执行文件 (假设你的代码文件叫 main.cpp)
# 这里的 my_node 是你随便起的可执行程序名字
add_executable(my_node src/hello.cpp)

# 3. 告诉 CMake 你的程序依赖 rclcpp
ament_target_dependencies(my_node rclcpp)

# 4. 安装规则（告诉系统把编译好的文件放哪里，不写这个 ros2 run 会找不到）
install(TARGETS
  my_node
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# 安装 launch 文件夹
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)
# 5. 结束符，必须在最后一行
ament_package()