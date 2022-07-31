# Задача о рюкзаке

M = 68
m = [12, 15, 9, 10]
c = [24, 37, 35, 48]
F = []
Ans = [[0, 0, 0, 0] for i in range(M)]
index = None


def function(n: int, ind: int) -> int:
    if n - m[ind] < 0:
        return 0
    else:
        return (F[n - m[ind]] + c[ind])


for n in range(M):
    answer = function(n, 0)
    if answer != 0:
        index = 0
    for i in range(1, 4):
        if answer < function(n, i):
            answer = function(n, i)
            index = i
    F.append(answer)

    if index is not None:
        Ans[n] = [Ans[n - m[index]][j] for j in range(4)]
        Ans[n][index] += 1
    index = None
    print(f"Итерация №{n}: общаяя стоимость товаров:{F[n]}, количество товаров по типам: "
          f"{Ans[n][0]}\t{Ans[n][1]}\t{Ans[n][2]}\t{Ans[n][3]}. Общая масса товаров = "
          f"{Ans[n][0] * m[0] + Ans[n][1] * m[1] + Ans[n][2] * m[2] + Ans[n][3] * m[3]}")
