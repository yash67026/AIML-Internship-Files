ml_ideas = {
    "College": {
        "Problem": "Predict student performance",
        "Input": ["Study hours", "Attendance", "Previous marks"],
        "Output": "Predicted final exam marks"
    },

    "Healthcare": {
        "Problem": "Disease prediction",
        "Input": ["Age", "Blood pressure", "Sugar level"],
        "Output": "Disease risk (Yes/No)"
    },

    "Shopping": {
        "Problem": "Product recommendation",
        "Input": ["User purchase history", "Product ratings"],
        "Output": "Recommended products"
    },

    "Traffic": {
        "Problem": "Traffic congestion prediction",
        "Input": ["Time", "Weather", "Vehicle count"],
        "Output": "Traffic level"
    }
}

for domain, details in ml_ideas.items():
    print("\nDomain:", domain)
    print("Problem:", details["Problem"])
    print("Input:", details["Input"])
    print("Output:", details["Output"])
    