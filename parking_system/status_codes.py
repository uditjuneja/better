class Responses:
    VehicleEntered = (
        {
            "code": "S0001",
            "message": "Vehicle Added to DB and Entered",
            "floor": None,
            "lot": None,
        },
        True,
    )
    VehicleEntered = ({"code": "S0002", "message": "Vehicle Entered"}, True)

    VehicleExited = ({"code": "S0003", "message": "Vehicle Exited"}, True)

    VehicleStillInside = (
        {"code": "F0001", "message": "Vehicle still in parking"},
        False,
    )
    VehicleNotFound = ({"code": "F0002", "message": "Vehicle not in parking"}, False)
    LOT_FULL = (
        {"code": "F0003", "message": "No emplty slot for this particular vehicle"},
        False,
    )
