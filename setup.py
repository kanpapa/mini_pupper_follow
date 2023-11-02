from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mini_pupper_follow'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kazuhiro Ouchi',
    maintainer_email='kanpapa@todo.todo',
    description='Mini Pupper Object Detection Demo',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'oak_detect = mini_pupper_follow.oak_detect:main'
        ],
    },
)
