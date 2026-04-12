from ursina import *



class Monster(Entity):
    def __init__(self, monster_data, pos, player):
        super().__init__(
            model='cube',
            color=color.blue,
            scale=1,
            position=pos,
            collider='box',
            
        )
        self.player=player
        self.hit_timer = 0
        self.original = self.position
        self.is_hit = False
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
        m_hp_ratio = self.monster_data.current_hp / self.monster_data.max_hp
        self.bar.scale_x = m_hp_ratio
        if  self.player.is_dead == False:
            
            d = distance(self, self.player) #Measure distance between player and Entities
            
            if self.hit_timer > 0:
                self.color=color.yellow
                self.hit_timer-=time.dt
            else:    
                if d < 5:
                    self.color = color.red
                    self.look_at(self.player)
                    if d > 1.5:
                        self.position += (self.player.position - self.position).normalized() * self.speed * time.dt
            
            if d < 1.5:
                self.timer += time.dt #Time between attacks instead of 60 times per frame
                #Attack :
                if self.timer >= self.attack_cooldown:
                    self.player.data.current_hp -= 3
                    self.player.p_bar.scale_x
                    self.scale = 1.2
                    self.timer = 0
                #Shortly after attack :
                if 0.1<self.timer<0.2:
                        self.scale = 1
            
            if d > 5:
                self.color = color.blue
                

            if m_hp_ratio < 0.3:
                self.bar.color=color.red

            if self.player.data.current_hp <= 0:
                self.player.is_dead = True
        #Monster position return
        self.direction2 = (self.original - self.position).normalized()    
        if self.player.is_dead == True:
            if distance(self.position, self.original) > 0.01:
                self.position += self.direction2 * self.speed * time.dt
                self.look_at(self.original)
                self.color = color.blue
            else:
                self.position = self.original
            
            
        #Monster death!
        if self.monster_data.current_hp <= 0:
            destroy(self)
            print('Monster defeated!')