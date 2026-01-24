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