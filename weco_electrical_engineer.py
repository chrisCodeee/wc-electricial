import datetime
from typing import Dict, List, Optional, Tuple, Union
import uuid
import math

class ElectricalEngineerSystem:
    def __init__(self):
        # Power Distribution Systems: {system_id: {"name": str, "voltage_level": str, "status": str, "components": List[Dict]}}
        self.distribution_systems: Dict[str, Dict] = {}

        # Load Studies: {study_id: {"system_id": str, "type": str, "results": Dict, "recommendations": List[str]}}
        self.load_studies: Dict[str, Dict] = {}

        # Short Circuit Analysis: {analysis_id: {"system_id": str, "fault_type": str, "results": Dict, "mitigations": List[Dict]}}
        self.short_circuit_analyses: Dict[str, Dict] = {}

        # Protection Coordination: {coordination_id: {"system_id": str, "settings": Dict, "curves": List[Dict]}}
        self.protection_coordination: Dict[str, Dict] = {}

        # Smart Grid Projects: {project_id: {"name": str, "status": str, "energy_savings": float, "team": List[str]}}
        self.smart_grid_projects: Dict[str, Dict] = {}

        # Equipment: {equipment_id: {"name": str, "type": str, "status": str, "commissioning_date": str, "settings": Dict}}
        self.equipment: Dict[str, Dict] = {}

        # System Settings: {setting_id: {"system_id": str, "parameter": str, "value": Union[float, str], "impact": str}}
        self.system_settings: Dict[str, Dict] = {}

        # Audit Logs: List[Dict]
        self.audit_logs: List[Dict] = {}

        # Next IDs
        self.next_system_id = 1
        self.next_study_id = 1
        self.next_analysis_id = 1
        self.next_coordination_id = 1
        self.next_project_id = 1
        self.next_equipment_id = 1
        self.next_setting_id = 1

    # --- Power Distribution System Design ---
    def design_distribution_system(self, name: str, voltage_level: str) -> str:
        """Design a new low or medium voltage power distribution system."""
        system_id = f"DS{self.next_system_id}"
        self.next_system_id += 1
        self.distribution_systems[system_id] = {
            "name": name,
            "voltage_level": voltage_level,
            "status": "Design",
            "components": [],
            "stability_score": 0.0
        }
        self._log_activity("system_designed", {
            "system_id": system_id,
            "name": name,
            "voltage_level": voltage_level
        })
        return f"Distribution System '{name}' designed with ID: {system_id}"

    def add_component(self, system_id: str, component_type: str, specs: Dict) -> str:
        """Add a component (e.g., transformer, switchgear) to a distribution system."""
        if system_id in self.distribution_systems:
            component_id = f"COMP{str(uuid.uuid4())[:6]}"
            component = {
                "component_id": component_id,
                "type": component_type,
                "specs": specs,
                "status": "Installed"
            }
            self.distribution_systems[system_id]["components"].append(component)
            self._log_activity("component_added", {
                "system_id": system_id,
                "component_id": component_id,
                "type": component_type
            })
            return f"Component {component_type} added to system {system_id} with ID: {component_id}"
        return f"System ID {system_id} not found."

    def update_system_status(self, system_id: str, status: str) -> str:
        """Update the status of a distribution system (e.g., Design, Installed, Operational)."""
        if system_id in self.distribution_systems:
            self.distribution_systems[system_id]["status"] = status
            self._log_activity("system_status_updated", {
                "system_id": system_id,
                "status": status
            })
            return f"System {system_id} status updated to: {status}"
        return f"System ID {system_id} not found."

    # --- Load Studies ---
    def conduct_load_study(self, system_id: str, study_type: str = "Load Flow") -> str:
        """Conduct a load study for a distribution system."""
        if system_id in self.distribution_systems:
            study_id = f"LS{self.next_study_id}"
            self.next_study_id += 1
            self.load_studies[study_id] = {
                "system_id": system_id,
                "type": study_type,
                "results": {},
                "recommendations": []
            }
            self._log_activity("load_study_conducted", {
                "study_id": study_id,
                "system_id": system_id,
                "type": study_type
            })
            return f"Load Study conducted with ID: {study_id}"
        return f"System ID {system_id} not found."

    def add_load_study_results(self, study_id: str, results: Dict) -> str:
        """Add results to a load study."""
        if study_id in self.load_studies:
            self.load_studies[study_id]["results"] = results
            # Auto-generate recommendations based on results
            if results.get("loading_percentage", 0) > 90:
                self.load_studies[study_id]["recommendations"].append("Upgrade transformer capacity")
            if results.get("voltage_drop", 0) > 5:
                self.load_studies[study_id]["recommendations"].append("Install voltage regulators")
            self._log_activity("load_study_results_added", {
                "study_id": study_id,
                "results": results
            })
            return f"Results added to Load Study {study_id}"
        return f"Study ID {study_id} not found."

    # --- Short Circuit Analysis ---
    def conduct_short_circuit_analysis(self, system_id: str, fault_type: str = "3-Phase") -> str:
        """Conduct a short circuit analysis for a distribution system."""
        if system_id in self.distribution_systems:
            analysis_id = f"SC{self.next_analysis_id}"
            self.next_analysis_id += 1
            self.short_circuit_analyses[analysis_id] = {
                "system_id": system_id,
                "fault_type": fault_type,
                "results": {},
                "mitigations": []
            }
            self._log_activity("short_circuit_analysis_conducted", {
                "analysis_id": analysis_id,
                "system_id": system_id,
                "fault_type": fault_type
            })
            return f"Short Circuit Analysis conducted with ID: {analysis_id}"
        return f"System ID {system_id} not found."

    def add_short_circuit_results(self, analysis_id: str, results: Dict) -> str:
        """Add results to a short circuit analysis."""
        if analysis_id in self.short_circuit_analyses:
            self.short_circuit_analyses[analysis_id]["results"] = results
            # Auto-generate mitigations based on results
            if results.get("fault_current", 0) > results.get("interrupting_rating", 0):
                self.short_circuit_analyses[analysis_id]["mitigations"].append({
                    "issue": "Fault current exceeds interrupting rating",
                    "action": "Upgrade protective devices",
                    "priority": "High"
                })
            self._log_activity("short_circuit_results_added", {
                "analysis_id": analysis_id,
                "results": results
            })
            return f"Results added to Short Circuit Analysis {analysis_id}"
        return f"Analysis ID {analysis_id} not found."

    # --- Protection Coordination ---
    def create_protection_coordination(self, system_id: str) -> str:
        """Create a protection coordination study for a distribution system."""
        if system_id in self.distribution_systems:
            coordination_id = f"PC{self.next_coordination_id}"
            self.next_coordination_id += 1
            self.protection_coordination[coordination_id] = {
                "system_id": system_id,
                "settings": {},
                "curves": [],
                "stability_improvement": 0.0
            }
            self._log_activity("protection_coordination_created", {
                "coordination_id": coordination_id,
                "system_id": system_id
            })
            return f"Protection Coordination created with ID: {coordination_id}"
        return f"System ID {system_id} not found."

    def add_protection_setting(self, coordination_id: str, device: str, setting: Dict) -> str:
        """Add a protection setting (e.g., relay settings) to a coordination study."""
        if coordination_id in self.protection_coordination:
            self.protection_coordination[coordination_id]["settings"][device] = setting
            self._log_activity("protection_setting_added", {
                "coordination_id": coordination_id,
                "device": device,
                "setting": setting
            })
            return f"Protection setting for {device} added to Coordination {coordination_id}"
        return f"Coordination ID {coordination_id} not found."

    def add_time_current_curve(self, coordination_id: str, curve: Dict) -> str:
        """Add a time-current curve to a protection coordination study."""
        if coordination_id in self.protection_coordination:
            self.protection_coordination[coordination_id]["curves"].append(curve)
            # Calculate stability improvement (simplified)
            self.protection_coordination[coordination_id]["stability_improvement"] = min(
                100, len(self.protection_coordination[coordination_id]["curves"]) * 5
            )
            self._log_activity("time_current_curve_added", {
                "coordination_id": coordination_id,
                "curve": curve
            })
            return f"Time-Current Curve added to Coordination {coordination_id}"
        return f"Coordination ID {coordination_id} not found."

    # --- Smart Grid Modernization ---
    def create_smart_grid_project(self, name: str, team: List[str]) -> str:
        """Create a new Smart Grid Modernization Project."""
        project_id = f"SG{self.next_project_id}"
        self.next_project_id += 1
        self.smart_grid_projects[project_id] = {
            "name": name,
            "status": "Planning",
            "energy_savings": 0.0,  # Target: 15%
            "team": team,
            "completion_date": None
        }
        self._log_activity("smart_grid_project_created", {
            "project_id": project_id,
            "name": name,
            "team": team
        })
        return f"Smart Grid Project '{name}' created with ID: {project_id}"

    def update_smart_grid_status(self, project_id: str, status: str, energy_savings: float = 0.0, completion_date: Optional[str] = None) -> str:
        """Update the status of a Smart Grid project and its energy savings."""
        if project_id in self.smart_grid_projects:
            self.smart_grid_projects[project_id]["status"] = status
            if energy_savings > 0:
                self.smart_grid_projects[project_id]["energy_savings"] = energy_savings
            if completion_date:
                self.smart_grid_projects[project_id]["completion_date"] = completion_date
            self._log_activity("smart_grid_status_updated", {
                "project_id": project_id,
                "status": status,
                "energy_savings": energy_savings
            })
            return f"Smart Grid Project {project_id} updated. Status: {status}, Energy Savings: {energy_savings}%"
        return f"Project ID {project_id} not found."

    # --- Equipment Commissioning ---
    def add_equipment(self, name: str, equipment_type: str, specs: Dict) -> str:
        """Add a new piece of equipment (e.g., transformer, switchgear)."""
        equipment_id = f"EQ{self.next_equipment_id}"
        self.next_equipment_id += 1
        self.equipment[equipment_id] = {
            "name": name,
            "type": equipment_type,
            "status": "Installed",
            "commissioning_date": None,
            "settings": specs,
            "behavior_verification": None
        }
        self._log_activity("equipment_added", {
            "equipment_id": equipment_id,
            "name": name,
            "type": equipment_type
        })
        return f"Equipment '{name}' added with ID: {equipment_id}"

    def commission_equipment(self, equipment_id: str, commissioning_date: str, behavior: Dict) -> str:
        """Commission equipment and verify its behavior under real operating conditions."""
        if equipment_id in self.equipment:
            self.equipment[equipment_id]["status"] = "Commissioned"
            self.equipment[equipment_id]["commissioning_date"] = commissioning_date
            self.equipment[equipment_id]["behavior_verification"] = behavior
            self._log_activity("equipment_commissioned", {
                "equipment_id": equipment_id,
                "commissioning_date": commissioning_date,
                "behavior": behavior
            })
            return f"Equipment {equipment_id} commissioned on {commissioning_date}. Behavior: {behavior}"
        return f"Equipment ID {equipment_id} not found."

    # --- System Settings ---
    def establish_system_setting(self, system_id: str, parameter: str, value: Union[float, str], impact: str) -> str:
        """Establish a system setting to improve stability and fault response."""
        if system_id in self.distribution_systems:
            setting_id = f"SET{self.next_setting_id}"
            self.next_setting_id += 1
            self.system_settings[setting_id] = {
                "system_id": system_id,
                "parameter": parameter,
                "value": value,
                "impact": impact
            }
            # Update system stability score based on settings
            self.distribution_systems[system_id]["stability_score"] = min(
                100, self.distribution_systems[system_id]["stability_score"] + 5
            )
            self._log_activity("system_setting_established", {
                "setting_id": setting_id,
                "system_id": system_id,
                "parameter": parameter,
                "value": value
            })
            return f"System Setting established with ID: {setting_id}. Impact: {impact}"
        return f"System ID {system_id} not found."

    # --- Audit Logging ---
    def _log_activity(self, action: str, details: Dict) -> None:
        """Log an activity to the audit trail."""
        log_entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "details": details
        }
        self.audit_logs.append(log_entry)

    def get_audit_logs(self) -> List[Dict]:
        """Retrieve all audit logs."""
        return self.audit_logs

    # --- Reporting ---
    def generate_system_report(self, system_id: str) -> Dict:
        """Generate a comprehensive report for a power distribution system."""
        if system_id in self.distribution_systems:
            system = self.distribution_systems[system_id]
            report = {
                "system_id": system_id,
                "name": system["name"],
                "voltage_level": system["voltage_level"],
                "status": system["status"],
                "stability_score": system["stability_score"],
                "components": system["components"],
                "load_studies": [ls for ls in self.load_studies.values() if ls["system_id"] == system_id],
                "short_circuit_analyses": [sc for sc in self.short_circuit_analyses.values() if sc["system_id"] == system_id],
                "protection_coordination": [pc for pc in self.protection_coordination.values() if pc["system_id"] == system_id],
                "system_settings": [ss for ss in self.system_settings.values() if ss["system_id"] == system_id]
            }
            return report
        return {"error": "System ID not found"}

    def generate_project_report(self) -> Dict:
        """Generate a report summarizing all Smart Grid projects and their outcomes."""
        report = {
            "total_projects": len(self.smart_grid_projects),
            "completed_projects": sum(1 for proj in self.smart_grid_projects.values() if proj["status"] == "Completed"),
            "avg_energy_savings": sum(
                proj["energy_savings"] for proj in self.smart_grid_projects.values()
            ) / len(self.smart_grid_projects) if self.smart_grid_projects else 0,
            "projects": [
                {
                    "name": proj["name"],
                    "status": proj["status"],
                    "energy_savings": proj["energy_savings"],
                    "completion_date": proj["completion_date"]
                }
                for proj in self.smart_grid_projects.values()
            ]
        }
        return report

    def generate_equipment_report(self) -> Dict:
        """Generate a report summarizing all commissioned equipment and their behavior."""
        report = {
            "total_equipment": len(self.equipment),
            "commissioned_equipment": sum(1 for eq in self.equipment.values() if eq["status"] == "Commissioned"),
            "equipment": [
                {
                    "name": eq["name"],
                    "type": eq["type"],
                    "status": eq["status"],
                    "commissioning_date": eq["commissioning_date"],
                    "behavior_verification": eq["behavior_verification"]
                }
                for eq in self.equipment.values()
            ]
        }
        return report

