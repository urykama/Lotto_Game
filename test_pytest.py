import pytest
# import pytest_cov
from main import check_correct_answer

from main import Bag, Player, Card


class TestBag:

    def test_Bag(self):
        '''
        Всего 90 бочонков с цифрами от 1 до 90
        (В жизни они обычно достаются из мешка чтобы можно было вытянуть случайно)
        :return:
        '''
        bag = Bag()
        assert len(bag.numbers) == 90

    def test_Bag_first_end(self):
        bag = Bag()
        temp = bag.numbers
        temp.sort()
        assert temp[0] == 1
        assert temp[-1] == 90

    def test_Bag_random(self):
        bag = Bag()
        # ниже проверка, что нет повторяющихся номеров
        assert len(set(bag.numbers)) == len(bag.numbers)

    def test_Bag_len(self):
        bag = Bag()
        assert len(bag) == len(bag.numbers)

    def test_Bag_get_item(self):
        bag = Bag()
        assert int(bag[89])
        assert bag[90] == None


class TestPlayer():
    def test_get_user_name(self):
        player = Player()
        assert player.get_user_name() == 'UnNamedUser'

    def test_get_user_is_PC(self):
        player = Player()
        assert player.get_user_is_PC() == True

    def test_get_user2(self):
        player = Player()
        player.take_a_card()
        assert len(player.card.__str__()) == 194

    def test_check_card(self):
        player = Player()
        player.take_a_card()
        player.card.numbers = [13]
        assert player.winner == False
        player.check_card(13)
        assert player.winner == True


class TestCard():
    def test_card(self):
        card = Card()
        assert len(card.__str__()) == 194
        assert len(card.numbers) == 15
        assert card.сheck(card.numbers[0]) == True
        assert len(card.numbers) == 14
        assert card.сheck(91) == False
        card.numbers = [13]
        assert card.сheck(13) == 'victory'


@pytest.mark.parametrize('a, b, expected_result', [(True, True, False),
                                                   (True, False, True),
                                                   (False, True, True),
                                                   (False, False, False)])
def test_check_correct_answer(a, b, expected_result):
    '''
	Если игрок выбрал "зачеркнуть":
		Если цифра есть на карточке - она зачеркивается и игра продолжается.
		Если цифры на карточке нет - игрок проигрывает и игра завершается.
	Если игрок выбрал "продолжить":
		Если цифра есть на карточке - игрок проигрывает и игра завершается.
		Если цифры на карточке нет - игра продолжается.
	:return: True - выход из игры
	'''
    assert check_correct_answer(a, b) == expected_result
