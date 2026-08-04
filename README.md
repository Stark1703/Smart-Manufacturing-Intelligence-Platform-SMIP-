# 🏭 Smart Manufacturing Intelligence Platform (SMIP)



![System Architecture](docs/images/architecture/system_architecture.svg)



A complete end-to-end Smart Manufacturing Digital Twin and Manufacturing Execution System (MES) simulation platform built using Python, SQL, and Databricks-ready data pipelines.

The project generates realistic synthetic manufacturing data representing a high-voltage electrical equipment factory, including production planning, manufacturing execution, quality testing, IoT force curves, packaging, and full product traceability.

The generated datasets are designed for:

- Manufacturing Analytics
- Manufacturing Execution Systems (MES)
- Factory Digital Twin
- Industrial IoT
- Predictive Maintenance
- Process Mining
- Power BI Dashboards
- Databricks Lakehouse
- Machine Learning

---

# 📌 Project Overview

The Smart Manufacturing Intelligence Platform simulates the complete lifecycle of manufacturing operations inside a modern industrial plant.

The project reproduces realistic manufacturing processes including:

- SAP Work Order generation
- Production Execution
- Operator Login
- Material Barcode/RFID Scan
- Press-Fit Operations
- IoT Force Curve Acquisition
- Quality Testing
- Packaging
- Product Traceability

The objective is to create a realistic manufacturing dataset that can be used for analytics, visualization, machine learning, and digital twin applications.

---

# 🏭 Simulated Manufacturing Process

```text
                        ERP (SAP)
                            │
                            ▼
                     Work Orders
                            │
                            ▼
                Production Executions
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
 Operator Login      Material Scan      Serial Numbers
                                                │
                         ┌──────────────────────┼──────────────────────┐
                         ▼                      ▼                      ▼
                 Press Operations        Test Results           Packaging
                         │
                         ▼
                 Force Curve Acquisition
                 (Industrial IoT Dataset)
```

---

# 🚀 Features

## Master Data Generation

- Factory Layout
- Production Halls
- Production Lines
- Stations
- Machines
- Operators
- Products
- Tools
- Manufacturing Operations
- Press Programs
- Test Programs

## Manufacturing Simulation

- Production Planning
- Work Order Generation
- Production Execution
- Operator Login Simulation
- Material Barcode Scan
- Serial Number Generation
- Press Operation Simulation
- Force Curve Simulation
- Quality Testing
- Packaging Simulation

## Analytics Ready

The generated data is structured for:

- Databricks Lakehouse
- Delta Tables
- SQL Analytics
- Power BI
- Manufacturing KPIs
- OEE
- Quality Analysis
- Traceability
- Process Mining

---

# 📂 Repository Structure

```
Smart-Manufacturing-Intelligence-Platform-SMIP/
│
├── dashboard/
│   └── png/
│
├── data/
│   ├── master_data/
│   ├── transactional_data/
│   └── analytics/
│
├── datasets/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── tests/
│
├── docs/
│   ├── architecture/
│   ├── data_model/
│   ├── meeting_notes/
│   └── README_assets/
│
├── generator/
│   ├── configs/
│   ├── engine/
│   ├── master_data/
│   └── simulation/
│
├── notebooks/
│
├── sql/
│   ├── ddl/
│   ├── analytics/
│   └── views/
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

# 📁 Repository Description

## generator/

Contains the synthetic manufacturing data generation engine.

### configs/

Configuration files and Digital Twin definitions.

- Factory Digital Twin
- Dataclasses
- Enumerations
- Paths
- Manufacturing Constants
- Simulation Configuration

---

### engine/

Core manufacturing business logic.

- Production Planner
- Scheduler
- Routing Engine
- Quality Engine
- Time Generator

---

### master_data/

Generates all factory master data.

- Factory Layout
- Machines
- Products
- Operators
- Tools
- Operations
- Press Programs
- Test Programs

---

### simulation/

Generates manufacturing transactional data.

- Work Orders
- Production Executions
- Operator Logins
- Material Scans
- Serial Numbers
- Press Operations
- Force Curves
- Test Results
- Packaging

---

## data/

Stores generated CSV datasets.

```
data/
│
├── master_data/
│
│   machines.csv
│   production_halls.csv
│   production_lines.csv
│   stations.csv
│   operators.csv
│   products.csv
│   tools.csv
│   operations.csv
│   press_programs.csv
│   test_programs.csv
│
└── transactional_data/
    work_orders.csv
    production_executions.csv
    operator_logins.csv
    material_scans.csv
    serial_numbers.csv
    press_operations.csv
    force_curves.csv
    testing_results.csv
    packaging.csv
