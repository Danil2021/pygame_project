def get_card_from_coord(x, y):
    if 33 <= x <= 102 and 881 <= y <= 980:
        return '2'
    elif 103 <= x < 169 and 881 <= y <= 980:
        return '3'
    elif 172 <= x <= 240 and 881 <= y <= 980:
        return '4'
    elif 245 <= x <= 311 and 881 <= y <= 980:
        return '5'
    elif 312 <= x <= 380 and 881 <= y <= 980:
        return '6'
    elif 381 <= x <= 450 and 881 <= y <= 980:
        return '7'
    elif 451 <= x <= 520 and 881 <= y <= 980:
        return '8'
    elif 521 <= x <= 590 and 881 <= y <= 980:
        return '9'
    elif 591 <= x <= 660 and 881 <= y <= 980:
        return 'T'
    elif 661 <= x <= 730 and 881 <= y <= 980:
        return 'J'
    elif 731 <= x <= 800 and 881 <= y <= 980:
        return 'Q'
    elif 801 <= x <= 870 and 881 <= y <= 980:
        return 'K'
    elif 871 <= x <= 940 and 881 <= y <= 980:
        return 'A'

