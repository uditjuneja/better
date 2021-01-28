from flask_restful import reqparse, Resource, request

from .funcs import enter_vehicle, exit_vehicle

lot_parser = reqparse.RequestParser()
lot_parser.add_argument("vehicle_no", help="This field cannot be blank", required=True)
lot_parser.add_argument("colour", help="This field cannot be blank", required=False)
lot_parser.add_argument("_type", help="This field cannot be blank", required=False)
lot_parser.add_argument(
    "entry_floor", help="This field cannot be blank", required=False, default=0, type=int
)


class Parking(Resource):
    def get(self):
        columns = request.args.get("col", "*")
        query = request.args.get("query", "")

        columns, query = columns.strip(), query.strip()

        return f"{columns} -- {query}"

    def post(self):
        data = lot_parser.parse_args()

        return enter_vehicle(data)

    def delete(self):
        data = lot_parser.parse_args()

        return exit_vehicle(data)


class Floor(Resource):
    def get(self, floor):
        columns = request.args.get("col", "*")
        query = request.args.get("query", "")

        columns, query = columns.strip(), query.strip()

        return f"{columns} -- {query}"
