"""
production_planner.py

Production Planning Engine

Responsible for creating realistic SAP work orders for the
Smart Manufacturing Lakehouse.

Author:
Jason + ChatGPT

Version:
1.0.0
"""

from __future__ import annotations

import random

from datetime import datetime
from datetime import timedelta

import pandas as pd

from generator.configs.factory_digital_twin import (
    Priority,
    ShiftType,
    WorkOrder,
    WorkOrderStatus,
)

from generator.configs.simulation_config import (
    START_DATE,
    SIMULATION_DAYS,
    PRODUCT_SELECTION_WEIGHTS,
    MIN_WORK_ORDERS_PER_DAY,
    MAX_WORK_ORDERS_PER_DAY,
    PLANNER_NAME,
    ROUTING_VERSION,
    PRODUCTION_LINES,
    RANDOM_SEED,
)


class ProductionPlanner:

    """
    Production Planning Engine.
    """

    def __init__(self, products: pd.DataFrame):

        self.products = products

        self.random = random.Random(RANDOM_SEED)

        self.current_date = START_DATE

        self.work_order_counter = 1

        self.sap_counter = 5000000000

        self.line_counter = 0



    def generate(self) -> list[WorkOrder]:

        """
        Generate work orders for all simulation days.
        """

        work_orders = []

        for _ in range(SIMULATION_DAYS):

            work_orders.extend(
                self._generate_day()
            )

            self.current_date += timedelta(days=1)

        return work_orders



    def _generate_day(self) -> list[WorkOrder]:

        daily_orders = []

        count = self.random.randint(
            MIN_WORK_ORDERS_PER_DAY,
            MAX_WORK_ORDERS_PER_DAY,
        )

        release_time = datetime.combine(
            self.current_date,
            ShiftType.MORNING.start_time,
        )

        for index in range(count):

            daily_orders.append(

                self._create_work_order(
                    release_time + timedelta(
                        minutes=index * 20
                    )
                )

            )

        return daily_orders
          
      
 def _create_work_order(
        self,
        planned_start: datetime,
    ) -> WorkOrder:

        product = self._select_product()

        quantity = self._select_quantity(
            product["product_code"]
        )

        cycle = product["average_cycle_time_sec"]

        finish = planned_start + timedelta(
            minutes=max(quantity * cycle / 60, 30)
        )

        work_order = WorkOrder(

            work_order_id=self._next_work_order(),

            sap_order_number=self._next_sap(),

            product_code=product["product_code"],

            quantity=quantity,

            production_line=self._next_line(),

            priority=self._select_priority(),

            planned_shift=ShiftType.MORNING,

            planned_start=planned_start,

            planned_finish=finish,

            routing_version=ROUTING_VERSION,

            planner=PLANNER_NAME,

            status=WorkOrderStatus.RELEASED,

        )

        return work_order

    def _select_product(self):

        weights = PRODUCT_SELECTION_WEIGHTS

        codes = list(weights.keys())

        probabilities = list(weights.values())

        selected = self.random.choices(
            codes,
            weights=probabilities,
            k=1,
        )[0]

        return self.products.loc[
            self.products["product_code"] == selected
        ].iloc[0]

    def _select_quantity(
        self,
        product_code: str,
    ) -> int:

        if "072" in product_code:
            return self.random.randint(3,5)

        if "145" in product_code:
            return self.random.randint(2,4)

        if "170" in product_code:
            return self.random.randint(2,3)

        if "245" in product_code:
            return self.random.randint(1,3)

        if "300" in product_code:
            return self.random.randint(1,2)

        if "420" in product_code:
            return self.random.randint(1,2)

        return 1

    def _select_priority(self) -> Priority:

        priorities = [
            Priority.LOW,
            Priority.NORMAL,
            Priority.HIGH,
            Priority.URGENT,
        ]

        weights = [10,65,20,5]

        return self.random.choices(
            priorities,
            weights=weights,
            k=1,
        )[0]



    def _next_line(self) -> str:

        line = PRODUCTION_LINES[
            self.line_counter
        ]

        self.line_counter += 1

        if self.line_counter == len(PRODUCTION_LINES):
            self.line_counter = 0

        return line


    def _next_work_order(self) -> str:

        value = (
            f"WO-"
            f"{self.current_date:%Y%m%d}-"
            f"{self.work_order_counter:06d}"
        )

        self.work_order_counter += 1

        return value

    def _next_sap(self) -> str:

        self.sap_counter += 1

        return str(self.sap_counter)

planner = ProductionPlanner(products)

orders = planner.generate()
