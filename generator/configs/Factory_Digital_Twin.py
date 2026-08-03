"""
factory_digital_twin.py

Digital Twin configuration for the Smart Manufacturing Lakehouse.

This file defines the structure of the manufacturing plant and all
master data used by the simulation engine.

Author:
Sumanth Vempalle

Version:
1.0
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


# =============================================================================
# ENUMS
# =============================================================================


class MachineStatus(Enum):
    ACTIVE = "Active"
    MAINTENANCE = "Maintenance"
    OUT_OF_SERVICE = "Out of Service"


class ShiftType(Enum):
    MORNING = "Morning"
    EVENING = "Evening"
    NIGHT = "Night"


class QualityResult(Enum):
    PASS = "PASS"
    FAIL = "FAIL"


class ProductFamily(Enum):
    GIS_BAY = "GIS Bay"
    CIRCUIT_BREAKER = "Circuit Breaker"
    DISCONNECTOR = "Disconnector"
    EARTHING_SWITCH = "Earthing Switch"
    CURRENT_TRANSFORMER = "Current Transformer"
    VOLTAGE_TRANSFORMER = "Voltage Transformer"


class MachineType(Enum):
    PRESS_FITTING = "Press Fitting Machine"
    CIRCUIT_BREAKER_ASSEMBLY = "Circuit Breaker Assembly"
    DEAD_TANK_ASSEMBLY = "Dead Tank Assembly"
    GIS_ASSEMBLY = "GIS Bay Assembly"
    VISUAL_INSPECTION = "Visual Inspection"
    MECHANICAL_TEST = "Mechanical Test Bench"
    HIGH_VOLTAGE_TEST = "High Voltage Test Bench"
    PRESSURE_TEST = "Pressure Leak Test Bench"
    PACKAGING = "Packaging Station"
  

class StationType(Enum):
    PRESS_FITTING = "Press Fitting"
    CIRCUIT_BREAKER_ASSEMBLY = "Circuit Breaker Assembly"
    DEAD_TANK_ASSEMBLY = "Dead Tank Assembly"
    GIS_ASSEMBLY = "GIS Bay Assembly"
    VISUAL_INSPECTION = "Visual Inspection"
    MECHANICAL_TEST = "Mechanical Test"
    HIGH_VOLTAGE_TEST = "HV Test"
    PRESSURE_TEST = "Pressure Test"
    PACKAGING = "Packaging"



class ToolType(Enum):
    PRESS_TOOL = "Press Tool"
    ASSEMBLY_FIXTURE = "Assembly Fixture"
    TORQUE_TOOL = "Torque Tool"
    INSPECTION_GAUGE = "Inspection Gauge"



class TestType(Enum):
    MECHANICAL = "Mechanical"
    DIELECTRIC = "Dielectric"
    PRESSURE = "Pressure Leak"



class MaintenanceType(Enum):
    PREVENTIVE = "Preventive"
    CORRECTIVE = "Corrective"
    PREDICTIVE = "Predictive"



class PackagingType(Enum):
    EXPORT_CRATE = "Export Wooden Crate"
    DOMESTIC = "Domestic Shipment"
    CONTAINER = "Container Shipment"



@dataclass(slots=True)
class Factory:

    factory_id: str

    name: str

    country: str

    city: str

    plant_code: str

    business_unit: str

    erp_system: str

    mes_system: str

    data_platform: str

    production_halls: int

    production_lines: int

    shifts: int


@dataclass(slots=True)
class ProductionHall:

    hall_id: str

    hall_name: str

    description: str



@dataclass(slots=True)
class ProductionLine:

    line_id: str

    hall_id: str

    line_name: str

    MachineStatus: str


@dataclass(slots=True)
class Station:

    station_id: str

    line_id: str

    station_code: str

    station_type: StationType

    sequence: int



@dataclass(slots=True)
class Machine:

    machine_id: str

    line_id: str

    station_id: str

    station_sequence: int

    machine_name: str

    machine_type: MachineType

    manufacturer: str

    status: MachineStatus

    commissioned_year: int


@dataclass(slots=True)
class Tool:

    tool_id: str

    machine_id: str

    tool_name: str

    tool_type: ToolType

    machine_type: MachineType

    calibration_interval_days: int

    last_calibration: Optional[str] = None

    next_calibration: Optional[str] = None

    status: MachineStatus = MachineStatus.ACTIVE


@dataclass(slots=True, frozen=True)
class Product:

    product_id: str
    product_code: str
    product_name: str
    family: ProductFamily

    rated_voltage_kv: float
    rated_current_a: int
    short_circuit_rating_ka: float

    target_force_kn: float
    force_tolerance_kn: float

    average_cycle_time_sec: int

    dielectric_test_voltage_kv: float
    pressure_test_bar: float



@dataclass(slots=True)
class PressProgram:

    program_id: str

    product_code: str

    tool_id: str

    machine_type: str

    target_force_kn: float

    force_tolerance_kn: float

    max_displacement_mm: float



@dataclass(slots=True)
class TestProgram:

    program_id: str

    product_code: str

    TestType: str

    target_value: float

    tolerance: float





@dataclass(slots=True)

class FactoryLayout:

    factory: Factory

    halls: list[ProductionHall]

    lines: list[ProductionLine]

    stations: list[Station]

    machines: list[Machine]

    tools: list[Tool]

    products: list[Product]

    press_programs: list[PressProgram]

    test_programs: list[TestProgram]



from dataclasses import asdict


def to_dict(objects: list) -> list[dict]:
    """
    Convert a list of dataclass objects into dictionaries.
    """
    return [asdict(obj) for obj in objects]


#def to_dict(objects):

    #return [asdict(obj) for obj in objects]


#generate_machine_layout()

#generate_products()

#generate_tools()

#generate_press_programs()

#build_factory()

