from restaurant import Restaurant
from delivery import Delivery
from utils.payment import process_payment

class FoodApp:
    def __init__(self):
        self.restaurant = Restaurant()
        self.delivery = Delivery()

    def run(self):
        print("앱 실행됨")
        menu = self.restaurant.get_menu()
        print("메뉴:", menu)

        selected_item = menu[0]
        print(f"{selected_item}을 선택하고 장바구니에 추가함")

        process_payment(10000)

        self.restaurant.receive_order(selected_item)
        self.delivery.start_delivery(selected_item)

        print("배달 진행 상황: 음식이 배달 중입니다.")
