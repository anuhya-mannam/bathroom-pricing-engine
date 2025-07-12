import unittest
from pricing_logic.material_db import get_material_costs
from pricing_logic.labor_calc import estimate_labor
from pricing_logic.vat_rules import get_vat

class TestPricingLogic(unittest.TestCase):

    def test_material_costs(self):
        materials = ['vanity', 'toilet']
        expected = 270  # vanity=150, toilet=120 (from materials.json)
        result = get_material_costs(materials)
        self.assertEqual(result, expected)

    def test_labor_estimate(self):
        task = "Install vanity"
        expected_hours = 3  # from hardcoded logic
        expected_cost = 90  # 3 hrs * 30 €/hr
        hours, cost = estimate_labor(task)
        self.assertEqual(hours, expected_hours)
        self.assertEqual(cost, expected_cost)

    def test_vat_rule(self):
        city = "Marseille"
        vat = get_vat(city)
        self.assertEqual(vat, 0.2)

if __name__ == '__main__':
    unittest.main()
