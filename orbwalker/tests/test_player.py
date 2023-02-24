import unittest
from unittest.mock import MagicMock

from orbwalker import Player, Champion, Orbwalker


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.mock_champion_data = {
            "id": 1,
            "name": "Test Champion",
            "range": 550,
            "attack_speed": 0.625,
            "attack_damage": 60,
            "abilities": {
                "q": {"name": "Test Q", "range": 500},
                "w": {"name": "Test W", "range": 600},
                "e": {"name": "Test E", "range": 400},
                "r": {"name": "Test R", "range": 800},
            },
        }
        self.champion = Champion(self.mock_champion_data)
        self.orbwalker = Orbwalker()
        self.mock_prediction = MagicMock(return_value=(500, 500))
        self.player = Player(self.champion, self.orbwalker, self.mock_prediction)

    def test_player_can_move(self):
        self.assertTrue(self.player.move((500, 500)))

    def test_player_can_attack(self):
        self.assertTrue(self.player.attack((500, 500)))

    def test_player_can_cast_ability(self):
        self.assertTrue(self.player.cast_ability("q", (500, 500)))

    def test_player_knows_his_champion(self):
        self.assertEqual(self.player.champion.name, "Test Champion")

    def test_player_can_set_attack_target(self):
        target = MagicMock()
        self.player.set_attack_target(target)
        self.assertEqual(self.player.attack_target, target)

    def test_player_can_set_move_target(self):
        target = (500, 500)
        self.player.set_move_target(target)
        self.assertEqual(self.player.move_target, target)

    def test_player_can_set_ability_target(self):
        target = (500, 500)
        self.player.set_ability_target(target)
        self.assertEqual(self.player.ability_target, target)

    def test_player_knows_his_attack_range(self):
        self.assertEqual(self.player.attack_range, 550)

    def test_player_knows_his_attack_speed(self):
        self.assertEqual(self.player.attack_speed, 0.625)

    def test_player_knows_his_attack_damage(self):
        self.assertEqual(self.player.attack_damage, 60)

    def test_player_knows_his_ability_ranges(self):
        self.assertEqual(
            self.player.ability_ranges, {"q": 500, "w": 600, "e": 400, "r": 800}
        )

    def test_player_can_predict_ability(self):
        ability = "q"
        target = MagicMock()
        self.player.predict_ability(ability, target)
        self.mock_prediction.assert_called_once_with(self.champion, ability, target)
