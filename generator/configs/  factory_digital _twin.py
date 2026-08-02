"""
factory_config.py

Central configuration for the Smart Manufacturing Lakehouse.

Author: sumanth VEMPALLE
Version: 1.0.0
"""

# =============================================================================
# FACTORY INFORMATION
# =============================================================================

FACTORY = {
    "factory_id": "FG-001",
    "factory_name": "VoltGrid Manufacturing",
    "business_unit": "Grid Solutions",
    "country": "Czech Republic",
    "city": "Brno",
    "plant_code": "CZ-BR-01",
    "erp_system": "SAP S/4HANA",
    "mes_system": "Manufacturing Execution System",
    "data_platform": "Azure Databricks",
    "production_lines": 6,
    "working_days_per_week": 5,
    "shifts_per_day": 3,
}

# =============================================================================
# WORKING CALENDAR
# =============================================================================

WORKING_CALENDAR = {
    "working_days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
    ],
    "weekend": [
        "Saturday",
        "Sunday",
    ],
    "shift_duration_hours": 8,
    "planned_break_minutes": 30,
}



# =============================================================================
# SHIFT DEFINITIONS
# =============================================================================

SHIFTS = [
    {
        "shift_id": "S1",
        "shift_name": "Morning",
        "start_time": "06:00",
        "end_time": "14:00",
    },
    {
        "shift_id": "S2",
        "shift_name": "Evening",
        "start_time": "14:00",
        "end_time": "22:00",
    },
    {
        "shift_id": "S3",
        "shift_name": "Night",
        "start_time": "22:00",
        "end_time": "06:00",
    },
]

# =============================================================================
# PRODUCT FAMILIES
# =============================================================================

PRODUCT_FAMILIES = [
    "Circuit Breaker",
    "Disconnect Switch",
    "Earthing Switch",
    "Current Transformer",
    "Voltage Transformer",
    "Busbar Module",
    "GIS Bay",
]


# =============================================================================
# PRODUCTION LINES
# =============================================================================

PRODUCTION_LINES = [
    {
        "line_id": "LINE-01",
        "line_name": "Production Lane 1",
        "description": "Circuit Breaker & GIS Bay Assembly",
        "status": "Active"
    },
    {
        "line_id": "LINE-02",
        "line_name": "Production Lane 2",
        "description": "Circuit Breaker & GIS Bay Assembly",
        "status": "Active"
    },
    {
        "line_id": "LINE-03",
        "line_name": "Production Lane 3",
        "description": "Circuit Breaker & GIS Bay Assembly",
        "status": "Active"
    },
    {
        "line_id": "LINE-04",
        "line_name": "Production Lane 4",
        "description": "Circuit Breaker & GIS Bay Assembly",
        "status": "Active"
    },
    {
        "line_id": "LINE-05",
        "line_name": "Production Lane 5",
        "description": "Circuit Breaker & GIS Bay Assembly",
        "status": "Active"
    },
    {
        "line_id": "LINE-06",
        "line_name": "Production Lane 6",
        "description": "Circuit Breaker & GIS Bay Assembly",
        "status": "Active"
    },
]


# =============================================================================
# SHOP FLOOR WORKFLOW
# =============================================================================

SHOP_FLOOR_WORKFLOW = [
    {
        "step": 1,
        "station": "Press Fitting",
        "station_code": "PF"
    },
    {
        "step": 2,
        "station": "Circuit Breaker Assembly",
        "station_code": "CBA"
    },
    {
        "step": 3,
        "station": "Dead Tank Assembly",
        "station_code": "DTA"
    },
    {
        "step": 4,
        "station": "GIS Bay Assembly",
        "station_code": "GBA"
    },
    {
        "step": 5,
        "station": "Visual Inspection",
        "station_code": "VIS"
    },
    {
        "step": 6,
        "station": "Mechanical Operation Test",
        "station_code": "MOT"
    },
    {
        "step": 7,
        "station": "High Voltage Dielectric Test",
        "station_code": "HVT"
    },
    {
        "step": 8,
        "station": "Pressure / Leak Test",
        "station_code": "PLT"
    },
    {
        "step": 9,
        "station": "Packaging",
        "station_code": "PKG"
    }
]



