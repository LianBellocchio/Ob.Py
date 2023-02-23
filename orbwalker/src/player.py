import os
import json
from src.champion import Champion

class Player:

    def __init__(self, name: str, champion: str):
        self.name = name
        self.champion = Champion(champion)
        self.level = 1
        self.health = self.champion.base_health
        self.mana = self.champion.base_mana

    def level_up(self):
        self.level += 1
        self.health += self.champion.base_health_per_level
        self.mana += self.champion.base_mana_per_level
        
    def gain_health(self, amount: float):
        self.health = min(self.health + amount, self.champion.max_health)
    
    def gain_mana(self, amount: float):
        self.mana = min(self.mana + amount, self.champion.max_mana)

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'champion': self.champion.name,
            'level': self.level,
            'health': self.health,
            'mana': self.mana
        }
