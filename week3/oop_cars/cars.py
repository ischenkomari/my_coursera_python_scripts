import os.path
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying, car_type = None):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.car_type = None

    def get_photo_file_ext(self):
        extention = os.path.splitext(self.photo_file_name)[1]
        return extention

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        if body_whl:
            self.body_width, self.body_height, self.body_length = [float(x) for x in body_whl.split('x')]
        else:
            self.body_width, self.body_height, self.body_length = [0,0,0]
        self.car_type = 'truck'

    def get_body_volume(self):
        return self.body_width*self.body_height*self.body_length

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, encoding="utf8") as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            try:
                if row[0] == 'car':
                    car_list.append(Car(row[1], row[3], row[5], row[2]))
                elif row[0] == 'truck':
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))
                elif row[0] == 'spec_machine':
                    car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
                else:
                    pass
            except IndexError:
                pass
    return car_list

def _main():
    get_car_list("coursera_week3_cars.csv")

if __name__ == "__main__":
    _main()
