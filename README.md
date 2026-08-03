# smart-manufacturing-lakehouse


An end-to-end Azure Databricks Data Engineering project that simulates a modern manufacturing environment for Gas Insulated Switchgear (GIS).

## Objectives

- Simulate manufacturing data from SAP and MES
- Build a Medallion Architecture using Delta Lake
- Develop manufacturing KPIs
- Create Power BI dashboards
- Demonstrate production-grade Data Engineering practices


# Architecture V1.0

smart-manufacturing-lakehouse/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
│   ├── 01_Business_Requirements.md
│   ├── 02_Functional_Design.md
│   ├── 03_Technical_Architecture.md
│   ├── 04_Data_Model.md
│   ├── 05_ETL_Design.md
│   ├── 06_KPI_Definitions.md
│   ├── 07_Dashboard_Design.md
│   ├── 08_Data_Lineage.md
│
├── data/
│   ├── master_data/
│   ├── transactional_data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── generator/
│   │
│   ├── configs/
│   │   ├── factory_digital_twin.py
│   │   └── paths.py
│   │
│   ├── master_data/
│   │   ├── generate_product_master.py
│   │   ├── generate_machine_layout.py
│   │   ├── generate_tool_master.py
│   │   ├── generate_operator_master.py
│   │   ├── generate_press_program_master.py
│   │   └── generate_test_program_master.py
│   │
│   ├── transactional_data/
│   │   ├── simulate_work_orders.py
│   │   ├── simulate_press_operations.py
│   │   ├── simulate_force_curves.py
│   │   ├── simulate_assembly.py
│   │   ├── simulate_testing.py
│   │   └── simulate_packaging.py
│   │
│   └── utils/
│       ├── validation.py
│       ├── logging_utils.py
│       └── helpers.py
│
├── databricks/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
└── powerbi/
    └── dashboards/
