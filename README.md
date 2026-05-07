# WECO Electrical Engineer System

---

## ** Overview**

The ** Electrical Engineer System** is a **Python-based automation tool** designed to streamline **electrical engineering workflows** (February 2022 – July 2023)**. This system supports the **design of low and medium voltage power distribution systems**, **load studies**, **short circuit analysis**, **protection coordination**, and **Smart Grid Modernization Projects**. It enables engineers to achieve **15% energy efficiency improvements**, enhance **system stability**, and ensure **reliable fault response** through advanced analysis and optimization.

---

## ** Features**

---

### **Power Distribution System Design**

- **System Design**: Create and manage **low and medium voltage power distribution systems** with customizable components (e.g., transformers, switchgear).
- **Component Management**: Add and track **equipment specifications** (e.g., capacity, voltage ratios, ratings).
- **Status Tracking**: Monitor system statuses (e.g., Design, Installed, Operational).

---

### **Load Studies**

- **Study Conduct**: Perform **load flow studies** to assess system performance under various conditions.
- **Results Analysis**: Track **loading percentages, voltage drops, and power losses**.
- **Auto-Recommendations**: Generate **mitigation strategies** (e.g., upgrade transformers if loading exceeds 90%).

---

### **Short Circuit Analysis**

- **Fault Analysis**: Conduct **3-phase, line-to-ground, and other fault analyses** to evaluate system behavior during faults.
- **Results Tracking**: Document **fault currents, interrupting ratings, and fault locations**.
- **Mitigation Strategies**: Auto-generate **corrective actions** (e.g., upgrade protective devices if fault currents exceed ratings).

---

### **Protection Coordination**

- **Coordination Studies**: Create and manage **protection coordination studies** for distribution systems.
- **Relay Settings**: Configure **overcurrent, voltage, and time-delay settings** for protective devices.
- **Time-Current Curves**: Model and analyze **time-current curves** for protective devices.
- **Stability Improvement**: Track **stability improvements** from coordination efforts.

---

### **Smart Grid Modernization**

- **Project Management**: Lead **cross-functional Smart Grid projects** with teams, timelines, and energy savings targets.
- **Energy Efficiency**: Track and achieve **15% energy efficiency improvements** through modernization efforts.
- **Status Tracking**: Monitor project statuses (e.g., Planning, In Progress, Completed).

---

### **Equipment Commissioning**

- **Equipment Management**: Add and track **transformers, switchgear, and protective devices** with detailed specifications.
- **Commissioning Workflows**: Commission equipment and **verify behavior** under real operating conditions.
- **Test Documentation**: Record **commissioning dates, test results, and performance metrics**.

---

### **System Settings**

- **Setting Establishment**: Configure **system parameters** (e.g., voltage regulation, fault response times) to improve stability.
- **Impact Tracking**: Monitor the **impact of settings** on system performance and stability scores.

---

### **Audit Logging**

- **Activity Tracking**: Automatically log all actions (e.g., system design, studies, commissioning) for **traceability and compliance**.
- **Comprehensive Logs**: Retrieve logs for **auditing, reporting, and debugging**.

---

### **Reporting**

- **System Reports**: Generate **detailed reports** for individual power distribution systems, including components, studies, and settings.
- **Project Reports**: Summarize **Smart Grid projects**, energy savings, and completion statuses.
- **Equipment Reports**: Track **commissioned equipment**, behavior verification, and test results.

---

## ** Installation**

### **Prerequisites**

- **Python 3.8+**
- **Dependencies**: None (uses Python’s built-in libraries)

### **Setup**

1. **Clone the repository**:
  ```bash
   git clone https://github.com/chrisCodeee/wc-electricial
   cd weco-electrical
  ```
2. **Run the system**:
  ```bash
   python weco_electrical_engineer.py
  ```

---

## ** Usage**

---

### **1. Initialize the System**

```python
weco = ElectricalEngineerSystem()
```

---

### **2. Power Distribution System Design**

