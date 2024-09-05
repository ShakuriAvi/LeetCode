
class Scooter:
    def __init__(self, id: int):
        self.id = id

class ScooterRent:
    scooters = set()
    def rent_scooter(self, scooter_id: int) -> bool:
        if scooter_id in self.scooters:
            return False
        self.scooters.add(scooter_id)
        return True

    def remove_scooter(self, scooter_id):
        self.scooters.remove(scooter_id)
        return True
class Parking:
    def __init__(self, id: int):
        self.id = id

class ParkingManager:
    scooter_by_parking_dict = dict()

    def parking_scooter(self, parking_id: int, scooter_id: int) -> bool:
        if parking_id in self.scooter_by_parking_dict:
            return False
        self.scooter_by_parking_dict[parking_id] = scooter_id
        return True
    def remove_by_scooter(self, scooter_id:int):
        for parking_id , _scooter_id in self.scooter_by_parking_dict.items():
            if _scooter_id == scooter_id:
                del self.scooter_by_parking_dict[parking_id]
                return True
        return False


class ManagerScooterParking:
    parking_manager = ParkingManager()
    scooter_rent = ScooterRent()

    def parking_scooter_manager(self,parking_id: int, scooter_id: int):
        action = self.parking_manager.parking_scooter(parking_id, scooter_id)
        if action:
            res = self.scooter_rent.remove_scooter(scooter_id)
            return res
        return action

    def rent_scooter_manager(self, scooter_id: int):
        action = self.scooter_rent.rent_scooter(scooter_id)

        if action:
            res = self.parking_manager.remove_by_scooter(scooter_id)
            return res
        return action






if __name__ == '__main__':
    pass
