#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('q1_publisher')
        self.publisher_ = self.create_publisher(String, '/new', 10)
        self.timer = self.create_timer(1.0 / 15.0, self.publish_message)  # 15 Hz

    def publish_message(self):
        msg = String()
        msg.data = 'Hello World !'
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
