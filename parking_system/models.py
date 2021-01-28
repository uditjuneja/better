from datetime import date, datetime
from sqlalchemy import or_, func

from parking_system import db
from parking_system.status_codes import Responses
from parking_system.config import Config, VEHICLE_MAPPING


class ParkingLot(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    floor = db.Column(db.Integer, nullable=False)
    category = db.Column(db.Integer, nullable=False)

    vehicle_no = db.Column(db.String(120), nullable=True)
    colour = db.Column(db.String(120), nullable=True)

    entry_date = db.Column(db.Date, nullable=True)
    entry_time = db.Column(db.Time, nullable=True)

    @classmethod
    def enter_vehicle(cls, vehicle_no, colour, _type, entry_floor):
        """
        """
        if cls.query.filter_by(vehicle_no=vehicle_no).first():
            return Responses.vehicle_still_inside

        vehicle_type = VEHICLE_MAPPING.get(_type.upper(), 1)

        def find_lot(entry_floor, vehicle_type):
            """
            """
            for delta_floor in range(0, Config.FLOORS):
                lot = cls.query.filter(
                    or_(
                        cls.floor == entry_floor + delta_floor,
                        cls.floor == entry_floor - delta_floor,
                    ),
                    cls.category == vehicle_type,
                    cls.vehicle_no == None,
                ).first()

                if lot:
                    return lot

            return None

        lot = find_lot(entry_floor, vehicle_type)
        if lot:
            lot.vehicle_no = vehicle_no
            lot.colour = colour
            lot.entry_date = date.today()
            lot.entry_time = datetime.now().time()

            db.session.commit()

            response = Responses.vehicle_added
            response[0]['floor'] = lot.floor
            response[0]['lot'] = lot.id

        return response

    @classmethod
    def exit_vehicle(cls, vehicle_no):
        """
        """
        vehicle_entry = cls.query.filter_by(vehicle_no=vehicle_no).first()

        if not vehicle_entry:
            return Responses.vehivle_not_found

        entry_date, entry_time = vehicle_entry.entry_date, vehicle_entry.entry_time

        vehicle_entry.vehicle_no = None
        vehicle_entry.colour = None
        vehicle_entry.entry_date = None
        vehicle_entry.entry_time = None

        db.session.commit()

        return entry_date, entry_time

    @classmethod
    def get_detail_of_filled_slots(cls):
        """
        """

        vehicle_entries = cls.query.filter_by(vehicle_no=None)

        return vehicle_entries.count()
