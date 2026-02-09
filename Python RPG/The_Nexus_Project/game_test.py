from Entities import CombatEntity
import keyboard
from ursina import *

app = Ursina()

obj_cube = Entity(model='cube', color=color.green, scale=(20,1,20))
class Player(Entity):
    def __init__(self, data):
        super().__init__(
            model='cube',
            color=color.orange,
            scale=(1,2,1),
            position=(0,1.5,0),
            )
        self.speed = 5
        self.data = data
        Text(
             text=f"{self.data.name} : {self.data.current_hp}/{self.data.max_hp}",
             parent=self,
             position=(0,1.5,0),
             size=3,
             color=color.gold
            )
    def update(self):
        self.x += held_keys['d'] * time.dt * self.speed
        self.x -= held_keys['a'] * time.dt * self.speed
        self.z += held_keys['w'] * time.dt * self.speed
        self.z -= held_keys['s'] * time.dt * self.speed
        if keyboard.is_pressed('space'):
            self.data.current_hp -= 10
            Text.text = f"{self.data.name} : {self.data.current_hp}/{self.data.max_hp}"
my_data = CombatEntity("Hero", 100, 100)
player = Player(my_data)
EditorCamera()

app.run()