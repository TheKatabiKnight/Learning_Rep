from abc import ABC, abstractmethod



###Health/Death governance###
class CombatEntity:
    def __init__(self, name, max_hp, current_hp):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = current_hp
    @property
    def current_hp(self):
        return self._current_hp
    @current_hp.setter
    def current_hp(self, value):
        self._current_hp = max(0, min(value, self.max_hp))
    @property
    def is_alive(self):
        return self._current_hp > 0
    def __str__(self):
            return f"{self.name}: {self._current_hp}/{self.max_hp} HP"
###Hero creation governance###
class BaseHero(ABC):
    @abstractmethod
    def unique_ability(self):
        pass
    @abstractmethod
    def get_role(self):
        pass
    def introduce(self):
        return f"I am {self.name}, the {self.get_role()}."
class Mage(BaseHero):
    def __init__(self, name):
        self.name = name
    def unique_ability(self):
        return "Casts Fireball"
    def get_role(self):
        return "Mage"
###Skill limit/Aquisition management###
class SkillSystem:
    def __init__(self, max_slots):
        self._max_slots = max_slots
        self._skills = []
    @property
    def skills(self):
        return self._skills[:]
    def learn_skill(self, name, rank):
        skill_des = f"{name} (Rank {rank})"
        if skill_des not in self._skills:
            if len(self._skills) < self._max_slots:
                self._skills.append(skill_des)
                return "Learned"
            else:
                return "Failed"
        else:
            return "Failed"
    def forget_skill(self, name_with_rank):
        if name_with_rank in self._skills:
            self._skills.remove(name_with_rank)
###Level governance###
class Hero:
    def __init__(self, level):
        self.level = level
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, value):
        if value < 1:
            self._level = 1
        else:
            self._level = value


















