# --- Example Usage ---
if __name__ == "__main__":
    weco = ElectricalEngineerSystem()

    # Design power distribution systems
    print("=== Power Distribution System Design ===")
    print(weco.design_distribution_system("Industrial Park LV System", "Low Voltage"))
    print(weco.design_distribution_system("City Substation MV System", "Medium Voltage"))
    print(weco.add_component("DS1", "Transformer", {"capacity": "1000 kVA", "voltage_ratio": "11/0.4 kV"}))
    print(weco.add_component("DS1", "Switchgear", {"type": "LV", "rating": "1000A"}))
    print(weco.update_system_status("DS1", "Operational"))

    # Conduct load studies
    print("\n=== Load Studies ===")
    print(weco.conduct_load_study("DS1", "Load Flow"))
    print(weco.add_load_study_results("LS1", {
        "loading_percentage": 95,
        "voltage_drop": 6,
        "power_losses": "3.2%"
    }))

    # Conduct short circuit analysis
    print("\n=== Short Circuit Analysis ===")
    print(weco.conduct_short_circuit_analysis("DS1", "3-Phase"))
    print(weco.add_short_circuit_results("SC1", {
        "fault_current": 25000,
        "interrupting_rating": 20000,
        "fault_location": "Busbar A"
    }))

    # Protection coordination
    print("\n=== Protection Coordination ===")
    print(weco.create_protection_coordination("DS1"))
    print(weco.add_protection_setting("PC1", "Relay 1", {"type": "Overcurrent", "setting": "120%", "time_delay": "0.5s"}))
    print(weco.add_time_current_curve("PC1", {
        "device": "Relay 1",
        "curve_type": "Inverse Time",
        "points": [(0.1, 10), (0.5, 5), (1.0, 2)]
    }))

    # Smart Grid Modernization Project
    print("\n=== Smart Grid Modernization ===")
    print(weco.create_smart_grid_project("WECO Smart Grid Initiative", ["Alice", "Bob", "Charlie"]))
    print(weco.update_smart_grid_status("SG1", "Completed", 15.0, "2023-07-31"))

    # Equipment commissioning
    print("\n=== Equipment Commissioning ===")
    print(weco.add_equipment("Transformer T1", "Power Transformer", {"capacity": "2500 kVA", "voltage": "33/11 kV"}))
    print(weco.add_equipment("Switchgear S1", "MV Switchgear", {"rating": "1250A", "type": "Indoor"}))
    print(weco.commission_equipment("EQ1", "2023-06-15", {
        "voltage_regulation": "Within Limits",
        "temperature": "Normal",
        "noise_level": "Acceptable"
    }))
    print(weco.commission_equipment("EQ2", "2023-06-20", {
        "operation": "Smooth",
        "arc_resistance": "Tested",
        "interlocks": "Functional"
    }))

    # Establish system settings
    print("\n=== System Settings ===")
    print(weco.establish_system_setting("DS1", "Voltage Regulation", 1.05, "Improved voltage stability"))
    print(weco.establish_system_setting("DS1", "Fault Response Time", 0.2, "Faster fault clearing"))

    # Generate reports
    print("\n=== System Report for Industrial Park LV System ===")
    system_report = weco.generate_system_report("DS1")
    for key, value in system_report.items():
        print(f"{key}: {value}")

    print("\n=== Smart Grid Project Report ===")
    project_report = weco.generate_project_report()
    for key, value in project_report.items():
        print(f"{key}: {value}")

    print("\n=== Equipment Report ===")
    equipment_report = weco.generate_equipment_report()
    for key, value in equipment_report.items():
        print(f"{key}: {value}")
