def estimate_labor(task, city="Marseille"):
    hourly_rates = {
        "Marseille": 30,
        "Paris": 40
    }

    labor_hours = {
        "Remove old tiles": 3,
        "Redo plumbing for shower": 6,
        "Replace toilet": 2,
        "Install vanity": 3,
        "Repaint walls": 2,
        "Lay ceramic floor tiles": 4
    }

    hours = labor_hours.get(task, 2)  # Default to 2 hours if not found
    rate = hourly_rates.get(city, 30)  # Default to Marseille rate

    return hours, hours * rate

