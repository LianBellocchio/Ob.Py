import unittest
from orbwalker.champion import Champion

class TestChampion(unittest.TestCase):
    def test_init(self):
        # Test case for creating a new champion
        champion = Champion(name="Ashe", attack_range=600, attack_damage=59, attack_speed=0.658, movement_speed=325)
        self.assertEqual(champion.name, "Ashe")
        self.assertEqual(champion.attack_range, 600)
        self.assertEqual(champion.attack_damage, 59)
        self.assertEqual(champion.attack_speed, 0.658)
        self.assertEqual(champion.movement_speed, 325)

    def test_update_stats(self):
        # Test case for updating champion stats
        champion = Champion(name="Ashe", attack_range=600, attack_damage=59, attack_speed=0.658, movement_speed=325)
        champion.update_stats(attack_range=625, attack_damage=61, attack_speed=0.678, movement_speed=330)
        self.assertEqual(champion.attack_range, 625)
        self.assertEqual(champion.attack_damage, 61)
        self.assertEqual(champion.attack_speed, 0.678)
        self.assertEqual(champion.movement_speed, 330)

    def test_add_ability(self):
        # Test case for adding an ability to a champion
        champion = Champion(name="Ashe", attack_range=600, attack_damage=59, attack_speed=0.658, movement_speed=325)
        ability = {"name": "Frost Shot", "type": "passive", "description": "Ashe's basic attacks slow her targets by 15% for 2 seconds."}
        champion.add_ability(ability)
        self.assertEqual(len(champion.abilities), 1)
        self.assertEqual(champion.abilities[0]["name"], "Frost Shot")
        self.assertEqual(champion.abilities[0]["type"], "passive")
        self.assertEqual(champion.abilities[0]["description"], "Ashe's basic attacks slow her targets by 15% for 2 seconds.")

    def test_remove_ability(self):
        # Test case for removing an ability from a champion
        champion = Champion(name="Ashe", attack_range=600, attack_damage=59, attack_speed=0.658, movement_speed=325)
        ability1 = {"name": "Frost Shot", "type": "passive", "description": "Ashe's basic attacks slow her targets by 15% for 2 seconds."}
        ability2 = {"name": "Volley", "type": "active", "description": "Ashe fires 9 arrows in a cone dealing damage to all enemies hit."}
        champion.add_ability(ability1)
        champion.add_ability(ability2)
        champion.remove_ability(ability1)
        self.assertEqual(len(champion.abilities), 1)
        self.assertEqual(champion.abilities[0]["name"], "Volley")
        self.assertEqual(champion.abilities[0]["type"], "active")
        self.assertEqual(champion.abilities[0]["description"], "Ashe fires 9 arrows in a cone dealing damage to all enemies hit.")

if __name__ == '__main__':
    unittest.main()
