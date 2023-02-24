import random

class Player:
    def __init__(self, position):
        self.position = position
        self.movement_speed = 345

    def move_to(self, destination):
        # Calculate distance to destination
        distance_x = destination[0] - self.position[0]
        distance_y = destination[1] - self.position[1]
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5
        
        # If already at destination, don't move
        if distance == 0:
            return
        
        # Calculate time it would take to arrive at destination
        time_to_arrive = distance / self.movement_speed
        
        # Simulate movement over time
        current_pos = self.position
        remaining_time = time_to_arrive
        while remaining_time > 0:
            # Calculate distance to destination
            distance_x = destination[0] - current_pos[0]
            distance_y = destination[1] - current_pos[1]
            distance = (distance_x ** 2 + distance_y ** 2) ** 0.5
            
            # If already at destination, stop
            if distance == 0:
                break
            
            # Calculate the direction of the movement
            direction_x = distance_x / distance
            direction_y = distance_y / distance
            
            # Calculate the movement to make during this iteration
            movement_x = direction_x * self.movement_speed * min(remaining_time, 0.02)
            movement_y = direction_y * self.movement_speed * min(remaining_time, 0.02)
            
            # Update position
            current_pos = (current_pos[0] + movement_x, current_pos[1] + movement_y)
            self.position = current_pos
            
            # Update remaining time
            remaining_time -= 0.02
        
        # If we ended up slightly past the destination, adjust position
        distance_x = destination[0] - current_pos[0]
        distance_y = destination[1] - current_pos[1]
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5
        if distance != 0:
            direction_x = distance_x / distance
            direction_y = distance_y / distance
            correction_x = direction_x * distance
            correction_y = direction_y * distance
            self.position = (current_pos[0] + correction_x, current_pos[1] + correction_y)

    def attack(self, enemy):
        # Simulate an attack on the enemy
        pass

    def use_ability(self, ability, target):
        # Simulate using an ability on the target
        pass

    def predict_move(self, enemies):
        random_pos = (random.uniform(0, 15000), random.uniform(0, 15000))
        return random_pos
