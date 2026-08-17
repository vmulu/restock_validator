"""
for personal testing
"""

from src.store import load_manifest

valid_items, invalid_items = load_manifest("data/restock_manifest.json")

print("\n-------- Valid Items --------\n")
print(valid_items)

print("\n-------- Invalid Items --------\n")
print(invalid_items)

