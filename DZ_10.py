# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.

import time

class Bank_account:

    def __init__(self):
        self.balance = 0
        self.number_operations = 0
        self.money_commission = 0
        self.history_operations = []

    def _print_history_operation(self):

        print('\n')
        for number, value in enumerate(self.history_operations, 1):
            print(f'{number}. {value}')

    def refill_withdraw(self, mode):


        self.money_commission = 0 + self.money_commission

        while True:
            self.money = int(input('Введите сумму (кратную 50): '))
            if self.money % 50 == 0:
                break
            else:
                print('Повторите попытку')

        if self.number_operations == 3:
            self.money_commission += 0.03

        match mode:
            case 1:
                self.money_value = (self.money - (self.money * self.money_commission))
                self.balance += self.money_value
                self.history_operations.append(f'Пополнение баланса +{self.money_value}')
                self.number_operations += 1
            case 2:
                if self.money > self.balance:
                    print('Ошибочная операция!')
                if self.money * (0.015 + self.money_commission) <= 30:
                    self.money_value = (self.money + 30)
                    self.balance -= self.money_value
                    self.history_operations.append(f'Снятие средств -{self.money_value}')
                elif self.money * (0.015 + self.money_commission) >= 600:
                    self.money_value = (self.money + 600)
                    self.balance -= self.money_value
                    self.history_operations.append(f'Снятие средств -{self.money_value}')
                else:
                    self.money_value = (self.money + (self.money * (0.015 + self.money_commission)))
                    self.balance -= self.money_value
                    self.history_operations.append(f'Снятие средств -{self.money_value}')
                self.number_operations += 1


test = Bank_account()

while True:
    print(f'\nВведите номер операции:\n'
          '1. Пополнить счет\n'
          '2. Снять деньги\n'
          '3. Показать баланс\n'
          '4. История операций\n'
          '5. Выйти\n')

    mode = int(input('Введите номер операции: '))

    if test.balance >= 5_000_000:
        test.money_commission = 10

    match mode:
        case 1:
            test.refill_withdraw(mode)
        case 2:
            if test.balance != 0:
                test.refill_withdraw(mode)
            else:
                print('Нулевой баланс!')
        case 3:
            print(f'\nВаш баланс: {test.balance}')
            time.sleep(2)
        case 4:
            test._print_history_operation()
            time.sleep(2)
        case 5:
            break