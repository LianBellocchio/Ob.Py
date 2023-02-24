from typing import Dict, List, Tuple
import numpy as np
import joblib

class ML_Predictor:
    def __init__(self):
        self.model = joblib.load("model.pkl")

    def predict(self, player: Dict, allies: List[Dict], enemies: List[Dict]) -> Tuple[int, int]:
        features = []
        for ally in allies:
            features.append(ally['pos_x'])
            features.append(ally['pos_y'])
            features.append(ally['health'])
            features.append(ally['mana'])
            features.append(ally['attack_damage'])
            features.append(ally['ability_power'])
            features.append(ally['armor'])
            features.append(ally['magic_resist'])
            features.append(ally['attack_speed'])
            features.append(ally['movement_speed'])

        for enemy in enemies:
            features.append(enemy['pos_x'])
            features.append(enemy['pos_y'])
            features.append(enemy['health'])
            features.append(enemy['mana'])
            features.append(enemy['attack_damage'])
            features.append(enemy['ability_power'])
            features.append(enemy['armor'])
            features.append(enemy['magic_resist'])
            features.append(enemy['attack_speed'])
            features.append(enemy['movement_speed'])

        features.append(player['pos_x'])
        features.append(player['pos_y'])
        features.append(player['health'])
        features.append(player['mana'])
        features.append(player['attack_damage'])
        features.append(player['ability_power'])
        features.append(player['armor'])
        features.append(player['magic_resist'])
        features.append(player['attack_speed'])
        features.append(player['movement_speed'])

        features_array = np.array(features).reshape(1, -1)
        predicted_move = self.model.predict(features_array)

        return predicted_move[0][0], predicted_move[0][1]
