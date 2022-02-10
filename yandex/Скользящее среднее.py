# Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.

# Измерения велись n секунд.

# В секунду i поступает qi запросов.

# Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.

n = int(input())
requests = [int(x) for x in input().split()]
k = int(input())

result = []
current_average_sum = sum(requests[:k], 0)
result.append(current_average_sum/k)

for i in range(n - k):
    # делаем сдвиг в сумме чисел
    current_average_sum -= requests[i]
    current_average_sum += requests[i + k]
    result.append(current_average_sum/k)

print(*result)

