n = int(input())
mas = list(map(int, input().split()))
num, indexZero = list(map(int, input().split()))
mas.append(num)
for i in range(len(mas) - 1, indexZero - 1, -1):
    mas[i] = mas[i - 1]
    mas[i - 1] = num
print(" ".join(map(str, mas)))