```python
# Design LV and MV systems
lv_system = weco.design_distribution_system("Industrial Park LV System", "Low Voltage")
mv_system = weco.design_distribution_system("City Substation MV System", "Medium Voltage")

# Add components
weco.add_component(lv_system, "Transformer", {"capacity": "1000 kVA", "voltage_ratio": "11/0.4 kV"})
weco.add_component(lv_system, "Switchgear", {"type": "LV", "rating": "1000A"})

# Update system status
weco.update_system_status(lv_system, "Operational")
```

---

### **3. Load Studies**

```python
# Conduct a load study
load_study = weco.conduct_load_study(lv_system, "Load Flow")

# Add results
weco.add_load_study_results(load_study, {
    "loading_percentage": 95,
    "voltage_drop": 6,
    "power_losses": "3.2%"
})
```

---

### **4. Short Circuit Analysis**

```python
# Conduct a short circuit analysis
sc_analysis = weco.conduct_short_circuit_analysis(lv_system, "3-Phase")

# Add results
weco.add_short_circuit_results(sc_analysis, {
    "fault_current": 25000,
    "interrupting_rating": 20000,
    "fault_location": "Busbar A"
})
```

---

### **5. Protection Coordination**

```python
# Create a protection coordination study
coordination = weco.create_protection_coordination(lv_system)

# Add relay settings
weco.add_protection_setting(coordination, "Relay 1", {
    "type": "Overcurrent",
    "setting": "120%",
    "time_delay": "0.5s"
})

# Add time-current curve
weco.add_time_current_curve(coordination, {
    "device": "Relay 1",
    "curve_type": "Inverse Time",
    "points": [(0.1, 10), (0.5, 5), (1.0, 2)]
})
```

---

### **6. Smart Grid Modernization**

```python
# Create a Smart Grid project
smart_grid_project = weco.create_smart_grid_project(
    "WECO Smart Grid Initiative",
    ["Alice", "Bob", "Charlie"]
)

# Update project status and energy savings
weco.update_smart_grid_status(
    smart_grid_project,
    "Completed",
    energy_savings=15.0,
    completion_date="2023-07-31"
)
```

---

### **7. Equipment Commissioning**

```python
# Add equipment
transformer = weco.add_equipment(
    "Transformer T1",
    "Power Transformer",
    {"capacity": "2500 kVA", "voltage": "33/11 kV"}
)
switchgear = weco.add_equipment(
    "Switchgear S1",
    "MV Switchgear",
    {"rating": "1250A", "type": "Indoor"}
)

# Commission equipment
weco.commission_equipment(transformer, "2023-06-15", {
    "voltage_regulation": "Within Limits",
    "temperature": "Normal",
    "noise_level": "Acceptable"
})
weco.commission_equipment(switchgear, "2023-06-20", {
    "operation": "Smooth",
    "arc_resistance": "Tested",
    "interlocks": "Functional"
})
```

---

### **8. System Settings**

```python
# Establish system settings
weco.establish_system_setting(
    lv_system,
    "Voltage Regulation",
    1.05,
    "Improved voltage stability"
)
weco.establish_system_setting(
    lv_system,
    "Fault Response Time",
    0.2,
    "Faster fault clearing"
)
```

---

### **9. Generate Reports**

```python
# Generate system report
system_report = weco.generate_system_report(lv_system)

# Generate project report
project_report = weco.generate_project_report()

# Generate equipment report
equipment_report = weco.generate_equipment_report()
```

---

## ** Repository Structure**

```
.
├── weco_electrical_engineer.py  # Main system code
├── README.md                     # Project documentation
└── requirements.txt              # Dependencies (if any)
```

---

## ** Technical Details**

---

### **Architecture**

- **Class-Based Design**: The `ElectricalEngineerSystem` class encapsulates all functionalities.
- **Data Storage**: Uses **dictionaries and lists** for in-memory storage (suitable for small-to-medium datasets).
- **Unique Identifiers**: Sequential IDs ensure **unique tracking** of systems, studies, and equipment.
- **Audit Logging**: Tracks all actions for **compliance, traceability, and debugging**.

