import game_logic
import pygame
import deck


one_card = pygame.image.load("recources/sprites/env/table_card.png")

def get_card(surf, fps):
    for _ in range(10):
        if fps // 10 == 0:
            surf.blit(one_card, (250, 750))
        elif fps // 10 == 1:
            surf.blit(one_card, (250, 760))
        elif fps // 10 == 2:
            surf.blit(one_card, (250, 770))
        elif fps // 10 == 3:
            surf.blit(one_card, (250, 780))
        elif fps // 10 == 4:
            surf.blit(one_card, (250, 790))
        elif fps // 10 == 5:
            surf.blit(one_card, (250, 800))
        elif fps // 10 == 6:
            surf.blit(one_card, (250, 810))




