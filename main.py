from random import sample  # , randint


class Player():
    def __init__(self, name='UnNamedUser', user=False):
        '''
        :param name: имя
        :param user: человек или компьютер
        '''
        self.name = name
        self.user = True if user else False

    def get(self):
        return self.name
    def get_user(self):
        return self.user

    def take_a_card(self, number_of_cards=1):
        '''
        игрок набирает себе карты
        :param number_of_cards: количество карт
        :return:
        '''
        self.card = Card()


class Card():
    # def __init__(self):
    #     '''
    #     Создание карточки
    #     как оказалось, это "тупиковый" путь
    #     '''
    #     ok = True
    #     while ok:
    #         ok = False
    #         self.numbers = sorted(list(sample(range(1, 91), k=15)))
    #         # print(self.numbers)
    #         for i in range(0, 81, 10):
    #             # print(i)
    #             decimal = 0
    #             for j in range(i, i + 10):
    #                 if j in self.numbers: decimal += 1
    #                 if j == 89 and 90 in self.numbers: decimal += 1
    #             if decimal > 3:  # в каждом столбике ... не больше трёх чисел
    #                 print(f'1111111111111111111111111111111  {j}')
    #                 ok = True

    def __init__(self):
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
            numbers = sorted(list(sample(range(10 * j, 10 * j + 9), k=sum_in_column)))
            self.numbers += numbers

            for i in range(3):
                if self.card[i][j] == 1:
                    self.card[i][j] = numbers.pop(0)
                    # print(numbers)
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
            print('VICTORY')
            return 2
        return True


class Bag():
    '''
    Bag - мешок с бочонками
    создатся случайная последовательность бочонков
    '''

    def __init__(self):
        self.numbers = list(sample(range(1, 91), k=90))


# class Keg():
#     pass

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
    # if answer:
    #     if card_check:
    #         print('продолжаем игру1')
    #         return False
    #     else:
    #         print('выход из игры1')
    #         return True
    # else:
    #     if card_check:
    #         print('выход из игры2')
    #         return True
    #     else:
    #         print('продолжаем игру2')
    #         return False
    return answer ^ card_check

# print(check_correct_answer(True, True) == False)
# print(check_correct_answer(True, False) == True)
# print(check_correct_answer(False, True) == True)
# print(check_correct_answer(False, False) == False)




if __name__ == '__main__':
    '''
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
    '''

    players = []
    number_of_players = 1  # imt(input('Введите количество игроков') - 1)
    for i in range(number_of_players):
        players.append(Player(f'PC Player {i + 1}'))
    players.append(Player('User', True))
    for i in players:
        print(i.get())
    for i in players:
        i.take_a_card()
    # for i in players:
    #     print(i.get(), '\t', i.card.numbers)

    bag = Bag()
    # print(len(bag.numbers))
    step = 0
    game_over = False
    for keg in bag.numbers:
        if game_over:
            break
        step += 1
        print(f'\tХод № {step} \t\tБочонок {keg}')
        for player in players:
            print('\tкарточка игрока: ' + player.name)
            print(player.card)
            if player.user:
                if answer():
                    if not player.card.сheck(keg):
                        print('Game Over')
                        game_over = True
                else:
                    if player.card.сheck(keg):
                        print('Game Over')
                        game_over = True
            # print(player.get(), '\t', player.card.numbers)
            if player.card.сheck(keg) == 2:
                print(f'\t\t\t{player.get()} VIN')
                game_over = True
        print()

