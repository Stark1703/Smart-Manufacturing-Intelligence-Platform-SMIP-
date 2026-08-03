
from pathlib import Path

# ============================================================
# Project Root
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ============================================================
# Dataset Paths
# ============================================================

DATASETS = PROJECT_ROOT / "datasets"

RAW_DATA = DATASETS / "raw"

BRONZE_DATA = DATASETS / "bronze"

SILVER_DATA = DATASETS / "silver"

GOLD_DATA = DATASETS / "gold"

# ============================================================
# Raw Source Paths
# ============================================================

PRODUCTS_PATH = RAW_DATA / "products"

MACHINES_PATH = RAW_DATA / "machines"

OPERATORS_PATH = RAW_DATA / "operators"

TOOLS_PATH = RAW_DATA / "tools"

WORK_ORDERS_PATH = RAW_DATA / "work_orders"

PRESSFIT_PATH = RAW_DATA / "pressfit"

FORCE_CURVES_PATH = RAW_DATA / "force_curves"

ASSEMBLY_PATH = RAW_DATA / "assembly"

TESTING_PATH = RAW_DATA / "testing"

PACKAGING_PATH = RAW_DATA / "packaging"

from pathlib import Path

DATA_ROOT = Path("data")

MASTER_DATA = DATA_ROOT / "master_data"

MACHINES_PATH = MASTER_DATA / "machines.csv"
HALLS_PATH = MASTER_DATA / "production_halls.csv"
LINES_PATH = MASTER_DATA / "production_lines.csv"
STATIONS_PATH = MASTER_DATA / "stations.csv"
TOOLS_PATH = MASTER_DATA / "tools.csv"
OPERATORS_PATH = MASTER_DATA / "operators.csv"
PRESS_PROGRAMS_PATH = MASTER_DATA / "press_programs.csv"
OPERATIONS_PATH = MASTER_DATA / "operations.csv"
TEST_PROGRAMS_PATH = MASTER_DATA / "test_programs.csv"
WORK_ORDERS_PATH = TRANSACTIONAL_DATA / "work_orders.csv"
TRANSACTIONAL_DATA = DATA_ROOT / "transactional_data"
