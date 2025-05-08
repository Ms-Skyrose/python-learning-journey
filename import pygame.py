import pygame
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('ML Interactions with Pygame')

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Agent class
class Agent:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.size = 20
        self.speed = 5

    def move(self, action):
        if action == 0:  # Move up
            self.y -= self.speed
        elif action == 1:  # Move right
            self.x += self.speed
        elif action == 2:  # Move down
            self.y += self.speed
        elif action == 3:  # Move left
            self.x -= self.speed

        # Ensure agent stays within bounds
        self.x = max(0, min(WIDTH - self.size, self.x))
        self.y = max(0, min(HEIGHT - self.size, self.y))

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.size, self.size))

# Target class (the goal for the agent)
class Target:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 20)
        self.y = random.randint(0, HEIGHT - 20)
        self.size = 20

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.size, self.size))

# Main loop
def main():
    clock = pygame.time.Clock()

    agent = Agent()
    target = Target()

    action_space = 4  # 4 actions: up, right, down, left
    reward = 0
    done = False

    while not done:
        screen.fill(WHITE)
        
        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Random action (for demonstration purposes)
        action = random.randint(0, action_space - 1)
        agent.move(action)

        # Check if agent has reached the target
        if (abs(agent.x - target.x) < agent.size and abs(agent.y - target.y) < agent.size):
            reward = 1  # Reward for reaching the target
            target = Target()  # Respawn target at a new location
        else:
            reward = 0  # No reward if agent hasn't reached the target

        # Draw everything
        agent.draw()
        target.draw()

        # Display the reward and interaction info on screen
        font = pygame.font.SysFont(None, 30)
        reward_text = font.render(f"Reward: {reward}", True, (0, 0, 0))
        screen.blit(reward_text, (10, 10))

        # Update display
        pygame.display.update()

        # Control frame rate
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
