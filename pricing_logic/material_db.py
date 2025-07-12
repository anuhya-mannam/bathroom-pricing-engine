# Example material database (you may already have this)
material_prices = {
    "vanity": 150,
    "toilet": 120,
    "pipes": 30,
    "fittings": 30,
    "paint": 50,
    "ceramic tiles": 100
}

def get_material_costs(materials):
    return sum(material_prices.get(m, 0) for m in materials)


