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
