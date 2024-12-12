def check_prime(number):
    count = 0
    if number < 2:
        count += 1
    for i in range(number - 1, 1, -1):
        if number % i == 0:
            count += 1

    if count > 0:
        print(f"{number} - Составное")
    else:
        print(f"{number} - Простое")

# Прогон чисел от 1 до 100
for num in range(1, 101):
    check_prime(num)
