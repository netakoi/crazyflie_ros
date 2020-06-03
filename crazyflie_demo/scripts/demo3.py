#!/usr/bin/env python
from demo import Demo

if __name__ == '__main__':
    demo = Demo(
        [
            #x   ,   y,   z, yaw, sleep
            [0.0 , -1.0, 2, 0, 2],
            [1.5 , -1.0, 2, 0, 2],
            [-1.5 , -1.0, 2, 0, 2],
            [-1.5 , -1.5, 2, 0, 2],
            [0.0 , -1.0, 2, 0, 0],
        ]
    )
    demo.run()
