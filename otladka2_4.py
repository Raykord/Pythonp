'''
В этой программе «чат-бот» просит ввести команду и выполняет её.
Если он не знает команду, он должен сообщить, что она неверная
Но это работает как-то неправильно.
'''

command = input("Введите команду(«помощь» для помощи): ")

while command != "выход":
    if command == "сказка":
        print("Жили были и жили они долго и счастливо")
    if command == "анекдот":
        print("Колобок не любил ходить в боулинг")
    if command == "мудрость":
        print("Ходи зимой в двух штанах")
    if command == "помощь":
        print("Введите команду помощь, сказка, анекдот или мудрость")
    else:
        print("Неверная команда"
    command = input("Введите команду(«помощь» для помощи): ")