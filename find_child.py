def find_child(n, k):
 
    effective_k = k % (2 * (n - 1))

    if effective_k <= n - 1:
        return effective_k 
    else:
        return (2 * (n - 1)) - effective_k


try:
    n = int(input("число детей (n): "))
    k = int(input("число секунд (k): "))

    if n <= 0 or k < 0:
        print("Не бывает отрицательного времени и количества людей (см. курс философии)!")
    else:
        result = find_child(n, k)
        print(f"Номер ребенка, получившего мяч после {k} секунд: {result}")
except ValueError:
    print("Нет, требуются нормальные числа!")