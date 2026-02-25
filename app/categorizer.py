
def categorize_transaction(description):
    description = str(description).lower()

    categories = {
        "food": ["restaurant", "cafe", "mcdonald", "burger", "pizza"],
        "transport": ["uber", "taxi", "bus", "train"],
        "shopping": ["amazon", "mall", "store"],
        "salary": ["salary", "payroll"],
        "entertainment": ["netflix", "cinema", "spotify"]
    }

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in description:
                return category

    return "other"