```

---

## datasets/

Databricks Lakehouse storage.

```
Raw
   │
   ▼
Bronze
   │
   ▼
Silver
   │
   ▼
Gold
```

This directory is used by Databricks notebooks for ETL processing.

---

## notebooks/

Databricks notebooks implementing the Medallion Architecture.

```
01 Bronze Ingestion

↓

02 Silver Transformation

↓

03 Gold KPIs
```

---

## sql/

SQL scripts used for:

- Database DDL
- Views
- KPI Queries
- Analytics

---

## docs/

Project documentation.

Includes:

- Architecture
- Functional Design
- Technical Design
- Data Model
- KPI Definitions
- Future Roadmap

---


# 📊 Generated Datasets

The platform generates both **Master Data** and **Transactional Data** representing a complete manufacturing execution process.

---

# Master Data

| Dataset | Description |
|----------|-------------|
| production_halls.csv | Production halls within the factory |
| production_lines.csv | Manufacturing production lines |
| stations.csv | Workstations inside each production line |
| machines.csv | Manufacturing machines and equipment |
| operators.csv | Operator master data |
| products.csv | High-voltage product catalog |
| tools.csv | Press tools and fixtures |
| operations.csv | Manufacturing routing operations |
| press_programs.csv | Press-fit machine programs |
| test_programs.csv | Quality test specifications |

---

# Transactional Data

| Dataset | Description |
|----------|-------------|
| work_orders.csv | ERP production work orders |
| production_executions.csv | MES production execution records |
| operator_logins.csv | Operator login/logout sessions |
| material_scans.csv | Material barcode/RFID scans |
| serial_numbers.csv | Manufactured product serial numbers |
| press_operations.csv | Press-fit operation results |
| force_curves.csv | High-frequency force curve samples |
| testing_results.csv | Manufacturing quality inspection results |
| packaging.csv | Packaging and shipment records |

---

# 📈 Generated Record Counts

The default simulation generates approximately:

| Dataset | Records |
|----------|---------:|
| Products | 12 |
| Machines | 54 |
| Operators | 72 |
| Work Orders | 640 |
| Production Executions | 640 |
| Operator Logins | 640 |
| Material Scans | 1,803 |
| Serial Numbers | 1,803 |
| Press Operations | 7,212 |
| Test Results | 5,409 |
| Packaging Records | 1,803 |
| Force Curve Points | **3,606,000** |

The number of generated records can be increased by modifying the simulation configuration.

---

# 🔄 Manufacturing Data Flow

The simulation reproduces the complete lifecycle of a manufactured product.

```text
ERP (SAP)
    │
    ▼
Work Orders
    │
    ▼
Production Executions
    │
    ├─────────────┐
    ▼             ▼
Operator Login   Material Scan
    │             │
    └──────┬──────┘
           ▼
     Serial Numbers
           │
           ▼
   Press Operations
           │
           ▼
    Force Curve Data
           │
           ▼
     Quality Testing
           │
           ▼
       Packaging
           │
           ▼
 Ready for Shipment
```

---

# 🔗 Entity Relationships

```text
Factory
│
├── Production Hall
│      │
│      ├── Production Line
│      │        │
│      │        ├── Station
│      │        │      │
│      │        │      └── Machine
│      │        │
│      │        └── Work Order
│      │               │
│      │               ▼
│      │        Production Execution
│      │               │
│      │               ▼
│      │         Serial Number
│      │               │
│      │      ┌────────┼─────────┐
│      │      ▼        ▼         ▼
│      │ Press Ops   Testing   Packaging
│      │      │
│      │      ▼
│      │ Force Curves
│      │
│      └── Operators
│
└── Products
```

---

# 📦 Product Traceability

Every manufactured unit can be traced throughout its lifecycle.

```text
Product
   │
   ▼
Work Order
   │
   ▼
Production Execution
   │
   ▼
Serial Number
   │
   ├── Material Batch
   ├── Operator
   ├── Machine
   ├── Tool
   ├── Press Program
   ├── Force Curve
   ├── Test Results
   └── Packaging
