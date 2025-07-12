import json
from pricing_logic.material_db import get_material_costs
from pricing_logic.labor_calc import estimate_labor
from pricing_logic.vat_rules import get_vat

# Sample input transcript
transcript = """Client wants to renovate a small 4m² bathroom. 
They’ll remove the old tiles, redo the plumbing for the shower, 
replace the toilet, install a vanity, repaint the walls, 
and lay new ceramic floor tiles. Budget-conscious. Located in Marseille."""

# Parse input (simplified for now)
tasks = [
    "Remove old tiles",
    "Redo plumbing for shower",
    "Replace toilet",
    "Install vanity",
    "Repaint walls",
    "Lay ceramic floor tiles"
]

location = "Marseille"
area = 4  # m²
vat_rate = get_vat(location)

task_outputs = []
total_quote = 0

for task in tasks:
    materials = []
    if "plumbing" in task:
        materials = ["pipes", "fittings"]
    elif "toilet" in task:
        materials = ["toilet"]
    elif "vanity" in task:
        materials = ["vanity"]
    elif "paint" in task:
        materials = ["paint"]
    elif "tiles" in task:
        materials = ["ceramic tiles"]

    material_cost = get_material_costs(materials)
    labor_hours, labor_cost = estimate_labor(task, location)
    margin = 0.15
    base_cost = labor_cost + material_cost
    total_cost = base_cost * (1 + vat_rate) * (1 + margin)

    task_outputs.append({
        "zone": task.split()[0],
        "task": task,
        "materials": materials,
        "labor_hours": labor_hours,
        "labor_cost": labor_cost,
        "material_cost": material_cost,
        "vat_rate": vat_rate,
        "margin": margin,
        "total_cost": round(total_cost, 2),
        "confidence_score": 0.9
    })

    total_quote += total_cost

# -----------------------
# ✅ Feedback Loop Section
# -----------------------

# Load feedback from data/feedback.json
try:
    with open("data/feedback.json", "r") as f:
        feedback_data = json.load(f)
except FileNotFoundError:
    feedback_data = {"adjustments": {}}

# Apply feedback to adjust confidence scores
for task in task_outputs:
    task_name = task["task"]
    feedback = feedback_data["adjustments"].get(task_name)
    if feedback and "confidence_score" in feedback:
        task["confidence_score"] = feedback["confidence_score"]

# -----------------------
# ✅ Build final quote JSON
# -----------------------

quote = {
    "project": "Full Bathroom Renovation",
    "location": location,
    "area_m2": area,
    "tasks": task_outputs,
    "total_quote": round(total_quote, 2),
    "notes": "Budget-conscious",
    "error_flags": []
}

# Save output to JSON file
with open("output/sample_quote.json", "w") as f:
    json.dump(quote, f, indent=2)

print("✅ Quote generated successfully!")






