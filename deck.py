import pygame
import os
import game_logic
deck_img = pygame.image.load("recources/sprites/env/deck_part.png")
def deck(n: int, surf: pygame.surface.Surface):
    for i in range(1, n//5):
        surf.blit(deck_img, (450, 770 - i * 5))

cards_image = [pygame.image.load(f'recources/sprites/cards/{i}') for i in os.listdir('recources/sprites/cards')]
dict_cards = {}
for i, j in zip(cards_image, os.listdir('recources/sprites/cards')):
    dict_cards[j[:2]] = i




def draw_hand(hand, surf):
    res = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    for i in hand:
        match game_logic.get_card_rank(i):
            case '2':
                res[0].append(i)
            case '3':
                res[1].append(i)
            case '4':
                res[2].append(i)
            case '5':
                res[3].append(i)
            case '6':
                res[4].append(i)
            case '7':
                res[5].append(i)
            case '8':
                res[6].append(i)
            case '9':
                res[7].append(i)
            case 'T':
                res[8].append(i)
            case 'J':
                res[9].append(i)
            case 'Q':
                res[10].append(i)
            case 'K':
                res[11].append(i)
            case 'A':
                res[12].append(i)
    for i, x in zip(res, [30, 100, 170, 240, 310, 380, 450, 520, 590, 660, 730, 800, 870]):
        for j in range(len(i)):
            surf.blit(dict_cards[i[j]], (x, 880 - j * 25))


def get_group_cards(hand):
    res = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    for i in hand:
        match game_logic.get_card_rank(i):
            case '2':
                res[0].append(i)
            case '3':
                res[1].append(i)
            case '4':
                res[2].append(i)
            case '5':
                res[3].append(i)
            case '6':
                res[4].append(i)
            case '7':
                res[5].append(i)
            case '8':
                res[6].append(i)
            case '9':
                res[7].append(i)
            case 'T':
                res[8].append(i)
            case 'J':
                res[9].append(i)
            case 'Q':
                res[10].append(i)
            case 'K':
                res[11].append(i)
            case 'A':
                res[12].append(i)
    return res



def group_card(cards):
    tmp = [game_logic.find_similar_rank(game_logic.get_card_rank(i), cards) for i in cards]
    res = []
    for i in tmp:
        if i not in res:
            res.append(i)
    return res
