
# 🏗️ System Architecture

## Smart Manufacturing Intelligence Platform (SMIP)

Version: **1.0.0**

---

# Overview

The Smart Manufacturing Intelligence Platform (SMIP) is a modular data generation and analytics platform that simulates the operation of a modern manufacturing facility producing high-voltage electrical equipment.

The platform combines concepts from:

- Enterprise Resource Planning (ERP)
- Manufacturing Execution Systems (MES)
- Factory Digital Twins
- Industrial Internet of Things (IIoT)
- Manufacturing Analytics
- Databricks Lakehouse
- Power BI

Its primary objective is to generate realistic synthetic manufacturing datasets that can be used for analytics, machine learning, visualization, and digital twin applications.

---

# System Architecture

```
                                  Users
                                     │
                                     ▼
                        Smart Manufacturing Platform
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        ▼                            ▼                            ▼
 Configuration Layer          Data Generation Layer        Analytics Layer
        │                            │                            │
        ▼                            ▼                            ▼
 Factory Digital Twin        Master Data Generator        Databricks
 Simulation Config           Manufacturing Simulation     SQL Analytics
 Enumerations                Synthetic Data Engine        Power BI
 Paths                       CSV Export                   Machine Learning
```

---

# High-Level Architecture

```
                 ERP (SAP)
                     │
                     ▼
            Production Planning
                     │
                     ▼
       Manufacturing Execution System
                     │
      ┌──────────────┼───────────────┐
      ▼              ▼               ▼
Operator Login  Material Scan  Production Execution
                     │
                     ▼
              Serial Numbers
                     │
                     ▼
             Press Operations
                     │
                     ▼
            Force Curve Capture
                     │
                     ▼
              Quality Testing
                     │
                     ▼
                 Packaging
                     │
                     ▼
             Analytics Platform
```

---

# Architecture Layers

The project is organized into five logical layers.

---

## 1. Configuration Layer

Location:

```
generator/configs/
```

Purpose:

Provide all shared configuration used throughout the platform.

Contains:

- Factory Digital Twin
- Enumerations
- Dataclasses
- Simulation Configuration
- File Paths
- Manufacturing Constants

Main file:

```
factory_digital_twin.py
```

---

## 2. Master Data Layer

Location:

```
generator/master_data/
```

Responsible for generating all static manufacturing data.

Generated datasets:

- Production Halls
- Production Lines
- Stations
- Machines
- Operators
- Products
- Tools
- Operations
- Press Programs
- Test Programs

Output:

```
data/master_data/
```

---

## 3. Manufacturing Simulation Layer

Location:

```
generator/simulation/
```

Responsible for generating transactional manufacturing events.

Generated datasets:

- Work Orders
- Production Executions
- Operator Login Sessions
- Material Scans
- Serial Numbers
- Press Operations
- Force Curves
- Test Results
- Packaging Records

Output:

```
data/transactional_data/
```

---

## 4. Processing Layer

Current implementation:

CSV generation

Future implementation:

- Databricks Bronze Layer
- Silver Layer
- Gold Layer

Purpose:

Transform raw manufacturing datasets into analytical datasets.

---

## 5. Analytics Layer

Purpose:

Generate business insights.

Technologies:

- SQL
- Databricks SQL
- Power BI
- Machine Learning

Outputs:

- Production KPIs
- OEE
- Quality Analytics
- Throughput
- Machine Utilization
- Operator Performance
- Traceability

---

# Manufacturing Workflow

The manufacturing process implemented by the platform follows the sequence below.

```
ERP Work Order

↓

Production Execution

↓

Operator Login

↓

Material Scan

↓

Serial Number Assignment

↓

Press Operation

↓

Force Curve Acquisition

↓

Quality Testing

↓

Packaging

↓

Finished Product
```

Every simulated product follows the same lifecycle, ensuring complete manufacturing traceability.

---

# Data Flow

```
Master Data
     │
     ▼
Simulation Engine
     │
     ▼
CSV Generation
     │
     ▼
Databricks Bronze
     │
     ▼
Silver Transformations
     │
     ▼
Gold Analytics
     │
     ▼
Power BI Dashboards
```

---

# Component Responsibilities

| Component | Responsibility |
|-----------|----------------|
| configs | Shared configuration and dataclasses |
| master_data | Generate manufacturing master data |
| simulation | Generate transactional manufacturing events |
| engine | Production planning and simulation logic |
| data | Generated datasets |
| notebooks | Databricks ETL workflows |
| sql | SQL scripts and analytics |
| dashboard | Reporting assets |

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.13 |
| Data Processing | Pandas |
| Data Storage | CSV |
| Analytics | SQL |
| Visualization | Power BI |
| Lakehouse | Databricks (planned) |
| Version Control | Git |
| IDE | Visual Studio Code |

---

# Design Principles

The platform is designed according to the following principles:

- Modular architecture
- Separation of concerns
- Strong typing using Python dataclasses
- Configuration-driven simulation
- Reusable simulation modules
- Deterministic data generation
- Consistent validation before export
- Comprehensive logging
- Extensible design for future manufacturing scenarios

---

# Current Implementation Status

| Module | Status |
|----------|:------:|
| Factory Digital Twin | ✅ |
| Master Data Generation | ✅ |
| Production Planning | ✅ |
| Manufacturing Simulation | ✅ |
| Operator Login | ✅ |
| Material Traceability | ✅ |
| Serial Number Generation | ✅ |
| Press Operations | ✅ |
| Force Curve Simulation | ✅ |
| Quality Testing | ✅ |
| Packaging | ✅ |
| Documentation | 🚧 |
| Databricks Lakehouse | 🚧 |
| Power BI Dashboards | 🚧 |

---

# Future Enhancements

The architecture has been designed to support future capabilities, including:

- Delta Lake integration
- Real-time streaming simulation
- MQTT/OPC-UA IoT integration
- Predictive maintenance
- Manufacturing scheduling optimization
- REST API services
- Docker deployment
- CI/CD pipelines
- Automated testing
- Cloud deployment on Azure Databricks

---

# Summary

The Smart Manufacturing Intelligence Platform provides an end-to-end simulation of a modern manufacturing environment, covering production planning, execution, quality inspection, packaging, and analytics.

The modular architecture enables straightforward extension of the platform while supporting downstream analytics, visualization, and machine learning workflows through a consistent and traceable manufacturing data model.
