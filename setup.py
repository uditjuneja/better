from parking_system import db

db.create_all()

from parking_system.models import ParkingLot
from parking_system.config import Config, VEHICLE_MAPPING

mul_factor = Config.SPACE_ON_A_FLOOR // sum(list(Config.VEHICLES_RATIO.values()))

vehicle_id_count = {}

for vehicle in Config.VEHICLES_RATIO:
    vehicle_id = VEHICLE_MAPPING[vehicle]

    vehicle_id_count[vehicle_id] = Config.VEHICLES_RATIO[vehicle] * mul_factor

for floor in range(Config.FLOORS):
    print(f"creating floor {floor}")
    for vehicle in vehicle_id_count:
        num_slots = vehicle_id_count[vehicle]

        for _ in range(num_slots):
            pl = ParkingLot(floor=floor, category=vehicle)

            db.session.add(pl)


db.session.commit()
