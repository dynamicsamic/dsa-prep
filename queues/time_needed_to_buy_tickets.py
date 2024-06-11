def time_required_to_buy(tickets: list[int], k: int) -> int:
    counter = 0

    while tickets[k] > 0:
        for i in range(len(tickets)):
            if tickets[k] == 0:
                break

            if tickets[i] > 0:
                tickets[i] -= 1
                counter += 1

    return counter


def time_required_to_buy2(tickets: list[int], k: int) -> int:
    count = tickets[k]

    for i in range(len(tickets)):
        if i < k:
            count += min(tickets[i], tickets[k])
        elif i > k:
            count += min(tickets[k] - 1, tickets[i])

    return count


tickets1 = [2, 3, 2]
k1 = 2

tickets2 = [5, 1, 1, 1]
k2 = 0
print(time_required_to_buy2(tickets1, k1))

"""
[n for n in [:k] i n ]
"""
