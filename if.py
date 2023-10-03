pin = 1234
print("Введите пожалуйста Ваш пин-код")
user_pin = int(input())

if pin == user_pin:
    print("Какую сумму вы хотите снять")
else:
    print("Ошибка, введите корректный пин-код, у вас осталось 2 попытки")
    user_pin = int(input())
    if pin == user_pin:
        print("Какую сумму вы хотите снять")
    else:
        print("Ошибка, введите корректный пин-код, у вас осталось 1 попыткa")
        user_pin = int(input())

        if pin == user_pin:
            print("Какую сумму вы хотите снять")
        else:
            print("Ошибка, ваша карта заблокирована пошел нахер")





