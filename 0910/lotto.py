import random

def generate_lotto_numbers():
    lotto_numbers = set()

    while len(lotto_numbers) < 6:
        lotto_numbers.add(random.randint(1, 45))

    return sorted(lotto_numbers)
    # list.sort() <- 리스트를 정렬
    # sorted(list) <- 새로운 리스트 생성
lotto_result = generate_lotto_numbers()
print(lotto_result)
