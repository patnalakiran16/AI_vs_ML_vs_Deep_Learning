# AI, Machine Learning, and Deep Learning Comparison

# Store information about AI, ML, and Deep Learning
technologies = {
    "Artificial Intelligence (AI)": {
        "definition": "AI helps machines perform tasks that need human intelligence.",
        "examples": "Virtual assistants and expert systems"
    },
    "Machine Learning (ML)": {
        "definition": "ML helps computers learn from data and make predictions.",
        "examples": "Spam email detection and product recommendations"
    },
    "Deep Learning (DL)": {
        "definition": "DL uses neural networks to learn complex patterns from data.",
        "examples": "Image recognition and speech recognition"
    }
}

# Print the details of each technology
for name, details in technologies.items():
    print("\nTechnology:", name)
    print("Definition:", details["definition"])
    print("Examples:", details["examples"])

# Explain how AI, ML, and DL are related
print("\nRelationship between AI, ML, and DL:")
print("AI is the broader field of intelligent machines.")
print("ML is a part of AI that learns from data.")
print("DL is a part of ML that uses deep neural networks.")