```

This enables complete manufacturing genealogy and end-to-end traceability for every finished product.

---

# 🏗️ System Architecture

The Smart Manufacturing Intelligence Platform follows a modular architecture inspired by modern manufacturing systems integrating ERP, MES, Industrial IoT, and Analytics platforms.

```text
                        ┌──────────────────────┐
                        │      SAP / ERP       │
                        │  Work Order Planning │
                        └──────────┬───────────┘
                                   │
                                   ▼
                    ┌─────────────────────────┐
                    │ Manufacturing Execution │
                    │      System (MES)       │
                    └──────────┬──────────────┘
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
   Operator Login       Material Scan      Serial Numbers
          │                    │                    │
          └────────────────────┼────────────────────┘
                               ▼
                    Manufacturing Operations
                               │
                               ▼
                      Press-Fit Operations
                               │
                               ▼
                     Industrial IoT Sensors
                               │
                               ▼
                    Force Curve Acquisition
                               │
                               ▼
                       Quality Inspection
                               │
                               ▼
                          Packaging
                               │
                               ▼
                     Analytics & Dashboards
                               │
                               ▼
                  Databricks Lakehouse Platform
```

---

# ⚙️ Technology Stack

## Programming Language

- Python 3.13

---

## Data Processing

- Pandas
- NumPy

---

## Data Storage

- CSV
- Delta Lake (planned)
- Databricks Lakehouse (planned)

---

## Analytics

- SQL
- Power BI
- Databricks SQL

---

## Manufacturing Domain

- ERP (SAP-inspired)
- Manufacturing Execution System (MES)
- Factory Digital Twin
- Industrial IoT
- Production Planning
- Quality Management
- Manufacturing Traceability

---

## Development Tools

- Visual Studio Code
- Git
- GitHub
- Python Virtual Environment

---

# 🧠 Core Components

The project is divided into four logical layers.

## 1. Configuration Layer

Located in:

```
generator/configs/
```

Contains:

- Factory Digital Twin
- Dataclasses
- Enumerations
- Simulation Configuration
- Manufacturing Constants
- File Paths

---

## 2. Simulation Engine

Located in:

```
generator/engine/
```

Responsible for:

- Production Planning
- Scheduling
- Routing
- Quality Rules
- Time Generation

---

## 3. Data Generation

Located in:

```
generator/master_data/
```

Generates all manufacturing master data.

Examples:

- Machines
- Products
- Operators
- Tools
- Press Programs
- Test Programs

---

## 4. Manufacturing Simulation

Located in:

```
generator/simulation/
```

Generates transactional manufacturing events.

Examples:

- Work Orders
- Production Executions
- Operator Login
- Material Scan
- Press Operations
- Force Curves
- Testing
- Packaging

---

# 🏭 Factory Digital Twin

The project models a realistic high-voltage manufacturing facility.

Factory hierarchy:

```text
Factory
    │
    ├── Production Hall
    │
    ├── Production Line
    │
    ├── Station
    │
    ├── Machine
    │
    ├── Tool
    │
    ├── Operator
    │
    ├── Product
    │
    └── Manufacturing Operation
```

Every entity is represented as a strongly typed Python dataclass, providing a structured digital representation of the manufacturing environment.

---

# 🏗️ Medallion Architecture

The generated datasets are designed to support a Databricks Lakehouse implementation following the Medallion Architecture.

```text
CSV Files
    │
    ▼
Bronze Layer
(Raw Ingestion)
    │
    ▼
Silver Layer
(Data Cleaning & Transformation)
    │
    ▼
Gold Layer
(Business KPIs & Analytics)
```

The notebooks included in the repository demonstrate this progression:

```
notebooks/

01_bronze_ingestion.py

↓

02_silver_transform.py

↓

03_gold_kpis.py
```

---

# 📊 Planned Analytics

The generated datasets can be used to calculate manufacturing KPIs such as:

- Overall Equipment Effectiveness (OEE)
- Production Throughput
- First Pass Yield (FPY)
- Machine Utilization
- Operator Utilization
- Cycle Time Analysis
- Quality Pass Rate
- Force Curve Analysis
- Packaging Performance
- Production Line Performance
- Manufacturing Traceability
- Supplier Material Traceability

---

# 🔍 Engineering Principles

The project follows several software engineering practices:

- Modular project structure
- Separation of concerns
- Strong typing using Python dataclasses
- Configuration-driven simulation
- Reusable simulation components
- Validation before data export
- Consistent logging
- Reproducible synthetic data generation
- Extensible architecture for future manufacturing scenarios

---

# 🚀 Getting Started

Follow the steps below to set up the project and generate the complete manufacturing dataset.

---

# Prerequisites

Before running the project, ensure the following software is installed:

- Python 3.13 or later
- Git
- Visual Studio Code (recommended)

Verify your Python installation:

```bash
python --version
```

Example:

```text
Python 3.13.3
```

---

# Clone the Repository

```bash
git clone https://github.com/<your-github-username>/Smart-Manufacturing-Intelligence-Platform-SMIP.git

