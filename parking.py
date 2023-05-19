class Car:
    """
    car class to have details of the car
    """
    def __init__(self, license_no):
        self.license_no = license_no


class Level:
    """
    Level class which has parking spots to park the car
    """
    def __init__(self, level, level_no, spot_range):
        self.level = level
        self.level_no = level_no
        self.spots = [{}] * spot_range

    def park_car(self, car):
        parking_spot = self.available_spot()
        if parking_spot:
            self.spots[parking_spot - 1] = {car.license_no: {'level': self.level,
                                                             'spot': parking_spot + (self.level_no - 1) * 20}}
            return parking_spot
        return False

    def available_spot(self):
        for idx, val in enumerate(self.spots):
            if val == {}:
                return idx + 1
        return 0

    def remove_car(self, license_no):
        for idx, spot in enumerate(self.spots):
            if license_no in spot.keys():
                self.spots[idx] = {}
                return True
        return False

    def parking_details(self, license_no):
        for idx, spot in enumerate(self.spots):
            if license_no in spot.keys():
                return spot[license_no]
        return False


class ParkingSystem:
    """
    Parking system class which controls removal and parking of cars in each level
    """

    def __init__(self):
        self.levels = []

    def create_parking_level(self, level, level_no, spot_range):
        level = Level(level, level_no, spot_range)
        self.levels.append(level)

    def park_car(self, car):
        for level in self.levels:
            is_car_parked = level.park_car(car)
            if is_car_parked:
                print(f"\nCAR PARKED AT LEVEL {level.level}, SPOT {is_car_parked}")
                return
        print("\nSORRY PARKING IS FULL")

    def remove_car(self, license_no):
        for level in self.levels:
            is_car_removed = level.remove_car(license_no)
            if is_car_removed:
                print("\nCAR REMOVED SUCCESSFULLY")
                return
        print("\nSORRY CAR IS NOT PARKED")

    def get_parking_details(self, license_no):
        for level in self.levels:
            parking_details = level.parking_details(license_no)
            if parking_details:
                print(f"\nLicense no :{license_no}\n"
                      f"Level : {parking_details['level']}\n"
                      f"Spot : {parking_details['spot']}")
                return
        print("\nSORRY CAR IS NOT PARKED")

    def print_level(self):
        for level in self.levels:
            print("\n", level.spots)


if __name__ == '__main__':
    '''
     main function to handle the operation of parking system
    '''
    ps = ParkingSystem()
    ps.create_parking_level("A", 1, 20)
    ps.create_parking_level("B", 2, 20)
    system = 'on'
    while system == 'on':
        inp = input("\nParking System\n"
                    "1. Enter 'p' to park the vehicle\n"
                    "2. Enter 'r' to remove the vehicle\n"
                    "3. Enter 'd' to see parking details of a vechicle\n"
                    "4. Enter 'off' to turn off the parking system\n"
                    "\nPlease enter your choice : ")
        if inp == 'p':
            lc = input("Enter the license number of the car to park: ")
            car = Car(lc)
            ps.park_car(car)
            ps.print_level()
        elif inp == "r":
            lc = input("Enter the license number of the car to remove: ")
            ps.remove_car(lc)
        elif inp == "d":
            lc = input("Enter the license number of the car to get the details: ")
            ps.get_parking_details(lc)
        else:
            system = 'off'
