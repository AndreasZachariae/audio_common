#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sound_play.libsoundplay import SoundClient

from std_msgs.msg import String


class PlayFromTopic(Node):

    def __init__(self):
        super().__init__('play_from_topic_node')
        self.subscription = self.create_subscription(
            String,
            'play_sound_name',
            self.play_sound_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.soundhandle = SoundClient(self, blocking=False)
        self.volume = 1.0
        

    def play_sound_callback(self, msg):
        self.get_logger().info('I play: "%s"' % msg.data)
        self.soundhandle.playWave(msg.data, self.volume)
        self.get_logger().info('finished')


def main(args=None):
    rclpy.init(args=args)
    node = PlayFromTopic()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("KeyboardInterrupt")
    
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()