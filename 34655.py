from random import randint
n = 5
lst = [randint(1, 10) for _ in range(n)]
print("Початковий список",lst)
lst1 = lst[1:] + [lst[0]]
print("Список після перестановки", lst1)
