def generate_first_line(company):
    desc = company.get("description", "").lower()
    name = company.get("name", "")

    if "cut" in desc or "machine" in desc:
        return "Noticed your focus on industrial cutting and machine solutions—curious how you're helping manufacturers improve precision without compromising speed."

    elif "composite" in desc:
        return "Saw your work in composite materials—interested in how you're helping manufacturers balance strength, weight, and production efficiency."

    elif "energy" in desc or "transport" in desc:
        return "Noticed your work in transportation and energy solutions—curious how you're supporting evolving material and performance demands in these sectors."

    else:
        return f"Noticed your presence at CAMX—curious what key solutions you're focusing on this year for manufacturers."