import pygame
import math
from datetime import datetime as dt

screen_width, screen_height = 1200, 800

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Ur omkreds

    pygame.draw.circle(screen, (255, 255, 255), (0.5 * screen_width, 0.5 * screen_height), 300, 2)

    center_x, center_y = 0.5 * screen_width, 0.5 * screen_height

    # Ur segmenter

    for i in range(12):
        angle = math.radians(i * 30)
        
        start_x = center_x + 300 * math.cos(angle)
        start_y = center_y + 300 * math.sin(angle)
        
        end_x = center_x + 270 * math.cos(angle)
        end_y = center_y + 270 * math.sin(angle)
        
        pygame.draw.line(screen, (255, 255, 255), (start_x, start_y), (end_x, end_y), 2)

    # Visere
    # Sekund viser
    second = dt.now().strftime("%S")
    second_hand_angle = math.radians(int(second) * 6 - 90)
    second_hand_end_x = center_x + 300 * math.cos(second_hand_angle)
    second_hand_end_y = center_y + 300 * math.sin(second_hand_angle)
    pygame.draw.line(screen, (0, 255, 0), (center_x, center_y), (second_hand_end_x, second_hand_end_y), 2)

    # Minut viser
    minute = dt.now().strftime("%M")
    minute_hand_angle = math.radians(90 - ((int(minute) * 6) + (int(second) * 0.1)))
    minute_hand_end_x = center_x + 250 * math.cos(minute_hand_angle)
    minute_hand_end_y = center_y - 250 * math.sin(minute_hand_angle)
    pygame.draw.line(screen, (255, 255, 255), (center_x, center_y), (minute_hand_end_x, minute_hand_end_y), 2)

    # Time viser
    hour = dt.now().strftime("%H")
    hour_hand_angle = math.radians(90 + (((int(hour) % 12) * 30) + (int(minute) * 0.5) + (6 * 30)))
    hour_hand_end_x = center_x + 200 * math.cos(hour_hand_angle)
    hour_hand_end_y = center_y + 200 * math.sin(hour_hand_angle)
    pygame.draw.line(screen, (255, 255, 255), (center_x, center_y), (hour_hand_end_x, hour_hand_end_y), 3)

    pygame.display.flip()

    clock.tick(10)

pygame.quit()
