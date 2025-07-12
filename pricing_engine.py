import json
import os
from pricing_logic.material_db import get_material_costs
from pricing_logic.labor_calc import estimate_labor
from pricing_logic.vat_rules import get_vat

# 1. Input Transcript (hardcoded for now)
transcript = """
Client wants to renovate a small 4m² bathroom. They’ll remove the old tiles, redo the plumbing for the shower, replace the toilet, install a vanity, repaint the walls, and lay new ceramic floor tiles. Budget-conscious. Located in Marseille.
"""

# 2. Extract details (simplified logic)
tasks = [
    "Remove old tiles",
    "Redo plumbing for shower",
    "Replace toilet",
    "Install vanity",
    "Repaint walls",
    "Lay ceramic floor tiles"
]

project = {
    "project": "Full Bathroom Renovation",
    "location": "Marseille",
    "area_m2": 4,
    "tasks": [],
    "total_quote": 0,
    "notes": "Budget-conscious",
    "error_flags": []
}

city = "Marseille"
margin = 0.15  # Budget-conscious logic

# 3. Loop through tasks
total = 0
for task in tasks:
    materials = get_material_costs(task, city)
    labor_hours, labor_cost = estimate_labor(task, city)
    material_cost = sum(m["cost"] for m in materials)
    vat = get_vat(task)
    confidence_score = 0.9

    subtotal = labor_cost + material_cost
    subtotal_with_margin = subtotal * (1 + margin)
    total_with_vat = subtotal_with_margin * (1 + vat)

    task_data = {
        "zone": task.split()[0],  # Rough zone
        "task": task,
        "materials": [m["name"] for m in materials],
        "labor_hours": labor_hours,
        "labor_cost": labor_cost,
        "material_cost": material_cost,
        "vat_rate": vat,
        "margin": margin,
        "total_cost": round(total_with_vat, 2),
        "confidence_score": confidence_score
    }

    project["tasks"].append(task_data)
    total += total_with_vat

project["total_quote"] = round(total, 2)

# ✅ Write to sample_quote.json
try:
    with open("output/sample_quote.json", "w", encoding="utf-8") as f:
        json.dump(project, f, indent=2)
    print("✅ Quote written to:", os.path.abspath("output/sample_quote.json"))
except Exception as e:
    print("❌ Failed to write file:", e)

# 🖨️ Also print to terminal
print(json.dumps(project, indent=2))





