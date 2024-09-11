class Car:
    total_cars = 0 # 클래스 변수: 모든 인스턴스에서 공유됨.

    def __init__(self, make, model):
        # 인스턴스 변수: 각각의 인스턴스에서 개별적으로 유지됨.
        self.make = make
        self.model = model
        Car.total_cars += 1
    # 인스턴스 메서드: 각 인스턴스의 속성에 접근하고 변경 가능
    def get_info(self):
        return f"Car: {self.make}{self.model}"
    # 클래스 메서드: 클래스 변수에 접근 가능
    @classmethod
    def get_total_cars(cls):
        return {f"Total cars:{cls.total_cars}"}
    # 정적 메서드: 인스턴스나, 클래스와 관련이 없는 단순 기능 수행
    @staticmethod
    def car_horn():
        return "Beep beep!"
    # 인스턴스 생성
car1 = Car("Bentley", "컨티넨탈GT")
car2 = Car("Rolls=Royce", "팬텀")
    # 1. 인스턴스 메서드 호출
print(car1.get_info())
print(car2.get_info())
    # 2. 클래스 메서드 호출
print(Car.get_total_cars())
    # 3. 정적 메서드
print(Car.car_horn())