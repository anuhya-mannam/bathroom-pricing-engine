# 🚿 Donizo – Smart Bathroom Pricing Engine

This Python project builds a structured renovation quote from a plain-English client transcript using modular pricing logic.

---

## 🔧 How to Run

```bash
python pricing_engine.py
bathroom-pricing-engine/
├── pricing_engine.py
├── pricing_logic/
│   ├── material_db.py
│   ├── labor_calc.py
│   └── vat_rules.py
├── data/
│   ├── materials.json
│   ├── price_templates.csv
│   └── feedback.json
├── output/
│   └── sample_quote.json
├── tests/
│   └── test_logic.py
└── README.md
{
  "project": "Full Bathroom Renovation",
  "location": "Marseille",
  "tasks": [
    {
      "task": "Replace toilet",
      "confidence_score": 0.95,
      ...
    }
  ],
  "total_quote": 1490.4
}
Assumptions
Flat hourly labor rate by city (e.g., Paris higher than Marseille)

Prices based on hardcoded values in materials.json

Margin set at 15%

VAT pulled dynamically from city name

Area-based pricing can be extended
