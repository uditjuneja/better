from .models import ParkingLot
from .db import parse_query


def get_lot_details(data):
    """
    """
    ...


def enter_vehicle(data):
    """
    """
    response = ParkingLot.enter_vehicle(
        data["vehicle_no"], data["colour"], data["_type"], data["entry_floor"]
    )

    print(response)

    if response[-1]:
        return response[0], 200

    return response[0], 401


def exit_vehicle(data):
    """
    """
    response = ParkingLot.exit_vehicle(data["vehicle_no"])

    if response[-1]:
        return response[0], 200

    return response[0], 401
