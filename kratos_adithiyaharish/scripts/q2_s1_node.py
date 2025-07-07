#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SignalS1Node(Node):
    def __init__(self):
        super().__init__('signal_s1_node')
        self.publisher_ = self.create_publisher(String, '/s1', 10)
        self.state = 'green'
        self.publish_message()
        self.timer = self.create_timer(10.0, self.timer_callback)

    def timer_callback(self):
        self.state = 'red' if self.state == 'green' else 'green'
        self.publish_message()

    def publish_message(self):
        msg = String()
        msg.data = self.state
        self.publisher_.publish(msg)
        print(msg.data)  # Only prints "green" or "red"

def main(args=None):
    rclpy.init(args=args)
    node = SignalS1Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

