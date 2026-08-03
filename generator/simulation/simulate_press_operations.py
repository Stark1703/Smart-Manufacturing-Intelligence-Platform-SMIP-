
"""
simulate_press_operations.py

Simulate Press Fitting Operations.

Author:
Sumanth Vempalle 

Version:
1.0.0
"""

from __future__ import annotations

import logging
import random
from dataclasses import asdict
from datetime import timedelta

import pandas as pd

from generator.configs.factory_digital_twin import (
    PressOperation,
    QualityResult,
)

from generator.configs.paths import (
    SERIAL_NUMBERS_PATH,
    PRESS_PROGRAMS_PATH,
    PRESS_OPERATIONS_PATH,
)

from generator.configs.simulation_config import (
    RANDOM_SEED,
    PRESS_OPERATION_PASS_RATE,
    PRESS_OPERATIONS_PER_PRODUCT,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)

random.seed(RANDOM_SEED)


# ============================================================
# Load Data
# ============================================================

def load_serial_numbers() -> pd.DataFrame:

    df = pd.read_csv(
        SERIAL_NUMBERS_PATH,
        parse_dates=[
            "manufacturing_date",
        ],
    )

    logger.info(
        "Loaded %d Serial Numbers.",
        len(df),
    )

    return df


def load_press_programs() -> pd.DataFrame:

    df = pd.read_csv(
        PRESS_PROGRAMS_PATH
    )

    logger.info(
        "Loaded %d Press Programs.",
        len(df),
    )

    return df


# ============================================================
# Simulation
# ============================================================

def simulate_press_operations(
    serial_numbers: pd.DataFrame,
    press_programs: pd.DataFrame,
) -> list[PressOperation]:

    operations: list[PressOperation] = []

    operation_counter = 1

    for _, serial in serial_numbers.iterrows():

        product_programs = press_programs[
            press_programs["product_code"]
            ==
            serial["product_code"]
        ].sort_values(
            "operation_number"
        )

        start_time = serial[
            "manufacturing_date"
        ]

        for _, program in product_programs.iterrows():

            target_force = float(
                program["target_force_kn"]
            )

            tolerance = float(
                program["force_tolerance_kn"]
            )

            actual_force = random.gauss(
                target_force,
                tolerance / 3,
            )

            displacement = random.uniform(
                program["target_displacement_mm"] - 1,
                program["target_displacement_mm"] + 1,
            )

            passed = (
                random.random()
                <=
                PRESS_OPERATION_PASS_RATE
            )

            quality = (
                QualityResult.PASS
                if passed
                else QualityResult.FAIL
            )

            cycle_time = int(
                program["maximum_cycle_time_sec"]
            )

            end_time = (
                start_time +
                timedelta(
                    seconds=cycle_time
                )
            )

            operations.append(

                PressOperation(

                    press_operation_id=(
                        f"PRESS-"
                        f"{operation_counter:08d}"
                    ),

                    serial_number=serial[
                        "serial_number"
                    ],

                    execution_id=serial[
                        "execution_id"
                    ],

                    work_order_id=serial[
                        "work_order_id"
                    ],

                    product_code=serial[
                        "product_code"
                    ],

                    program_id=program[
                        "program_id"
                    ],

                    operation_number=int(
                        program["operation_number"]
                    ),

                    operation_name=program[
                        "operation_name"
                    ],

                    target_force_kn=target_force,

                    actual_force_kn=round(
                        actual_force,
                        2,
                    ),

                    displacement_mm=round(
                        displacement,
                        2,
                    ),

                    result=quality.value,

                    start_time=start_time,

                    end_time=end_time,

                )

            )

            operation_counter += 1

            start_time = end_time

    logger.info(
        "Generated %d Press Operations.",
        len(operations),
    )

    return operations


# ============================================================
# Validation
# ============================================================

def validate(
    operations: list[PressOperation],
) -> None:

    df = pd.DataFrame(
        [asdict(x) for x in operations]
    )

    if df.empty:
        raise ValueError(
            "No press operations generated."
        )

    if df[
        "press_operation_id"
    ].duplicated().any():

        raise ValueError(
            "Duplicate Press Operation IDs."
        )

    logger.info(
        "Press Operation validation successful."
    )
