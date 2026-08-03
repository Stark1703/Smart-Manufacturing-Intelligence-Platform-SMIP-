
"""
generate_machine_layout.py

Generate the complete machine layout for the Smart Manufacturing Lakehouse.

This module creates production halls, production lines, stations,
and machines from the Digital Twin configuration.

Author:
Sumanth Vempalle

Version:
1.0
"""

# =============================================================================
# Imports
# =============================================================================

from __future__ import annotations

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
# Factory Constants
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
        "prefix": "PF",
        "name": "Press Fitting Machine",
        "manufacturer": "Kistler",
        "type": MachineType.PRESS_FITTING,
    },
    {
        "prefix": "ASM",
        "name": "Circuit Breaker Assembly Station",
        "manufacturer": "VoltGrid",
        "type": MachineType.CIRCUIT_BREAKER_ASSEMBLY,
    },
    {
        "prefix": "DTA",
        "name": "Dead Tank Assembly Station",
        "manufacturer": "VoltGrid",
        "type": MachineType.DEAD_TANK_ASSEMBLY,
    },
    {
        "prefix": "GBA",
        "name": "GIS Bay Assembly Station",
        "manufacturer": "VoltGrid",
        "type": MachineType.GIS_ASSEMBLY,
    },
    {
        "prefix": "VIS",
        "name": "Visual Inspection Station",
        "manufacturer": "Keyence",
        "type": MachineType.VISUAL_INSPECTION,
    },
    {
        "prefix": "MOT",
        "name": "Mechanical Test Bench",
        "manufacturer": "ABB",
        "type": MachineType.MECHANICAL_TEST,
    },
    {
        "prefix": "HVT",
        "name": "High Voltage Test Bench",
        "manufacturer": "Haefely",
        "type": MachineType.HIGH_VOLTAGE_TEST,
    },
    {
        "prefix": "PLT",
        "name": "Pressure Leak Test Bench",
        "manufacturer": "ATEQ",
        "type": MachineType.PRESSURE_TEST,
    },
    {
        "prefix": "PKG",
        "name": "Packaging Station",
        "manufacturer": "VoltGrid",
        "type": MachineType.PACKAGING,
    },
]
