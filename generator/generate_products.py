"""
generate_products.py

Generate the Product Master dataset for the Smart Manufacturing Lakehouse.

Pipeline
--------
factory_config.PRODUCTS
        ↓
create_product_records()
        ↓
create_products_dataframe()
        ↓
validate_products()
        ↓
save_products()
"""

# =============================================================================
# Imports
# =============================================================================

from typing import Any

import pandas as pd

from generator.configs.factory_config import PRODUCTS
from generator.configs.paths import PRODUCTS_PATH
from generator.logger import get_logger

# =============================================================================
# Logger
# =============================================================================

logger = get_logger(__name__)

# =============================================================================
# Constants
# =============================================================================

REQUIRED_COLUMNS = [
    "product_id",
    "product_code",
    "product_name",
    "rated_voltage_kv",
    "circuit_breaker_type",
    "target_force_kn",
    "force_tolerance_kn",
    "average_cycle_time_sec",
    "dielectric_test_voltage_kv",
    "pressure_test_bar",
    "status",
    "created_at",
]

COLUMN_ORDER = REQUIRED_COLUMNS.copy()

# =============================================================================
# Helper Functions
# =============================================================================


def _validate_required_columns(df: pd.DataFrame) -> None:
    """
    Validate that all required columns exist.
    """
    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )


def _check_duplicates(df: pd.DataFrame, column: str) -> None:
    """
    Raise an exception if duplicate values exist.
    """
    duplicates = df[df.duplicated(subset=[column], keep=False)]

    if not duplicates.empty:
        raise ValueError(
            f"Duplicate values found in '{column}': "
            f"{duplicates[column].tolist()}"
        )


def _check_nulls(df: pd.DataFrame) -> None:
    """
    Raise an exception if null values exist.
    """
    null_columns = df.columns[df.isnull().any()].tolist()

    if null_columns:
        raise ValueError(
            f"Null values found in columns: {null_columns}"
        )


def _check_positive(df: pd.DataFrame, column: str) -> None:
    """
    Ensure numeric column contains only positive values.
    """
    invalid_rows = df[df[column] <= 0]

    if not invalid_rows.empty:
        raise ValueError(
            f"Column '{column}' contains non-positive values."
        )


# =============================================================================
# Generator Functions
# =============================================================================


def create_product_records() -> list[dict[str, Any]]:
    """
    Load product definitions from the factory configuration.

    Returns
    -------
    list[dict[str, Any]]
        Product master records.
    """
    logger.info("Loading product definitions from factory configuration.")

    return list(PRODUCTS)


def create_products_dataframe(
    records: list[dict[str, Any]]
) -> pd.DataFrame:
    """
    Convert product records into a pandas DataFrame.
    """
    df = pd.DataFrame(records)

    df = df[COLUMN_ORDER]

    return df


# =============================================================================
# Validation
# =============================================================================


def validate_products(df: pd.DataFrame) -> None:
    """
    Validate the Product Master dataset.
    """
    logger.info("Validating product master dataset.")

    _validate_required_columns(df)

    _check_duplicates(df, "product_id")

    _check_nulls(df)

    _check_positive(df, "rated_voltage_kv")

    _check_positive(df, "target_force_kn")

    _check_positive(df, "force_tolerance_kn")

    _check_positive(df, "average_cycle_time_sec")

    _check_positive(df, "dielectric_test_voltage_kv")

    _check_positive(df, "pressure_test_bar")

    logger.info("Validation completed successfully.")


# =============================================================================
# Save
# =============================================================================


def save_products(df: pd.DataFrame) -> None:
    """
    Save Product Master dataset to CSV.
    """
    PRODUCTS_PATH.mkdir(parents=True, exist_ok=True)

    output_file = PRODUCTS_PATH / "products.csv"

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )

    logger.info("Saved dataset to %s", output_file)


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    """
    Execute the Product Master generation pipeline.
    """
    logger.info("=" * 70)
    logger.info("Generating Product Master Dataset")
    logger.info("=" * 70)

    records = create_product_records()

    logger.info("Loaded %d products.", len(records))

    df = create_products_dataframe(records)

    validate_products(df)

    save_products(df)

    logger.info("Product Master generation completed successfully.")


if __name__ == "__main__":
    main()