# =============================================================================
# MACHINE TYPES
# =============================================================================

MACHINE_TYPES = [
    "Press Fitting Machine",
    "Assembly Station",
    "Visual Inspection Station",
    "Mechanical Test Bench",
    "High Voltage Test Bench",
    "Pressure Leak Test Bench",
    "Packaging Station"
]





# =============================================================================
# MACHINE LAYOUT
# =============================================================================

MACHINE_LAYOUT = {

    "LINE-01": [
        "PF-01",
        "ASM-01",
        "VIS-01",
        "MOT-01",
        "HVT-01",
        "PLT-01",
        "PKG-01",
    ],

    "LINE-02": [
        "PF-02",
        "ASM-02",
        "VIS-02",
        "MOT-02",
        "HVT-02",
        "PLT-02",
        "PKG-02",
    ],

    "LINE-03": [
        "PF-03",
        "ASM-03",
        "VIS-03",
        "MOT-03",
        "HVT-03",
        "PLT-03",
        "PKG-03",
    ],

    "LINE-04": [
        "PF-04",
        "ASM-04",
        "VIS-04",
        "MOT-04",
        "HVT-04",
        "PLT-04",
        "PKG-04",
    ],

    "LINE-05": [
        "PF-05",
        "ASM-05",
        "VIS-05",
        "MOT-05",
        "HVT-05",
        "PLT-05",
        "PKG-05",
    ],

    "LINE-06": [
        "PF-06",
        "ASM-06",
        "VIS-06",
        "MOT-06",
        "HVT-06",
        "PLT-06",
        "PKG-06",
    ]
}




MACHINES = [

    {
        "machine_id": "PF-01",
        "machine_name": "Press Fitting Machine 01",
        "line_id": "LINE-01",
        "machine_type": "Press Fitting Machine",
        "manufacturer": "Kistler",
        "status": "Active",
        "commissioned_year": 2023,
    },

    {
        "machine_id": "ASM-01",
        "machine_name": "Assembly Station 01",
        "line_id": "LINE-01",
        "machine_type": "Assembly Station",
        "manufacturer": "VoltGrid",
        "status": "Active",
        "commissioned_year": 2023,
    },

    {
        "machine_id": "VIS-01",
        "machine_name": "Visual Inspection Station 01",
        "line_id": "LINE-01",
        "machine_type": "Visual Inspection Station",
        "manufacturer": "Keyence",
        "status": "Active",
        "commissioned_year": 2023,
    },

    {
        "machine_id": "MOT-01",
        "machine_name": "Mechanical Test Bench 01",
        "line_id": "LINE-01",
        "machine_type": "Mechanical Test Bench",
        "manufacturer": "ABB",
        "status": "Active",
        "commissioned_year": 2023,
    },

    {
        "machine_id": "HVT-01",
        "machine_name": "High Voltage Test Bench 01",
        "line_id": "LINE-01",
        "machine_type": "High Voltage Test Bench",
        "manufacturer": "Haefely",
        "status": "Active",
        "commissioned_year": 2023,
    },

    {
        "machine_id": "PLT-01",
        "machine_name": "Pressure Leak Test Bench 01",
        "line_id": "LINE-01",
        "machine_type": "Pressure Leak Test Bench",
        "manufacturer": "ATEQ",
        "status": "Active",
        "commissioned_year": 2023,
    },

    {
        "machine_id": "PKG-01",
        "machine_name": "Packaging Station 01",
        "line_id": "LINE-01",
        "machine_type": "Packaging Station",
        "manufacturer": "VoltGrid",
        "status": "Active",
        "commissioned_year": 2023,
    },

]