---

### **Extensibility**

Future enhancements could include:

- **Database Integration**: Use `sqlite3` or `PostgreSQL` for persistent storage of projects and studies.
- **Data Visualization**: Integrate `matplotlib` or `seaborn` for generating **performance trend charts** and **compliance dashboards**.
- **Web Interface**: Deploy with **Flask/Django** for a user-friendly dashboard to manage systems and projects.
- **API Integration**: Connect with **ETAP, PSCAD, or PSSE** for advanced power system analysis.
- **Real-Time Monitoring**: Integrate with **SCADA systems** for live data collection and analysis.

---

## ** Example Output**

Running the example usage in `__main__` produces:

```
=== Power Distribution System Design ===
Distribution System 'Industrial Park LV System' designed with ID: DS1
Distribution System 'City Substation MV System' designed with ID: DS2
Component Transformer added to system DS1 with ID: COMP1
Component Switchgear added to system DS1 with ID: COMP2
System DS1 status updated to: Operational

=== Load Studies ===
Load Study conducted with ID: LS1
Results added to Load Study LS1

=== Short Circuit Analysis ===
Short Circuit Analysis conducted with ID: SC1
Results added to Short Circuit Analysis SC1

=== Protection Coordination ===
Protection Coordination created with ID: PC1
Protection setting for Relay 1 added to Coordination PC1
Time-Current Curve added to Coordination PC1

=== Smart Grid Modernization ===
Smart Grid Project 'WECO Smart Grid Initiative' created with ID: SG1
Smart Grid Project SG1 updated. Status: Completed, Energy Savings: 15.0%

=== Equipment Commissioning ===
Equipment 'Transformer T1' added with ID: EQ1
Equipment 'Switchgear S1' added with ID: EQ2
Equipment EQ1 commissioned on 2023-06-15. Behavior: {'voltage_regulation': 'Within Limits', ...}
Equipment EQ2 commissioned on 2023-06-20. Behavior: {'operation': 'Smooth', ...}

=== System Settings ===
System Setting established with ID: SET1. Impact: Improved voltage stability
System Setting established with ID: SET2. Impact: Faster fault clearing

=== System Report for Industrial Park LV System ===
system_id: DS1
name: Industrial Park LV System
voltage_level: Low Voltage
status: Operational
stability_score: 10.0
components: [{'component_id': 'COMP1', 'type': 'Transformer', ...}, ...]
load_studies: [{'system_id': 'DS1', 'type': 'Load Flow', ...}]
short_circuit_analyses: [{'system_id': 'DS1', 'fault_type': '3-Phase', ...}]
protection_coordination: [{'system_id': 'DS1', 'settings': {...}, ...}]
system_settings: [{'system_id': 'DS1', 'parameter': 'Voltage Regulation', ...}, ...]

=== Smart Grid Project Report ===
total_projects: 1
completed_projects: 1
avg_energy_savings: 15.0
projects: [{'name': 'WECO Smart Grid Initiative', 'status': 'Completed', ...}]

=== Equipment Report ===
total_equipment: 2
commissioned_equipment: 2
equipment: [{'name': 'Transformer T1', 'type': 'Power Transformer', ...}, ...]
```

---

## ** Contributing**

Contributions are welcome! To contribute:

1. **Fork the repository** and create a feature branch.
2. **Add improvements**:
  - Database integration (e.g., SQLite).
  - Advanced analytics (e.g., predictive maintenance for equipment).
  - API endpoints for external tools (e.g., ETAP, PSCAD).
3. **Submit a pull request** with a clear description of changes.

---

## ** License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## ** Acknowledgments**

- Inspired by **WECO Engineering’s electrical engineering workflows** in Nigeria.
- Designed to **improve system stability**, **enhance fault response**, and **achieve energy efficiency** in power distribution systems.
- Built to replicate the **15% energy efficiency improvement** and **reliable system performance** achievements at WECO Engineering.
