from flask_restful import reqparse, Resource, request

from .funcs import (
    enter_vehicle,
    exit_vehicle,
    get_lot_details,
    floor_details_grouppeed,
    do_db_query,
)

lot_parser = reqparse.RequestParser()
lot_parser.add_argument("vehicle_no", help="This field cannot be blank", required=True)
lot_parser.add_argument("colour", help="This field cannot be blank", required=False)
lot_parser.add_argument("_type", help="This field cannot be blank", required=False)
lot_parser.add_argument(
    "entry_floor",
    help="This field cannot be blank",
    required=False,
    default=0,
    type=int,
)


class Parking(Resource):
    def get(self):
        columns = request.args.get("columns", "None")
        query = request.args.get("query", "")

        columns, query = eval(columns.strip()), query.strip()

        if not query:
            return get_lot_details()

        if not columns:
            columns = [
                "floor",
                "category",
                "vehicle_no",
                "colour",
                "entry_date",
                "entry_time",
            ]
        return do_db_query(query, columns)

    def post(self):
        data = lot_parser.parse_args()

        return enter_vehicle(data)

    def delete(self):
        data = lot_parser.parse_args()

        return exit_vehicle(data)


class Floors(Resource):
    def get(self):
        return floor_details_grouppeed()
