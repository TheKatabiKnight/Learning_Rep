from ursina import *
from src.core.persistence import save_player_state





class Player(Entity):
    def __init__(self, data, player_pos, monster, **kwargs):
        super().__init__(
            model='cube',
            color=color.orange,
            scale=(1,2,1),
            position=player_pos,
            )
        self.monster=monster
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
        #camera angle
        # target_pos = self.position + Vec3(0, 10, -15)
        # camera.position = lerp(camera.position, target_pos, time.dt * 4)
        # camera.look_at(self)
        # camera.rotation_z = 0

        #hp bar
        p_hp_ratio = self.data.current_hp / self.data.max_hp
        self.p_bar.scale_x = p_hp_ratio
        if not self.is_dead:
            dx = held_keys['d'] - held_keys['a']
            dz = held_keys['w'] - held_keys['s']
            step = self.speed * time.dt
            ray_origin = self.position + Vec3(0, 0.5, 0)
            hit_info_X = raycast(ray_origin, Vec3(dx, 0, 0), step+0.5, ignore=(self,))
            if dx != 0 and not hit_info_X.hit:
                self.x += dx * step
            hit_info_Z = raycast(ray_origin, Vec3(0, 0, dz), step+0.5, ignore=(self,))
            if dz != 0 and not hit_info_Z.hit:
                self.z += dz * step  

        if self.data.current_hp <= 0:
            self.color = color.black
            self.is_dead = True
        
        if self.data.current_hp > 0:
            self.color = color.orange
            self.is_dead = False

        #hp bar color change
        if p_hp_ratio < 0.3:
                self.p_bar.color=color.red
        if p_hp_ratio >= 0.3:
                self.p_bar.color=color.green
        
    def input(self, key):
        if key == 'b':
            self.data.current_hp -= 10 #Lose HP
            self.p_bar.scale_x
        if key == 'h':
            self.data.current_hp += 10 #Gain HP
            self.p_bar.scale_x
        if key == 'left mouse down':
            target = mouse.hovered_entity
            if isinstance(mouse.hovered_entity, self.monster):
                if distance(self, target) < 2.0 :
                    target.monster_data.current_hp -= 5
                    target.bar.scale_x
                    target.hit_timer = 0.1
    
        if key == 'escape':
            save_player_state("save_player_data.txt", self)
            app.userExit()

