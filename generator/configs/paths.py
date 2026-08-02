
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
