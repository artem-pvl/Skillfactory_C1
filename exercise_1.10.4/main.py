from cat import Cat
from clients import Client, Guest

if __name__ == '__main__':

    cat1 = Cat("Барон", "Мальчик", "2")
    cat2 = Cat("Сэм", "Мальчик", "2")

    cat1.printCat()
    cat2.printCat()

    print()
    client_1 = Client("Вася", "Пупкин")
    print(client_1)
    client_1.add_money(30)
    print(client_1.get_account())
    client_1.add_money(30.1)
    client_1.spend_money(10)

    print()
    print(client_1)
    print("Транзакции клиента: ", ", ".join(map(str, client_1.get_transactions())))

    guests = [
        Guest("Иван", "Петров", "Москва", "Наставник"),
        Guest("Иван", "Кожедуб", "Орёл", "Наставник"),
        Guest("Какойто", "Человеков", "Санкт-Петербург", "Наставник")
    ]

    print("\nСписок гостей:")
    for guest in guests:
        print(guest)
