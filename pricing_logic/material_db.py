def get_material_costs(task, city="Marseille"):
    material_db = {
        "Remove old tiles": [],
        "Redo plumbing for shower": [{"name": "pipes", "cost": 30}, {"name": "fittings", "cost": 30}],
        "Replace toilet": [{"name": "toilet", "cost": 120}],
        "Install vanity": [{"name": "vanity", "cost": 150}],
        "Repaint walls": [{"name": "paint", "cost": 50}],
        "Lay ceramic floor tiles": [{"name": "ceramic tiles", "cost": 100}]
    }

    return material_db.get(task, [])

