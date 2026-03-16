import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 100)
    
    def move(self, dy):
        self.rect.y += dy
        # Prevent paddle from going out of bounds
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

# Define the Ball class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(width // 2, height // 2, 15, 15)
        self.speed_x = 7 * (-1)**(pygame.time.get_ticks() % 2)
        self.speed_y = 7 * (-1)**(pygame.time.get_ticks() % 2)
    
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Bounce off top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed_y *= -1
        # Reset ball if it goes out of bounds
        if self.rect.left <= 0 or self.rect.right >= width:
            self.rect.x = width // 2
            self.rect.y = height // 2
            self.speed_x *= -1

# Game loop
def main():
    clock = pygame.time.Clock()
    running = True
    player1 = Paddle(30, height // 2 - 50)
    player2 = Paddle(width - 45, height // 2 - 50)
    ball = Ball()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Control player 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.move(-10)
        if keys[pygame.K_s]:
            player1.move(10)
        # Control player 2
        if keys[pygame.K_UP]:
            player2.move(-10)
        if keys[pygame.K_DOWN]:
            player2.move(10)

        ball.move()

        # Check collision with paddles
        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            ball.speed_x *= -1

        # Render
        window.fill(BLACK)
        pygame.draw.rect(window, WHITE, player1.rect)
        pygame.draw.rect(window, WHITE, player2.rect)
        pygame.draw.ellipse(window, WHITE, ball.rect)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()