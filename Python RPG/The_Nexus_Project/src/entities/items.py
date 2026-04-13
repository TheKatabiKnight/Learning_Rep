from ursina import *


class Loot(Entity):
    def __init__(self,player ,item, add_to_scene_entities=True, enabled=True, **kwargs):
        super().__init__(add_to_scene_entities, enabled,
                          model='cube',
                          color=color.yellow,
                          origin=(0, 1.5),
                          position=(3, 0, 3),
                          collider='box',
                          **kwargs)
        self.player = player
        self.item = item
    def to_inv(self):
        self.player.inventory.append(self.item)
        destroy(self)
    
    def input(self, key):
        if key == 'left mouse down':
            if distance(self, self.player) < 2.0:
                button = Button(text=f"{self.item}")
                button.on_click = self.to_inv