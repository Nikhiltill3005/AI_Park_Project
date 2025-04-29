import pybullet as p
import os


class Box:
    def __init__(self, client, base):
        f_name = os.path.join(os.path.dirname(__file__), 'simplebox.urdf')
        self.goal = client.loadURDF(fileName=f_name,
                   basePosition=[base[0], base[1], 0])


