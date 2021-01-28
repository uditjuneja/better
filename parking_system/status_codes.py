class Responses:
    vehicle_added = (
        {
            "code": "S0001",
            "message": "Vehicle Added to DB and Entered",
            "floor": None,
            "lot": None,
        },
        True,
    )
    vehicle_entered = ({"code": "S0002", "message": "Vehicle Entered"}, True)

    vehicle_exited = ({"code": "S0003", "message": "Vehicle Exited"}, True)

    vehicle_still_inside = (
        {"code": "F0001", "message": "Vehicle still in parking"},
        False,
    )
    vehivle_not_found = ({"code": "F0002", "message": "Vehicle not in parking"}, False)
    LOT_FULL = (
        {"code": "F0003", "message": "No emplty slot for this particular vehicle"},
        False,
    )
