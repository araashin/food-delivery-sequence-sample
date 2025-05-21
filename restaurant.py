class Restaurant:
    def get_menu(self):
        return ["김치찌개", "된장찌개", "제육볶음"]

    def receive_order(self, item):
        print(f"음식점: '{item}' 주문을 받았습니다.")
