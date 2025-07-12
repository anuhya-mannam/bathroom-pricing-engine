📂 Project Structure
bathroom-pricing-engine/
├── pricing_engine.py
├── pricing_logic/
│   ├── material_db.py
│   ├── labor_calc.py
│   └── vat_rules.py
├── data/
│   ├── materials.json
│   └── price_templates.csv
├── output/
│   └── sample_quote.json
├── tests/
│   └── test_logic.py
├── README.md
🧠 Pricing Logic
Parses transcript and extracts tasks

Estimates material and labor costs per task

Applies location-based pricing (Marseille)

Adds margin (15%) and VAT (20%)

Outputs structured quote with confidence score
📝 Assumptions
Transcript is in English and manually handled

Pricing logic is hardcoded for MVP

City-based pricing handled via internal functions

Extendable to Paris or real APIs
✅ Sample Output
Example in sample_quote.json:

json
Copy
Edit
{
  "project": "Full Bathroom Renovation",
  "location": "Marseille",
  "area_m2": 4,
  "tasks": [...],
  "total_quote": 1490.4,
  "notes": "Budget-conscious"
}

---

### 💾 2. **Save the README**

Press:

