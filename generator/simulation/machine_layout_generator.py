"""
generate_machine_layout.py

Generate the complete machine layout for the Smart Manufacturing Lakehouse.

Author:
Sumanth Vempalle

Version:
1.0.0
"""

from __future__ import annotations

import logging

from generator.configs.factory_digital_twin import (
    Machine,
    MachineStatus,
    MachineType,
    ProductionHall,
    ProductionLine,
    Station,
    StationType,
)

# =============================================================================
# Logging
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)

# =============================================================================
# Factory Configuration
# =============================================================================

NUMBER_OF_HALLS = 2
LINES_PER_HALL = 3

HALL_NAMES = [
    "Production Hall A",
    "Production Hall B",
]

# =============================================================================
# Station Templates
# =============================================================================

STATION_TEMPLATES = [
    ("S10", 10, StationType.PRESS_FITTING),
    ("S20", 20, StationType.CIRCUIT_BREAKER_ASSEMBLY),
    ("S30", 30, StationType.DEAD_TANK_ASSEMBLY),
    ("S40", 40, StationType.GIS_ASSEMBLY),
    ("S50", 50, StationType.VISUAL_INSPECTION),
    ("S60", 60, StationType.MECHANICAL_TEST),
    ("S70", 70, StationType.HIGH_VOLTAGE_TEST),
    ("S80", 80, StationType.PRESSURE_TEST),
    ("S90", 90, StationType.PACKAGING),
]

# =============================================================================
# Machine Templates
# =============================================================================

MACHINE_TEMPLATES = [
    {
        "station": StationType.PRESS_FITTING,
        "prefix": "PF",
        "name": "Press Fitting Machine",
        "manufacturer": "Kistler",
        "machine_type": MachineType.PRESS_FITTING,
    },
    {
        "station": StationType.CIRCUIT_BREAKER_ASSEMBLY,
        "prefix": "ASM",
        "name": "Circuit Breaker Assembly Station",
        "manufacturer": "VoltGrid",
        "machine_type": MachineType.CIRCUIT_BREAKER_ASSEMBLY,
    },
    {
        "station": StationType.DEAD_TANK_ASSEMBLY,
        "prefix": "DTA",
        "name": "Dead Tank Assembly Station",
        "manufacturer": "VoltGrid",
        "machine_type": MachineType.DEAD_TANK_ASSEMBLY,
    },
    {
        "station": StationType.GIS_ASSEMBLY,
        "prefix": "GBA",
        "name": "GIS Bay Assembly Station",
        "manufacturer": "VoltGrid",
        "machine_type": MachineType.GIS_ASSEMBLY,
    },
    {
        "station": StationType.VISUAL_INSPECTION,
        "prefix": "VIS",
        "name": "Visual Inspection Station",
        "manufacturer": "Keyence",
        "machine_type": MachineType.VISUAL_INSPECTION,
    },
    {
        "station": StationType.MECHANICAL_TEST,
        "prefix": "MOT",
        "name": "Mechanical Test Bench",
        "manufacturer": "ABB",
        "machine_type": MachineType.MECHANICAL_TEST,
    },
    {
        "station": StationType.HIGH_VOLTAGE_TEST,
        "prefix": "HVT",
        "name": "High Voltage Test Bench",
        "manufacturer": "Haefely",
        "machine_type": MachineType.HIGH_VOLTAGE_TEST,
    },
    {
        "station": StationType.PRESSURE_TEST,
        "prefix": "PLT",
        "name": "Pressure Leak Test Bench",
        "manufacturer": "ATEQ",
        "machine_type": MachineType.PRESSURE_TEST,
    },
    {
        "station": StationType.PACKAGING,
        "prefix": "PKG",
        "name": "Packaging Station",
        "manufacturer": "VoltGrid",
        "machine_type": MachineType.PACKAGING,
    },
]

# =============================================================================
# Helper Functions
# =============================================================================

def line_id(line_number: int) -> str:
    """Return formatted production line ID."""
    return f"LINE-{line_number:02d}"


def hall_id(hall_number: int) -> str:
    """Return formatted production hall ID."""
    return f"HALL-{hall_number:02d}"


def machine_id(prefix: str, line_number: int, station_code: str) -> str:
    """Return formatted machine ID."""
    return f"{prefix}-L{line_number}-{station_code}"


def station_id(line_number: int, station_code: str) -> str:
    """Return formatted station ID."""
    return f"L{line_number}-{station_code}"


def get_machine_template(station_type: StationType) -> dict:
    """
    Return the machine template associated with a station type.
    """
    for template in MACHINE_TEMPLATES:
        if template["station"] == station_type:
            return template

    raise ValueError(f"No machine template defined for {station_type}")





# =============================================================================
# Production Hall Generator
# =============================================================================

def generate_production_halls() -> list[ProductionHall]:
    """
    Generate all production halls in the factory.
    """
    halls: list[ProductionHall] = []

    for hall_number in range(1, NUMBER_OF_HALLS + 1):

        halls.append(
            ProductionHall(
                hall_id=hall_id(hall_number),
                hall_name=HALL_NAMES[hall_number - 1],
                description=f"Main manufacturing hall {hall_number}",
            )
        )

    logger.info("Generated %d production halls", len(halls))

    return halls


# =============================================================================
# Production Line Generator
# =============================================================================

def generate_production_lines() -> list[ProductionLine]:
    """
    Generate all production lines.

    Hall 1
        LINE-01
        LINE-02
        LINE-03

    Hall 2
        LINE-04
        LINE-05
        LINE-06
    """

    lines: list[ProductionLine] = []

    line_number = 1

    for hall_number in range(1, NUMBER_OF_HALLS + 1):

        current_hall = hall_id(hall_number)

        for _ in range(LINES_PER_HALL):

            lines.append(
                ProductionLine(
                    line_id=line_id(line_number),
                    hall_id=current_hall,
                    line_name=f"Production Line {line_number}",
                    description=f"GIS Assembly Production Line {line_number}",
                    status=MachineStatus.ACTIVE,
                )
            )

            line_number += 1

    logger.info("Generated %d production lines", len(lines))

    return lines


# =============================================================================
# Station Generator
# =============================================================================

def generate_stations() -> list[Station]:
    """
    Generate all stations for every production line.

    Every line contains:

        S10 Press Fitting
        S20 Circuit Breaker Assembly
        S30 Dead Tank Assembly
        S40 GIS Assembly
        S50 Visual Inspection
        S60 Mechanical Test
        S70 High Voltage Test
        S80 Pressure Test
        S90 Packaging
    """

    stations: list[Station] = []

    total_lines = NUMBER_OF_HALLS * LINES_PER_HALL

    for line_number in range(1, total_lines + 1):

        for station_code, sequence, station_type in STATION_TEMPLATES:

            stations.append(
                Station(
                    station_id=station_id(
                        line_number=line_number,
                        station_code=station_code,
                    ),
                    line_id=line_id(line_number),
                    station_code=station_code,
                    station_type=station_type,
                    sequence=sequence,
                )
            )

    logger.info("Generated %d stations", len(stations))

    return stations
