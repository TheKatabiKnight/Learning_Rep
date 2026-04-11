from Entities import CombatEntity
from ursina import *
import random

app = Ursina()

ground_level = Entity(model='cube', color=color.gold, scale=(20,1,20))
class Player(Entity):
    def __init__(self, data):
        super().__init__(
            model='cube',
            color=color.orange,
            scale=(1,2,1),
            position=(5,1.5,-1),
            
            )
        self.is_dead = False
        self.speed = 5
        self.data = data
        
        self.p_bar_bg = Entity(
            parent=self,
            model='cube',
            color=color.black,
            scale=(1.2, 0.1, 0.1),
            y=0.8,
            billboard=True,
        )
        self.p_bar = Entity(
            parent=self.p_bar_bg,
            model='cube',
            color=color.green,
            scale=(1, 1, 1),
            x=-0.5,
            origin=(-0.5, 0),
            billboard=True,
        )
        self.HP = Text(
             text=f"{self.data.name}",
             parent=self,
             origin=(0,2),
             y=1.3,
             scale=5,
             color=color.white,
             billboard=True #Text follows camera angle
            )
        
    def update(self):
        target_pos = self.position + Vec3(0, 10, -15)
        camera.position = lerp(camera.position, target_pos, time.dt * 4)
        camera.look_at(player)
        camera.rotation_z = 0

        p_hp_ratio = self.data.current_hp / self.data.max_hp
        self.p_bar.scale_x = p_hp_ratio
        if not self.is_dead:
            self.x += held_keys['d'] * time.dt * self.speed
            self.x -= held_keys['a'] * time.dt * self.speed
            self.z += held_keys['w'] * time.dt * self.speed
            self.z -= held_keys['s'] * time.dt * self.speed

        if self.data.current_hp <= 0:
            self.color = color.black
            self.is_dead = True
        
        if self.data.current_hp > 0:
            self.color = color.orange
            self.is_dead = False

        if p_hp_ratio < 0.3:
                self.p_bar.color=color.red
        
    def input(self, key):
        if key == 'b':
            self.data.current_hp -= 10 #Lose HP
            self.p_bar.scale_x
        if key == 'h':
            self.data.current_hp += 10 #Gain HP
            self.p_bar.scale_x
        if key == 'left mouse down':
            target = mouse.hovered_entity
            if isinstance(mouse.hovered_entity, Monster):
                if distance(self, target) < 2.0 :
                    target.monster_data.current_hp -= 5
                    target.bar.scale_x
                    target.color=color.yellow

class Monster(Entity):
    def __init__(self, monster_data, pos):
        super().__init__(
            model='cube',
            color=color.blue,
            scale=1,
            position=pos,
            collider='box',
            
        )
        
        self.original = self.position
        self.is_hit = False
        self.player_dead = False
        self.speed = 1
        self.monster_data = monster_data
        self.bar_bg = Entity(
            parent=self,
            model='cube',
            color=color.black,
            scale=(1.2, 0.1, 0.1),
            y=1.2,
            billboard=True,
        )
        self.bar = Entity(
            parent=self.bar_bg,
            model='cube',
            color=color.green,
            scale=(1, 1, 1),
            x=-0.5,
            origin=(-0.5, 0),
            billboard=True,
        )
        
        self.attack_cooldown = 1.0
        self.timer = 0           
    def update(self):
        if not self.player_dead:
            m_hp_ratio = self.monster_data.current_hp / self.monster_data.max_hp
            self.bar.scale_x = m_hp_ratio
            d = distance(self, player) #Measure distance between player and Entities
            
            if d < 5:
                self.color = color.red
                
                self.look_at(player)
                if d > 1.5:
                    self.position += (player.position - self.position).normalized() * self.speed * time.dt
            
            if d < 1.5:
                self.timer += time.dt #Time between attacks instead of 60 times per frame
                #Attack :
                if self.timer >= self.attack_cooldown:
                    player.data.current_hp -= 3
                    player.p_bar.scale_x
                    self.scale = 1.2
                    self.timer = 0
                #Shortly after attack :
                if 0.1<self.timer<0.2:
                        self.scale = 1

            if d > 5:
                self.color = color.blue
                

            if m_hp_ratio < 0.3:
                self.bar.color=color.red

            if player.data.current_hp <= 0:
                self.player_dead = True
        #Monster position return
        self.direction2 = (self.original - self.position).normalized()    
        if self.player_dead:
            if distance(self.position, self.original) > 0.01:
                self.position += self.direction2 * self.speed * time.dt
            else:
                self.position = self.original
            
            
        #Monster death!
        if self.monster_data.current_hp <= 0:
            destroy(self)
            print('Monster defeated!')
        
def input(key):
    if key == 'enter':
        app.userExit()

my_data = CombatEntity("9tiba", 100, 100)
player = Player(my_data)
slimes = [
          Monster(CombatEntity("Slime", 60, 60),
          pos=(random.uniform(1, 10), 1.5, random.uniform(1, 10))) 
          for i in range(5)]

# EditorCamera() #todebug


app.run()