cd Smart-Manufacturing-Intelligence-Platform-SMIP
```

---

# Create a Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate it:

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Command Prompt

```cmd
.venv\Scripts\activate.bat
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

Example output:

```text
Successfully installed pandas numpy python-dateutil ...
```

---

# Project Structure

```
generator/
│
├── configs/
├── engine/
├── master_data/
└── simulation/
```

---

# Generate Master Data

Run the following scripts in order.

## 1. Factory Layout

```bash
python -m generator.master_data.generate_machine_layout
```

---

## 2. Product Master

```bash
python -m generator.master_data.generate_product_master
```

---

## 3. Tool Master

```bash
python -m generator.master_data.generate_tool_master
```

---

## 4. Operator Master

```bash
python -m generator.master_data.generate_operator_master
```

---

## 5. Operation Master

```bash
python -m generator.master_data.generate_operation_master
```

---

## 6. Press Program Master

```bash
python -m generator.master_data.generate_press_program_master
```

---

## 7. Test Program Master

```bash
python -m generator.master_data.generate_test_program_master
```

---

Generated master data is stored in:

```
data/master_data/
```

---

# Generate Manufacturing Simulation Data

Execute the following scripts in order.

## 1. Work Orders

```bash
python -m generator.simulation.simulate_work_orders
```

---

## 2. Production Executions

```bash
python -m generator.simulation.generate_production_executions
```

---

## 3. Operator Login

```bash
python -m generator.simulation.simulate_operator_login
```

---

## 4. Material Scan

```bash
python -m generator.simulation.simulate_material_scan
```

---

## 5. Serial Numbers

```bash
python -m generator.simulation.generate_serial_numbers
```

---

## 6. Press Operations

```bash
python -m generator.simulation.simulate_press_operations
```

---

## 7. Force Curves

```bash
python -m generator.simulation.simulate_force_curves
```

---

## 8. Manufacturing Testing

```bash
python -m generator.simulation.simulate_testing
```

---

## 9. Packaging

```bash
python -m generator.simulation.simulate_packaging
```

---

Generated transactional datasets are stored in:

```
data/transactional_data/
```

---

# Expected Output

After running all generators, your project should contain datasets similar to:

```
master_data/

machines.csv
operators.csv
operations.csv
press_programs.csv
products.csv
production_halls.csv
production_lines.csv
stations.csv
test_programs.csv
tools.csv

transactional_data/

force_curves.csv
material_scans.csv
operator_logins.csv
packaging.csv
press_operations.csv
production_executions.csv
serial_numbers.csv
testing_results.csv
work_orders.csv
```

---

# Logging

Each generator provides progress information.

Example:

```text
INFO     Starting Work Order Simulation
INFO     Loaded 12 products.
INFO     Generated 640 Work Orders.
INFO     Validation successful.
INFO     Exported 640 Work Orders.
INFO     Simulation completed successfully.
```

---

# Troubleshooting

## Import Errors

Ensure the virtual environment is activated.

```bash
python -m venv .venv

.venv\Scripts\Activate.ps1
```

---

## Missing Module Errors

Run scripts from the project root directory:

```bash
python -m generator.simulation.simulate_work_orders
```

instead of

```bash
python simulate_work_orders.py
```

---

## Missing CSV Files

Always execute the scripts in the documented order.

Several simulation modules depend on previously generated datasets.

---

## Validation Errors

Validation failures usually indicate:

- Missing prerequisite datasets
- Duplicate identifiers
- Modified CSV schemas
- Incomplete data generation

Regenerate the affected dataset before continuing.

---

# Performance

Approximate execution time on a modern laptop:

| Module | Approximate Time |
|---------|-----------------:|
| Master Data Generation | < 10 seconds |
| Work Order Simulation | < 5 seconds |
| Production Executions | < 5 seconds |
| Operator Login | < 5 seconds |
| Material Scan | < 5 seconds |
| Serial Numbers | < 5 seconds |
| Press Operations | < 10 seconds |
| Force Curve Simulation | 30–90 seconds |
| Manufacturing Testing | < 10 seconds |
| Packaging | < 5 seconds |

