import unittest
from orbwalker import Orbwalker
from champion import Champion
from player import Player

class TestOrbwalker(unittest.TestCase):
    def setUp(self):
        self.champion = Champion("Ashe", "marksman")
        self.player = Player("TestPlayer", self.champion)
        self.orbwalker = Orbwalker(self.player)

    def test_select_target(self):
        # Test selecting the closest target
        target1 = Player("Target1", Champion("Aatrox", "fighter"), position=(0, 0))
        target2 = Player("Target2", Champion("Blitzcrank", "tank"), position=(100, 100))
        self.player.update_nearby_enemies([target1, target2])
        selected_target = self.orbwalker.select_target()
        self.assertEqual(selected_target, target1)

        # Test selecting a target within attack range
        target3 = Player("Target3", Champion("Caitlyn", "marksman"), position=(300, 300))
        self.player.update_nearby_enemies([target3])
        selected_target = self.orbwalker.select_target()
        self.assertEqual(selected_target, target3)

        # Test selecting a target with lowest health
        target4 = Player("Target4", Champion("Darius", "fighter"), position=(200, 200))
        target5 = Player("Target5", Champion("Ezreal", "marksman"), position=(250, 250), current_health=50)
        self.player.update_nearby_enemies([target4, target5])
        selected_target = self.orbwalker.select_target()
        self.assertEqual(selected_target, target5)

    def test_attack(self):
        # Test attacking a target
        target = Player("Target", Champion("Fiora", "fighter"), position=(400, 400))
        self.player.update_nearby_enemies([target])
        self.orbwalker.attack(target)
        self.assertEqual(target.current_health, target.max_health - self.player.attack_damage)

    def test_move_to(self):
        # Test moving to a target's position
        target = Player("Target", Champion("Garen", "tank"), position=(600, 600))
        self.player.update_nearby_enemies([target])
        self.orbwalker.move_to(target.position)
        self.assertEqual(self.player.position, target.position)

if __name__ == '__main__':
    unittest.main()
