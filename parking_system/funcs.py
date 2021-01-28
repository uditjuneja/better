from flask import jsonify
from sqlalchemy import text

from parking_system import db
from .models import ParkingLot
from .db import parse_query


def get_lot_details():
    """
    """
    return ParkingLot.get_detail_of_unfilled_slots()


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


def do_db_query(query, columns):
    parsed_query = parse_query(query)

    query_results = (
        db.session.query(ParkingLot).from_statement(text(parsed_query)).all()
    )

    response = {"result": []}

    for query_result in query_results:
        obj = {}
        for col in columns:
            obj[col] = eval(f"query_result.{col}")
        response["result"].append(obj)

    return response


def floor_details_grouppeed():
    return ParkingLot.get_detail_floor_wise()
