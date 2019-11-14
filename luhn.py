def luhn_check(card_number: str) -> bool:
    """
    Validate card number

    :param card_number: credit card number
    :returns: True if number is valid
    """
    card_number = card_number.replace(' ', '')  # удаляем пробелы

    if card_number.isdigit():  # если в строке остались только цифры
        numbers = list(int(n) for n in card_number)  # получаем список из цифр
        for i in range(0, len(numbers), 2):  # удваиваем значения чисел с четных индексов
            numbers[i] = numbers[i] * 2 if numbers[i] * 2 < 10 else numbers[i] * 2 - 9
        return sum(numbers) % 10 == 0
    else:
        return False


if __name__ == '__main__':
    assert luhn_check('4532 3455 1540 6633') is True
    assert luhn_check('3528 5070 9380 0507') is True
    assert luhn_check('5106330611011704') is True
    assert luhn_check('36813670686745') is False
    assert luhn_check('4532 3455 154O 6633') is False
    assert luhn_check('1122 3344 5566 7788') is False
    assert luhn_check('11_2 3344 5566 7788') is False
