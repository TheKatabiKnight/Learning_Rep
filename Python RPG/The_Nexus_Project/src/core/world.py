from ursina import *


def create_environment():
        ground_level = Entity(model='cube', color=color.brown, scale=(20,1,20))
        # wall1 = Entity(model="cube", origin=(10, -0.5), color=color.brown, scale=(1, 5, 20), collider='box')
        # wall2 = Entity(model="cube", origin=(-10, -0.5), color=color.brown, scale=(1, 5, 20), collider='box')
        wall3 = Entity(model="cube", origin=(0, 10), color=color.brown, scale=(1, 5, 20), collider='box')
        # wall4 = Entity(model="cube", origin=(0, -0.5), color=color.brown, scale=(1, 5, 20), collider='box')