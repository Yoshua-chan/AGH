class Parking:
    def __init__(self):
        self.parking_spots = 5
        self.occupied_spots = 0
        self.gross_sales = 0
        self.current_truck_list = []
        self.current_car_list = []
        self.current_single_track_list = []
        self.numbers_truck = set()
        self.numbers_car = set()
        self.numbers_single_track = set()

    def add_car(self, car):
        if self.occupied_spots < self.parking_spots:
            self.occupied_spots += 1

            if car.car_type == "car":
                self.current_car_list.append(car)
                self.numbers_car.add(car.reg_num)
                self.gross_sales += 10

            elif car.car_type == "truck":
                self.current_truck_list.append(car)
                self.numbers_truck.add(car.reg_num)
                self.gross_sales += 30

            elif car.car_type == "single track":
                self.current_single_track_list.append(car)
                self.numbers_single_track.add(car.reg_num)
                self.gross_sales += 5
        else:
            print("Brak wolnych miejsc na parkingu")

    def empty(self):
        self.current_car_list.clear()
        self.current_truck_list.clear()
        self.current_single_track_list.clear()
        self.occupied_spots = 0

    def remove_car(self, car):
        if car.car_type == "car":
            self.current_car_list.remove(car)
            self.occupied_spots -= 1
        elif car.car_type == "truck":
            self.current_truck_list.remove(car)
            self.occupied_spots -= 1
        elif car.car_type == "single track":
            self.current_single_track_list.remove(car)
            self.occupied_spots -= 1
        else:
            print("Nie ma takiego samochodu na parkigu")

    def get_free_spots(self) -> int:
        return self.parking_spots - self.occupied_spots

    def get_gross_sales(self) -> int:
        return self.gross_sales

    def get_car_numbers(self):
        return self.numbers_car

    def get_truck_numbers(self):
        return self.numbers_truck

    def get_single_track_numbers(self):
        return self.numbers_single_track


class Car:
    def __init__(self, registration_number, color, car_type):
        self.reg_num = registration_number
        self.color = color
        self.car_type = car_type

    def drive_in(self, parking):
        parking.add_car(self)

    def drive_out(self, parking):
        parking.remove_car(self)
