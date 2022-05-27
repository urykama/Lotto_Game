from random import sample


class Player():
    def __init__(self, name='UnNamedUser', user_is_PC=True):
        '''
        :param name: имя
        :param user: человек или компьютер
        '''
        self.name = name
        self.user_is_PC = True if user_is_PC else False
        self.winner = False

    def get(self):
        return self.name

    def get_user(self):
        return self.user_is_PC

    def take_a_card(self, number_of_cards=1):
        '''
        игрок набирает себе карты
        :param number_of_cards: количество карт
        :return:
        '''
        self.card = Card()

    def show_cards(self):
        print('\tкарточка игрока: ' + self.name)
        print(self.card)

    def check_card(self, keg):
        if self.user_is_PC:
            if self.card.сheck(keg) == 'victory':
                self.winner = True
        else:
            player_card_сheck = self.card.сheck(keg)
            if answer() ^ player_card_сheck:
                if player_card_сheck == 'victory':
                    self.winner = True

class Card():
    def __init__(self):
        card_bad = True
        while card_bad:
            card_bad = False
            self.numbers = []
            self.card = ([0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0])
            for row in range(0, 3):
                numbers = sorted(list(sample(range(0, 9), k=5)))
                for i in range(0, 9):
                    self.card[row][i] = 1 if i in numbers else 0

            for j in range(9):
                sum_in_column = self.card[0][j] + self.card[1][j] + self.card[2][j]
                if sum_in_column in (0, 3):
                    card_bad = True
                    break
                plus = 10 if j < 8 else 11
                # print(j, '\t', 10 * j + plus, '\t',sum_in_column)
                numbers = sorted(list(sample(range(10 * j, 10 * j + plus), k=sum_in_column)))
                self.numbers += numbers

                for i in range(3):
                    if self.card[i][j] == 1:
                        self.card[i][j] = numbers.pop(0)
            # print(self.numbers)

    def __str__(self):
        ret = '+------------------------------------+\n'
        for i in range(3):
            for j in range(9):
                if j == 0:
                    ret += '|'
                if self.card[i][j] == 0:
                    ret += '    '
                elif self.card[i][j] in self.numbers:
                    if self.card[i][j] < 10:
                        ret += ' '
                    ret += ' ' + str(self.card[i][j]) + ' '
                else:
                    ret += ' -- '
            ret += '|\n'
        ret += '+------------------------------------+'
        return ret

    def сheck(self, keg):
        '''
        пробуем убрать из карточки выпавший бачонок
        + проверка, если карточка опустела, игрок победил
        :param keg:
        :return:
        '''
        try:
            self.numbers.remove(keg)
        except ValueError:  # IndexError:
            # print('ошибка удаления')
            return False
        # print('удаление прошло успешно')
        if self.numbers == []:
            return 'victory'
        return True


class Bag():
    '''
    Bag - мешок с бочонками
    создатся случайная последовательность бочонков
    '''

    def __init__(self):
        self.numbers = list(sample(range(1, 91), k=90))


def answer():
    '''
    пользовательский ввод:
    если введено "Y" или "y" (с пробелами до и или после) - возвращаем True
    в остальных случаях - возвращаем False
    :return: True or False
    '''
    return input('Зачеркнуть цифру? (y/n)  ').strip().lower() == 'y'


def check_correct_answer(answer, card_check):
    '''

    :param answer:
    :param card_check:
    :return: True  - выход из игры,
             False - продолжаем игру
    '''
    if answer:
        if card_check:
            print('продолжаем игру1')
            return False
        else:
            print('выход из игры1')
            return True
    else:
        if card_check:
            print('выход из игры2')
            return True
        else:
            print('продолжаем игру2')
            return False
    # return answer ^ card_check


class Game():
    '''
    создаем игров
    # int(input('Введите количество игроков') - 1)
    '''
    players = []
    number_of_players = 5  # количество игроков компьютер и их создание
    for i in range(number_of_players):
        players.append(Player(f'PC Player {i + 1}'))
    # players.append(Player('User', False))  # добавление игрока пользователь
    # for i in players:
    #     print(i.get())  # вывод имен игроков
    for player in players:
        player.take_a_card()  # игроки набирают карты
    # for i in players:
    #     print(i.get(), '\t', i.card.numbers)

    step = 0
    game_over = False
    bag = Bag()
    for keg in bag.numbers:
        step += 1
        print(f'\tХод № {step} \t\tБочонок {keg}')
        for player in players:
            player.show_cards()
            player.check_card(keg)
        for player in players:
            if player.winner:
                print(f'\t\t\t{player.get()} WINNER')
                game_over = True
        if game_over:
            break
        print()


if __name__ == '__main__':
    game = Game()
