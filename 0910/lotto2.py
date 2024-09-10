import random

def generate_lotto_numbers(*args):
    lotto_numbers = set()
    for n in args:
        lotto_numbers.add(n)

    while len(lotto_numbers) < 6:
        lotto_numbers.add(random.randint(1, 45))
        sorted_lotto_numbers = sorted(lotto_numbers)
    if args:
        print(f"입력된 숫자 + 생성된 로또 번호: {sorted_lotto_numbers}")
    else:
        print(f"입력된 숫자 없이 생성된 로또 번호: {sorted_lotto_numbers}")

    return sorted_lotto_numbers
    # list.sort() <- 리스트를 정렬
    # sorted(list) <- 새로운 리스트 생성
lotto_result = generate_lotto_numbers()
lotto_result2 = generate_lotto_numbers(1,2,3)
print(lotto_result2)
