#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class ClockPublisher(Node):
    def __init__(self):
        super().__init__('clock_publisher')
        self.second_pub = self.create_publisher(Int32, '/second', 10)
        self.minute_pub = self.create_publisher(Int32, '/minute', 10)
        self.hour_pub = self.create_publisher(Int32, '/hour', 10)
        self.clock_pub = self.create_publisher(String, '/clock', 10)

        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        self.timer = self.create_timer(1.0, self.update_clock)

    def update_clock(self):
        # Publish seconds, minutes, hours
        self.publish_time_data()

        # Update time
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1

            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1

                if self.hours >= 24:
                    self.hours = 0  # Reset at 24 hrs

    def publish_time_data(self):
        # Publish individual units
        sec_msg = Int32()
        sec_msg.data = self.seconds
        self.second_pub.publish(sec_msg)

        min_msg = Int32()
        min_msg.data = self.minutes
        self.minute_pub.publish(min_msg)

        hour_msg = Int32()
        hour_msg.data = self.hours
        self.hour_pub.publish(hour_msg)

        # Publish full formatted clock string
        clock_msg = String()
        clock_msg.data = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        self.clock_pub.publish(clock_msg)

        # Print for terminal visibility
        print(clock_msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = ClockPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