The Force Curve simulation generates over **3.6 million records** and is therefore the most computationally intensive step.

---

# 📷 Project Demonstration

The following images illustrate the Smart Manufacturing Intelligence Platform.

> **Note:** Screenshots will be added as the project evolves.

## Factory Digital Twin

```
docs/images/factory_layout.png
```

---

## Manufacturing Process

```
docs/images/manufacturing_process.png
```

---

## Databricks Lakehouse

```
docs/images/lakehouse_architecture.png
```

---

## Power BI Dashboard

```
docs/images/powerbi_dashboard.png
```

---

## Force Curve Visualization

```
docs/images/force_curve.png
```

---

# 📊 Example Datasets

## Work Orders

| work_order_id | product_code | quantity | production_line | planned_shift |
|---------------|--------------|----------|-----------------|---------------|
| WO-000001 | GIS-145 | 4 | LINE-01 | Morning |
| WO-000002 | GIS-220 | 2 | LINE-02 | Evening |

---

## Serial Numbers

| serial_number | work_order_id | execution_id | product_code |
|---------------|---------------|--------------|--------------|
| SN-00000001 | WO-000001 | EXEC-000001 | GIS-145 |
| SN-00000002 | WO-000001 | EXEC-000001 | GIS-145 |

---

## Force Curve

| sample | displacement_mm | force_kn |
|---------|----------------:|---------:|
| 1 | 0.00 | 0.10 |
| 2 | 0.05 | 0.45 |
| 3 | 0.10 | 0.91 |
| ... | ... | ... |

---

# 📈 Planned Dashboards

The generated datasets are intended to support interactive dashboards for manufacturing analytics.

Planned dashboards include:

- Executive Manufacturing Overview
- Production Planning Dashboard
- Shop Floor Monitoring
- Overall Equipment Effectiveness (OEE)
- Production Throughput
- Machine Utilization
- Operator Performance
- Force Curve Analytics
- Quality Inspection Dashboard
- Packaging & Shipment Dashboard
- End-to-End Product Traceability

---

# 🛣️ Roadmap

## Completed

- Factory Digital Twin
- Master Data Generation
- Production Planning
- Manufacturing Execution Simulation
- Operator Login Simulation
- Material Traceability
- Serial Number Generation
- Press Operation Simulation
- Force Curve Generation
- Manufacturing Testing
- Packaging Simulation

---

## In Progress

- Databricks Bronze Layer
- Silver Layer Transformations
- Gold KPI Tables
- SQL Analytics
- Power BI Dashboards

---

## Planned

- Delta Lake Integration
- Streaming IoT Data Simulation
- Predictive Maintenance Models
- Machine Learning Pipelines
- Process Mining
- REST API
- Docker Support
- CI/CD Pipeline
- Automated Data Validation
- Unit & Integration Tests

---

# 🤝 Contributing

Contributions are welcome.

