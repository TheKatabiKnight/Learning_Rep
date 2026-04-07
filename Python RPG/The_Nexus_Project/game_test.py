from Entities import CombatEntity
from ursina import *

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
        self.HP = Text(
             text=str(self.data),
             parent=self,
             origin=(0,0),
             y=1,
             scale=5,
             color=color.gold,
             billboard=True #Text follows camera angle
            )
    def update(self):
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

    def input(self, key):
        if key == 'b':
            self.data.current_hp -= 10 #Lose HP
            self.HP.text=str(self.data)
        if key == 'h':
            self.data.current_hp += 10 #Gain HP
            self.HP.text=str(self.data)
class Monster(Entity):
    def __init__(self, monster_data):
        super().__init__(
            model='cube',
            color=color.blue,
            scale=1,
            position=(5,1.5,5),
            collider='box',
            
        )
        self.original = self.position
        self.is_hit = False
        self.player_dead = False
        self.speed = 1
        self.monster_data = monster_data
        self.HP_monster = Text(
            text=str(self.monster_data),
             parent=self,
             origin=(0,0),
             y=1,
             scale=3.5,
             color=color.green,
             billboard=True
        )
        self.attack_cooldown = 1.0
        self.timer = 0           
    def update(self):
        if not self.player_dead:
            d = distance(self, player) #Measure distance between player and Entities
            self.direction = (player.position - self.position).normalized()
            
            if d <= 5:
                self.color = color.red
                self.HP_monster.color=color.red
                self.look_at(player)
                if d > 1.5:
                    self.position += self.direction * self.speed * time.dt
            
            if d <= 1.5:
                self.timer += time.dt #Time between attacks instead of 60 times per frame
                #Attack :
                if self.timer >= self.attack_cooldown:
                    player.data.current_hp -= 3
                    player.HP.text=str(player.data)
                    self.scale = 1.2
                    self.timer = 0
                #Shortly after attack :
                if 0.1<self.timer<0.2:
                        self.scale = 1    
                        
            if d > 5:
                self.color = color.blue
                self.HP_monster.color=color.green

            if player.data.current_hp <= 0:
                self.player_dead = True
        
        self.direction2 = (self.original - self.position).normalized()    
        if self.player_dead:
            self.position += self.direction2 * self.speed * time.dt
            
        #Monster death!
        if self.monster_data.current_hp <= 0:
            destroy(self)
            print('Monster defeated!')
        #Monster hit feedback!
        if self.is_hit == True:
            self.color = color.yellow
            self.timer += time.dt
            if self.timer >= 0.2:
                self.is_hit = False
                self.timer = 0
        
    def input(self, key):
        if key == 'left mouse down' and mouse.hovered_entity == self:
            self.monster_data.current_hp -= 5
            self.is_hit = True
            self.HP_monster.text=str(self.monster_data)

def input(key):
    if key == 'enter':
        app.userExit()

my_data = CombatEntity("Hero", 100, 100)
player = Player(my_data)
slime_data = CombatEntity("Slime", 50, 50)
slime = Monster(slime_data)

EditorCamera()

app.run()