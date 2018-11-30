import os.path
import csv

SPEC_MACHINE = 'spec_machine'
TRUCK = 'truck'
CAR = 'car'


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.car_type = None

    def get_photo_file_ext(self):
        extention = os.path.splitext(self.photo_file_name)[1]
        return extention

    def __repr__(self):
        return "{" + self.brand + " " + self.photo_file_name + " " + str(self.carrying) + " " + self.car_type + "}"


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = CAR


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        if body_whl:
            self.body_width, self.body_height, self.body_length = [float(x) for x in body_whl.split('x')]
        else:
            self.body_width, self.body_height, self.body_length = [0, 0, 0]
        self.car_type = TRUCK

    def get_body_volume(self):
        return self.body_width*self.body_height*self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = SPEC_MACHINE


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, encoding="utf8") as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) < 7:
                print('invalid row: ', row)
                break

            car = build_car(row)
            if car:
                car_list.append(car)

    return car_list


def build_car(row):
    car_type = row[0]
    brand = row[1]
    passenger_seats_count = row[2]
    photo_file_name = row[3]
    body_whl = row[4]
    carrying = row[5]
    extra = row[6]
    if car_type == CAR:
        car = Car(brand, photo_file_name, carrying, passenger_seats_count)
    elif car_type == TRUCK:
        car = Truck(brand, photo_file_name, carrying, body_whl)
    elif car_type == SPEC_MACHINE:
        car = SpecMachine(brand, photo_file_name, carrying, extra)
    else:
        print('unknown car type', car_type)
        car = None
    return car


def _main():
    print('Result: ', get_car_list("coursera_week3_cars.csv"))


if __name__ == "__main__":
    _main()
