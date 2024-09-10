# 클래스와 메서드 예제 파일

# 인스턴스 메서드 예제
class Dog:
    def __init__(self, name):
        self.name = name  # 인스턴스 변수

    def bark(self):  # 인스턴스 메서드
        return f"{self.name}가 짖습니다."

# 정적 메서드 예제
class MathUtils:
    @staticmethod
    def add(a, b):  # 정적 메서드
        return a + b

# 클래스 메서드 예제
class Animal:
    species_count = 0  # 클래스 변수

    def __init__(self, name):
        self.name = name
        Animal.species_count += 1

    @classmethod
    def get_species_count(cls):  # 클래스 메서드
        return f"총 {cls.species_count}종의 동물이 있습니다."

# 소멸자 메서드 예제
class Example:
    def __del__(self):
        print("객체가 소멸되었습니다.")

# 연산자 오버로딩 예제
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # + 연산자 오버로딩
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):  # 문자열 표현
        return f"({self.x}, {self.y})"

# 상속과 메서드 오버라이딩 예제
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "동물이 소리를 냅니다."

class Dog(Animal):  # Animal 클래스를 상속받음
    def speak(self):  # 메서드 오버라이딩
        return f"{self.name}가 짖습니다."

# 연산자 오버로딩 예제
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):  # + 연산자 오버로딩
        return self.value + other.value

# 실행 예제

if __name__ == "__main__":
    # 인스턴스 메서드 예제
    dog = Dog("Max")
    print(dog.bark())  # 출력: Max가 짖습니다.

    # 정적 메서드 예제
    print(MathUtils.add(3, 5))  # 출력: 8

    # 클래스 메서드 예제
    cat = Animal("고양이")
    dog = Animal("개")
    print(Animal.get_species_count())  # 출력: 총 2종의 동물이 있습니다.

    # 소멸자 메서드 예제
    obj = Example()
    del obj  # 출력: 객체가 소멸되었습니다.

    # 연산자 오버로딩 예제
    v1 = Vector(2, 4)
    v2 = Vector(1, 3)
    result = v1 + v2  # __add__ 메서드 호출
    print(result)  # 출력: (3, 7)

    # 상속과 메서드 오버라이딩 예제
    dog = Dog("Max")
    print(dog.speak())  # 출력: Max가 짖습니다.

    # 연산자 오버로딩 예제
    n1 = Number(10)
    n2 = Number(20)
    print(n1 + n2)  # 출력: 30
