class Config:
    SECRET_KEY = ""
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"

    FLOORS = 10
    SPACE_ON_A_FLOOR = 10

    TOTAL_SPACE = FLOORS * SPACE_ON_A_FLOOR

    VEHICLES_RATIO = {"CAR": 6, "BIKE": 3, "TRUCK": 1}


VEHICLE_MAPPING = {"CAR": 1, "BIKE": 2, "TRUCK": 3}
