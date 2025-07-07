#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('q1_subscriber')
        self.subscription = self.create_subscription(
            String,
            '/new',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        print(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
