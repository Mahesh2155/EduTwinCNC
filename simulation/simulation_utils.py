# simulation_utils.py
def simulate_toolpath(toolpath):
    """Simulate toolpath in console (simple example)."""
    for path in toolpath:
        print(f"Moving from {path['start']} to {path['end']}...")
