
def main():

    logger.info("Starting Work Order Simulation")

    products = load_products()

    planner = ProductionPlanner(products)

    work_orders = planner.generate()

    validate(work_orders)

    export(work_orders)

    logger.info("Simulation completed")
