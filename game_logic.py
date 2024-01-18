import random
import mr_svin
import only_deck
# просто колода

# формирование игровой колоды
deck = ['2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah', '2d', '3d', '4d', '5d', '6d',
        '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc',
        'Qc', 'Kc', 'Ac', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks', 'As']


def get_deck():
    #print(deck)
    #print(len(deck))
    return deck
game_deck = get_deck()
# получить значение карты - возвращает значение
def get_card_rank(card):
        return card[0]
#найти похожие по значению карты - возращает ложь если нету и индексы одинаковых значений
def find_similar_rank(rank, deck):
    similar = []
    for i in deck:
        if i[0] == rank:
            similar.append(deck.index(i))
    if len(similar) == 0:
        return False
    else:
        return similar
# получить игровую колоду
def get_game_deck():
    global game_deck
    game_deck = get_deck()
    random.shuffle(game_deck)
# получить игровую руку
def get_hand(deck):
    hand = []
    for _ in range(6):
        card = random.choice(deck)
        hand.append(card)
        deck.pop(deck.index(card))
    return hand
# поменять ход игрока
def invert_move(move):
    if move == 0:
        return 1
    else:
        return 0




class Player:
    def __init__(self, hand: list[str, str, ...]):
        self.hand = hand
        self.chests = 0

    #проверить есть ли такая карта у текущего игрока, если есть то вернуть эти карты
    def check_card(self, card):
        if find_similar_rank(get_card_rank(card), self.hand):
            return [self.hand[i] for i in find_similar_rank(get_card_rank(card), self.hand)]
        else:
            return False

    #добавить карты в руку игрока
    def add_cards(self, cards):
        self.hand.extend(cards)

    #удалить карты из руки игрока
    def delete_cards(self, cards_index):
        for i in cards_index:
            self.hand.pop(self.hand.index(i))

    #спросить есть ли карта у противника если есть то забрать у него и добавить себе, если нет то вернуть ложь
    def ask_card(self, other, card):
        if other.check_card(card):
            self.add_cards(other.check_card(card))
            other.delete_cards(other.check_card(card))
            return True
        else:
            return False

    #проверить есть ли сундучок у текущего игрока, если есть то истина иначе ложь
    def check_chest(self):
        for i in range(len(self.hand)):
            counter = 0
            for j in range(i, len(self.hand)):
                if get_card_rank(self.hand[i]) == get_card_rank(self.hand[j]):
                    counter += 1
            if counter == 4:
                return self.hand[i]
        return False


    # удалить сундучок у текущеко игрока и добавить в счет 1 очко
    #def delete_chest(self, card):
    #    for i in self.hand:
    #        if get_card_rank(card) == get_card_rank(i):
    #            print(i)
    #            self.hand.pop(self.hand.index(i))
    #    self.add_chest()
    def delete_chest(self, card_in):
        self.hand = [card for card in self.hand if get_card_rank(card) != get_card_rank(card_in)]
        self.add_chest()

    # добавить в счет одно очко
    def add_chest(self):
        self.chests += 1

    #взять карту сверху колоды
    def get_card_from_deck(self):
        self.hand.append(game_deck.pop())



class Game:
    def __init__(self):
        get_deck()
        get_game_deck()
        self.deck = game_deck
        self.player1 = Player(hand=get_hand(self.deck))
        self.player2 = Player(hand=get_hand(self.deck))
        self.players_list = [self.player1, self.player2] # сформировать список игроков в котором ходит случайный игрок
        self.move = 0

    #жребий
    def random_first(self):
        self.move = random.choice((0, 1))
        return self.move

    #игровой процесс
    def game(self, card):
        if self.players_list[invert_move(self.move)].check_card(card) == False: #если карта выбранная игроком не оказалась у соперника то взять одну карту из колоды и поменять ход игрока на противоположного
            self.players_list[self.move].get_card_from_deck()
            self.move = invert_move(self.move)
        else:
            self.players_list[self.move].ask_card(self.players_list[invert_move(self.move)], card) # ХЗ че такое разбирайся сам
        for i in self.players_list:
            check = i.check_chest()
            if check is not False:
                i.delete_chest(check)

    def check_win(self):
        for i in self.players_list:
            if i.chests == 7:
                return f'{"you" if self.players_list.index(i) == 0 else "svin"}'
        if self.players_list[0].chests == 6 and self.players_list[1] == 6:
            return f'{"you" if len(self.players_list[0].hand) == 0 else "svin"}'
        return False



    # Я ЭТО НЕ ПРОВЕРЯЛ ФИКСИ ОШИБКИ

