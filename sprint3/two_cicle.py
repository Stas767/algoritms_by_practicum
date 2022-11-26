from typing import List


def read_input() -> List[int]:
    '''Считывает и возвращает входящие данные.'''

    lenght = int(input())
    list_days = list(map(int, input().strip().split()))
    bike_price = int(input())

    return lenght, list_days, bike_price


def binary_search(list_days: List[int], bike_price: int, left: int, right: int) -> int:
    '''Бинарный поиск с рекурсией по определению первого дня,
    когда Вася может купить велосипед за стоимость bike_price. 
    '''

    if right <= left:  # промежуток пуст
        return -1

    mid = (left + right) // 2
    if list_days[mid - 1] < bike_price <= list_days[mid]:
        return mid
    if list_days[mid] >= bike_price:
        return binary_search(list_days, bike_price, left, mid)
    if list_days[mid] <= bike_price:
        return binary_search(list_days, bike_price, mid + 1, right)


def main() -> None:
    '''Основная логика.'''

    lenght, list_days, bike_price = read_input()
    left = 0
    right = lenght + 1  # Смещаю индексы на 1 вправо
    two_bikes_price = bike_price * 2
    list_days.insert(0, 0)  # Смещаю индексы на 1 вправо
    first_bike = binary_search(list_days, bike_price, left, right)
    second_bike = binary_search(list_days, two_bikes_price, left, right)
    print(first_bike, second_bike)


if __name__ == '__main__':
    main()
