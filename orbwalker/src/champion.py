from typing import Dict

class Champion:
    def __init__(self, data: Dict):
        self.id = data['id']
        self.name = data['name']
        self.attack_range = data['attack_range']
        self.attack_delay = data['attack_delay']
        self.base_attack_damage = data['base_attack_damage']
        self.base_attack_speed = data['base_attack_speed']
        self.is_melee = data['is_melee']
        
        self.attack_speed = self.calculate_attack_speed()
        
    def calculate_attack_speed(self):
        if self.is_melee:
            return self.base_attack_speed / (1 + self.base_attack_speed)
        else:
            return self.base_attack_speed / (1 + self.base_attack_speed * 0.625 * (self.attack_speed - 1))
