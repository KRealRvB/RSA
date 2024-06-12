p = 3
q = 7

mod = p * q # 21

phi = (p - 1) * (q - 1) # 12

e = 5 # открытый ключ

d = 17 # приватный ключ

x = int(input(f"Введите число, меньше {mod}: "))
crypted_message = (x ** e) % mod
print(f"Передаваемое значение: {x}")
print(f"Зашифрованное сообщение: {crypted_message}")
encrypted_message = (crypted_message ** 17) % mod
print(f"Расшифрованное сообщение: {encrypted_message}")