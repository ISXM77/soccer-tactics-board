import pygame
pygame.init()
pitch = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Tactics Board Test")
WHITE = (255, 255, 255)
SCALE = 10
PITCH_W = 105 * SCALE
PITCH_H = 68 * SCALE
LEFT = (1280 - PITCH_W) // 2
TOP = (720 - PITCH_H) // 2
RIGHT = LEFT + PITCH_W
BOTTOM = TOP + PITCH_H
CENTER = (LEFT + PITCH_W // 2, TOP + PITCH_H // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pitch.fill((34, 139, 34))
    pygame.draw.line(pitch, WHITE, (LEFT, TOP), (RIGHT, TOP), 3)
    pygame.draw.line(pitch, WHITE, (LEFT, BOTTOM), (RIGHT, BOTTOM), 3)
    pygame.draw.line(pitch, WHITE, (LEFT, TOP), (LEFT, BOTTOM), 3)
    pygame.draw.line(pitch, WHITE, (RIGHT, TOP), (RIGHT, BOTTOM), 3)
    pygame.draw.line(pitch, WHITE, (CENTER[0], TOP), (CENTER[0], BOTTOM), 3)
    pygame.draw.circle(pitch, WHITE, CENTER, int(9.15 * SCALE), 3)
    pygame.draw.circle(pitch, WHITE, CENTER, 4)
    pygame.display.flip()

pygame.quit()