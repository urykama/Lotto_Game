from random import sample  # , randint


class Player():
    def __init__(self, name = 'qwerty'):
        self.name = name

    def get(self):
        print(self.name)

    def take_a_card(self, number_of_cards = 1):
        self.card = Card()

class Card():
    def __init__(self):
        self.numbers = sorted(list(sample(range(1, 91), k=15)))

    def сheck(self, keg):
        try:
            self.numbers.remove(keg)
        except ValueError:  # IndexError:
            # print('ошибка удаления')
            return False
        print('удаление прошло успешно')
        if self.numbers == []:
            print('VICTORY')
            return 2
        return True


class Bag():
    def __init__(self):
        self.numbers = list(sample(range(1, 91), k=90))


# class Keg():
#     pass


if __name__ == '__main__':
    card_player = Card()
    card_comp = Card()
    bag = Bag()
    step = 0
    for i in bag.numbers:
        step += 1
        print(f'\tХод № {step} \t\tБочонок {i}')
        print(card_player.numbers)
        print(card_comp.numbers)
        # answer = True if input('Зачеркнуть цифру? (y/n)').strip().lower() == 'y' else False
        if card_player.сheck(i) == 2:
            print('Player VIN')
            break
        if card_comp.сheck(i) == 2:
            print('Comp VIN')
            break

    players = []
    number_of_players = 6  # imt(input('Введите количество игроков') - 1)
    for i in range(number_of_players):
        players.append(Player(f'Player {i + 1}'))
    for i in players:
        i.get()

    # if answer :
    #     print("Yes")
    # card_player.numbers.pop(i)
    # else:
    #     print('Game Over!')
    #     break
    # if answer and i in card_comp.numbers:
    #     print("Fuck")
    #     card_comp.numbers.remove(i)
