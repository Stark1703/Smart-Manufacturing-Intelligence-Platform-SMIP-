
"""
factory_config.py

Factory configuration used to simulate a GIS manufacturing shop floor.
"""

FACTORY = {

    "factory_name": "VoltGrid Manufacturing",

    "country": "Czech Republic",

    "city": "Brno",

    "production_lines": 6,

    "working_days_per_week": 5,

    "shifts_per_day": 3

}


PRODUCTION_LANES = {

    1: "Circuit Breaker Assembly",

    2: "Circuit Breaker Assembly",

    3: "Circuit Breaker Assembly",

    4: "Circuit Breaker Assembly",

    5: "Circuit Breaker Assembly",

    6: "Circuit Breaker Assembly"

}



PRODUCTS = {

    "GIS-72": {

        "rated_voltage_kv": 72.5,

        "target_force_kn": 145,

        "force_tolerance_kn": 5,

        "average_cycle_time_sec": 35

    },

    "GIS-145": {

        "rated_voltage_kv": 145,

        "target_force_kn": 170,

        "force_tolerance_kn": 6,

        "average_cycle_time_sec": 42

    },

    "GIS-245": {

        "rated_voltage_kv": 245,

        "target_force_kn": 195,

        "force_tolerance_kn": 8,

        "average_cycle_time_sec": 50

    },

    "GIS-420": {

        "rated_voltage_kv": 420,

        "target_force_kn": 220,

        "force_tolerance_kn": 10,

        "average_cycle_time_sec": 60

    }

}
