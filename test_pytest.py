import pytest
from main import check_correct_answer

from main import Bag


class TestBag:

    def test_Bag(self):
        '''
        Всего 90 бочонков с цифрами от 1 до 90
        (В жизни они обычно достаются из мешка чтобы можно было вытянуть случайно)
        :return:
        '''
        bag = Bag()
        assert len(bag.numbers) == 90
        assert len(set(bag.numbers)) == len(bag.numbers)


from main import answer


# def test_answer():
#     '''
#     Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
#     при вводе "y" или "Y" (с пробелами или без),
#     возвращает True
#     :return:
#     '''
#     assert answer('y') == True


def test_check_correct_answer():
    '''
	Если игрок выбрал "зачеркнуть":
		Если цифра есть на карточке - она зачеркивается и игра продолжается.
		Если цифры на карточке нет - игрок проигрывает и игра завершается.
	Если игрок выбрал "продолжить":
		Если цифра есть на карточке - игрок проигрывает и игра завершается.
		Если цифры на карточке нет - игра продолжается.
	:return: True - выход из игры
	'''
    assert check_correct_answer(True, True) == False
    assert check_correct_answer(True, False) == True
    assert check_correct_answer(False, True) == True
    assert check_correct_answer(False, False) == False
