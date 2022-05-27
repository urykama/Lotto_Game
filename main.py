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

    def __str__(self):
        if self.user_is_PC:
            ret = f'Имя компьютерного игрока: {self.name}'
        else:
            ret = f'Имя игрока: {self.name}'
        if self.winner:
            ret += '  ВЫИГРАЛ'
        return ret

    def __eq__(self, other):
        '''
        что тут сравнивать?
        :param other:
        :return:
        '''
        return self.user_is_PC == other.user_is_PC and self.winner == other.winner

    def get_user_name(self):
        return self.name

    def get_user_is_PC(self):
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
            self.card.сheck(keg)
            print(len(self.card), self.card.numbers)
            if len(self.card) == 0:
                self.winner = True
        else:
            if answer() ^ self.card.сheck(keg):
                if len(self.card) == 0:
                    self.winner = True
            else:
                return 'Акелла промахнулся'


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
                start = 1 if j < 1 else 10 * j
                stop = 10 * j + 10 if j < 8 else 91
                numbers = sorted(list(sample(range(start, stop), k=sum_in_column)))
                self.numbers += numbers
                for i in range(3):
                    if self.card[i][j] == 1:
                        self.card[i][j] = numbers.pop(0)

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

    def __eq__(self, other):
        '''
        вероятность выпадения одинаковых карточек стремиться к нулю
        :param other:
        :return:
        '''
        return self.card == other.card

    def __len__(self):
        return len(self.numbers)

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

    def __str__(self):
        ret = 'Бочонки перемешаны:\n'
        for i in range(0, 90, 15):
            ret += f'{self.numbers[i: i + 15]}\n'
        return ret

    def __len__(self):
        return len(self.numbers)

    def __getitem__(self, item):
        if 0 <= item < len(self.numbers):
            return self.numbers[item]
        print('Ошибка! Элемент с таким индексом отсутсвует!')


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
    #     print(i.get_name())  # вывод имен игроков
    for player in players:
        player.take_a_card()  # игроки набирают карты
    step = 0
    game_over = False
    bag = Bag()
    # print(bag[92])
    for keg in bag.numbers:
        step += 1
        print(f'\tХод № {step} \t\tБочонок {keg}')
        for player in players:
            player.show_cards()
            if player.check_card(keg) != None:
                print('Акелла промахнулся')
                game_over = True
        for player in players:
            if player.winner:
                print(player)
                game_over = True
        if game_over:
            break
        print()

    def __str__(self):
        '''
        Это шутка, здесь класс для организации кода,
        а не для создания объектов...
        :return: выводить нечего
        '''
        return 'И вновь подолжается бой.'


if __name__ == '__main__':
    game = Game()
