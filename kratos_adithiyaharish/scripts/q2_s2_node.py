#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SignalS2Node(Node):
    def __init__(self):
        super().__init__('signal_s2_node')
        self.publisher_ = self.create_publisher(String, '/s2', 10)
        self.subscription = self.create_subscription(String, '/s1', self.callback, 10)

    def callback(self, msg):
        opposite = 'red' if msg.data == 'green' else 'green'
        out_msg = String()
        out_msg.data = opposite
        self.publisher_.publish(out_msg)
        print(out_msg.data)  # Only prints "green" or "red"

def main(args=None):
    rclpy.init(args=args)
    node = SignalS2Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
