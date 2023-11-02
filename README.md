# mini_pupper_follow

This program is for object tracking by Mini Papper 2 running ROS2 Humble.  
This package is an alpha version. The program still needs to be tweaked.  
OAK-D LITE is required to run this prototype.  

## 1. Setup

1. Install depthai-ros
    ```
    sudo apt install libopencv-dev
    git clone https://github.com/luxonis/depthai-core.git
    cd depthai-core/
    git submodule update --init --recursive
    cmake -S. -Bbuild -D'BUILD_SHARED_LIBS=ON'
    cmake --build build
    echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="03e7", MODE="0666"' | sudo tee /etc/udev/rules.d/80-movidius.rules
    sudo udevadm control --reload-rules && sudo udevadm trigger
    sudo apt install ros-humble-depthai-ros
    ```

1. Install this package
    ```
    . ~/ros2_ws/install/setup.bash
    cd ~/ros2_ws/src
    git clone https://github.com/kanpapa/mini_pupper_follow.git
    cd ~/ros2_ws
    colcon build --symlink-install
    ```

## Test

```
# Terminal 1
. ~/ros2_ws/install/setup.bash
ros2 launch mini_pupper_bringup bringup.launch.py

# Terminal 2
ros2 launch depthai_examples mobile_publisher.launch.py camera_model:=OAK-D-LITE
 
# Terminal 3
. ~/ros2_ws/install/setup.bash
ros2 launch mini_pupper_follow follow.launch.py
```

## Reference
Original package is https://github.com/mangdangroboticsclub/mini_pupper_ros/tree/ros1/mini_pupper_examples

## Video
https://www.youtube.com/watch?v=uJlFrB2jR5M

