cmake_minimum_required(VERSION 3.8)
project(kratos_adithiyaharish)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rclcpp REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)


ament_python_install_package(${PROJECT_NAME})

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/RoverStatus.msg"
  DEPENDENCIES geometry_msgs builtin_interfaces
)
	

install(PROGRAMS
  scripts/q1_publisher_node.py
  scripts/q1_subscriber_node.py
  scripts/q2_s1_node.py
  scripts/q2_s2_node.py
  scripts/q4_clock.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
