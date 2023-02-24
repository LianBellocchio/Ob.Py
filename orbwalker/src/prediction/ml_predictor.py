import os
import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


class MLPredictor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        self.champions = None
        self.spells = None
        self.items = None
        self.model = None
        self.target = None

    def load_data(self):
        with open(os.path.join(self.data_path, "game_data.json")) as f:
            game_data = json.load(f)

        self.champions = game_data["champions"]
        self.spells = game_data["spells"]
        self.items = game_data["items"]

        df = pd.read_csv(os.path.join(self.data_path, "training_data.csv"), index_col=0)

        # Replace champion and spell IDs with their corresponding names
        df["champion"] = df["champion"].apply(lambda x: self.champions[str(x)]["name"])
        df["spell1"] = df["spell1"].apply(lambda x: self.spells[str(x)]["name"])
        df["spell2"] = df["spell2"].apply(lambda x: self.spells[str(x)]["name"])

        # Create dummy variables for champion, spell, and item names
        champ_dummies = pd.get_dummies(df["champion"], prefix="champ")
        spell1_dummies = pd.get_dummies(df["spell1"], prefix="spell1")
        spell2_dummies = pd.get_dummies(df["spell2"], prefix="spell2")
        item_dummies = pd.get_dummies(df["item"], prefix="item")

        # Combine dummy variables with the original dataframe and drop unnecessary columns
        self.df = pd.concat([df, champ_dummies, spell1_dummies, spell2_dummies, item_dummies], axis=1)
        self.df = self.df.drop(["champion", "spell1", "spell2", "item"], axis=1)

        # Set the target variable to "win"
        self.target = "win"

    def train_model(self):
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.df.drop(self.target, axis=1), self.df[self.target], test_size=0.2)

        # Train a random forest classifier
        self.model = RandomForestClassifier()
        self.model.fit(X_train, y_train)

        # Test the accuracy of the model
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy}")

    def predict(self, game_state):
        # Convert game state to a dataframe
        game_state_df = pd.DataFrame(game_state, index=[0])

        # Replace champion and spell IDs with their corresponding names
        game_state_df["champion"] = game_state_df["champion"].apply(lambda x: self.champions[str(x)]["name"])
        game_state_df["spell1"] = game_state_df["spell1"].apply(lambda x: self.spells[str(x)]["name"])
        game_state_df["spell2"] = game_state_df["spell2"].apply(lambda x: self.spells[str(x)]["name"])

        # Create dummy variables for champion, spell, and item names
        champ_dummies = pd.get_dummies(game_state_df["champion"], prefix="champ")

        # Convertir spells en variables dummy
        spell1_dummies = pd.get_dummies(game_state_df["spell1"], prefix="spell1")
        spell2_dummies = pd.get_dummies(game_state_df["spell2"], prefix="spell2")

        # Agregar variables dummy al dataframe
        game_state_df = pd.concat([game_state_df, spell1_dummies, spell2_dummies], axis=1)

        # Eliminar columnas originales de spells
        game_state_df.drop(["spell1", "spell2"], axis=1, inplace=True)

        # Eliminar columnas no relevantes para el modelo
        game_state_df.drop(["tick", "x", "y", "minimap_x", "minimap_y", "team", "level", "exp", "minions_killed",
                    "jungle_minions_killed", "total_gold", "current_health", "max_health", "current_mana",
                    "max_mana", "ability_haste", "armor", "magic_resist", "attack_damage", "ability_power",
                    "attack_speed", "life_steal", "spell_vamp", "tenacity", "movement_speed", "gold_earned",
                    "gold_spent", "turret_kills", "inhibitor_kills", "total_heal", "total_damage_dealt",
                    "total_damage_taken", "time_ccing_others", "kills", "deaths", "assists", "largest_killing_spree",
                    "largest_multi_kill", "killing_sprees", "double_kills", "triple_kills", "quadra_kills",
                    "penta_kills", "unreal_kills", "vision_score", "wards_placed", "wards_killed"], axis=1, inplace=True)

        # Preparar datos para hacer predicciones
        prediction_data = game_state_df.values.reshape(1, -1)

        # Hacer predicción con modelo cargado
        prediction = model.predict(prediction_data)

        # Devolver predicción
        return prediction[0]
