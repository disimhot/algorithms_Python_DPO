# умеет прыгать на числовой прямой вперед 1, 2, 3  
# либо + 1
# либо + 2 прыжок
# количество способов (различных траекторий) допрыгнуть до клеточки N

n = int(input())

# можем попасть только из N-1 или N-2 клеточки
# Тогда K(N) = K(N-2) + K(N-1) рекуррентная формула

def traj_num(n):
    K = [0, 1] + [0]*n
    for i in range(2, n + 1):
        K[i] = K[i-2] + K[i-1]
    return  K[n]

print(traj_num(n))
# запретим 4 и 7 клетки
# + 3 прыжок

# allowed булевский массив
allowed = []

def count_traj(N, allowed: list):
    K = [0, 1, int(allowed[2])] + [0]*(N-3)
    for i in range(3, N+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]


# Минимальная стоимость достижения клетки N
# price[i] цена за посещение клетки i
# cost[i], C[i] минимально возможная стоимость достижения клетки i
# будем выбирать минимум из цены

# +1 прыжок
# +2 прыжок

# рек формула C = price[i] + min(C[i-1], C[i-2])
# С[1] = price[1]
# C[2]  = price[1] + price[2]

def count_min_cost(N, price: list):
    C = [float('-inf'), price[1], price[1] + price[2]] + [0]*(N - 2)
    for i in range(3, N + 1):
        C[i] = price[i] + min(C[i-1], C[i-2])

    return C[N]