If you would like to contribute:

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature/my-feature
```

5. Open a Pull Request

---

# 📚 References

The project is inspired by modern manufacturing systems and Industry 4.0 concepts, including:

- Manufacturing Execution Systems (MES)
- Enterprise Resource Planning (ERP)
- Factory Digital Twins
- Industrial Internet of Things (IIoT)
- Databricks Lakehouse Architecture
- Medallion Architecture
- Manufacturing Analytics
- Production Planning & Scheduling

---

# 👨‍💻 Author

**Sumanth Vempalle**

Mechanical Engineer | Sustainable Industrial Engineering

Specializing in:

- Manufacturing Systems
- Data Engineering
- Industrial Digitalization
- Databricks
- SQL
- Python
- Power BI
- Manufacturing Analytics

GitHub:

```
https://github.com/<your-username>
```

LinkedIn:

```
https://linkedin.com/in/<your-linkedin-profile>
```

---

# 📄 License

This project is licensed under the MIT License.

See the LICENSE file for additional information.

---

# ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.

Feedback, suggestions, and contributions are always welcome.

---

# 📌 Project Status

**Current Version:** 1.0.0

**Status:** Active Development

The project currently provides a complete synthetic manufacturing data generation platform and serves as the foundation for a Databricks-based Smart Manufacturing Lakehouse and analytics solution.

# 📊 Manufacturing KPIs

The generated datasets support a wide range of manufacturing analytics and Key Performance Indicators (KPIs).

---

## Production KPIs

| KPI | Description | Source Dataset |
|------|-------------|----------------|
| Total Work Orders | Number of released work orders | work_orders.csv |
| Total Production Quantity | Total manufactured units | production_executions.csv |
| Production Throughput | Units produced per day/shift | production_executions.csv |
| Work Order Completion | Completed vs. released orders | production_executions.csv |

---

## Machine KPIs

| KPI | Description | Source Dataset |
|------|-------------|----------------|
| Machine Utilization | Operating time per machine | press_operations.csv |
| Machine Availability | Available production time | machines.csv |
| Machine Load | Operations assigned per machine | press_operations.csv |

---

## Operator KPIs

| KPI | Description | Source Dataset |
|------|-------------|----------------|
| Login Sessions | Total operator sessions | operator_logins.csv |
| Operator Utilization | Active production time | operator_logins.csv |
| Shift Distribution | Workload by shift | operator_logins.csv |

---

## Quality KPIs

| KPI | Description | Source Dataset |
|------|-------------|----------------|
| Pass Rate | PASS vs FAIL ratio | testing_results.csv |
| Test Execution Count | Number of executed tests | testing_results.csv |
| First Pass Yield | Percentage of products passing all tests | testing_results.csv |

---

## Process KPIs

| KPI | Description | Source Dataset |
|------|-------------|----------------|
| Average Cycle Time | Manufacturing cycle duration | press_operations.csv |
| Press Force Distribution | Force applied during assembly | force_curves.csv |
| Packaging Throughput | Finished packages | packaging.csv |

---

# 📈 Example SQL Analytics

Example queries that can be executed after loading the datasets into Databricks or SQL Server.

---

## Total Production

```sql
SELECT
    COUNT(*) AS total_work_orders
FROM work_orders;
```

---

## Production by Product

```sql
SELECT
    product_code,
    SUM(quantity) AS total_quantity
FROM production_executions
GROUP BY product_code
ORDER BY total_quantity DESC;
```

---

## Daily Production

```sql
SELECT
    DATE(execution_start) AS production_date,
    SUM(quantity) AS produced_units
FROM production_executions
GROUP BY DATE(execution_start)
ORDER BY production_date;
```

---

## Test Pass Rate

```sql
SELECT
    result,
    COUNT(*) AS total
FROM testing_results
GROUP BY result;
```

---

## Machine Utilization

```sql
SELECT
    machine_id,
    COUNT(*) AS operations
FROM press_operations
GROUP BY machine_id
ORDER BY operations DESC;
```

---

# 🏗️ Databricks Lakehouse Mapping

The generated datasets are intended to be processed using the Medallion Architecture.

| Layer | Purpose |
|--------|----------|
| Bronze | Raw CSV ingestion |
| Silver | Data cleansing, validation, enrichment |
| Gold | Business KPIs, reporting, dashboards |

---

## Bronze Layer

Raw CSV ingestion.

```
CSV Files

↓

Bronze Delta Tables
```

Examples:

```
bronze_products

bronze_work_orders

bronze_press_operations

bronze_force_curves
```

---

## Silver Layer

Business transformations.

Examples:

- Product dimension
- Machine dimension
- Operator dimension
- Calendar dimension
- Production fact table
- Quality fact table

---

## Gold Layer

Business-ready datasets.

Examples:

```
gold_daily_production

gold_machine_oee

gold_quality_summary

gold_operator_performance

gold_force_statistics

gold_packaging_summary
```

---

# 🔄 Data Lineage

The project maintains complete manufacturing traceability.

```text
Product
    │
    ▼
Work Order
    │
    ▼
Production Execution
    │
    ▼
Serial Number
    │
    ├──────────────┐
    ▼              ▼
Material Scan   Operator Login
    │              │
    └──────┬───────┘
           ▼
   Press Operation
           │
           ▼
      Force Curve
           │
           ▼
      Test Result
           │
           ▼
      Packaging
```

This lineage enables complete product genealogy from raw material receipt through manufacturing, quality inspection, and packaging.

---

# 🎯 Project Objectives

The Smart Manufacturing Intelligence Platform was developed to demonstrate:

- Factory Digital Twin modeling
- Manufacturing Execution System (MES) concepts
- Synthetic industrial data generation
- Manufacturing traceability
- Industrial IoT simulation
- Databricks Lakehouse integration
- SQL analytics
- Power BI reporting
- Data engineering workflows
- Manufacturing analytics and KPI development

The project serves as a practical foundation for learning and demonstrating modern manufacturing data engineering techniques using realistic synthetic datasets.

