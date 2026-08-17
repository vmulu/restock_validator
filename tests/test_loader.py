"""
Tests for loading our data from JSON
"""

import pytest
from pydantic import ValidationError
from src.models import RestockItem
from src.store import load_manifest, ManifestFileNotFoundError, RestockItemError

def test_valid_row_load_correctly():
    """
    Testing if a row loads correctly
    """
    load_row = RestockItem.model_validate(
        {"sku": "SKU-1001",
         "warehouse": "west-1",
         "quantity": 25,
         "unit_cost": 12.50,
         "category": "electronics"}
    )

    expected = RestockItem(
        sku="SKU-1001",
        warehouse="west-1",
        quantity=25,
        unit_cost=12.50,
        category="electronics",
    )

    assert load_row == expected

@pytest.mark.parametrize(
    "field, value",
    [
        ("category", "Hello"),
        ("quantity", -1),
        ("unit_cost", -1)
    ],
)

def test_invalid_fields(field, value):
    """
    Testing that mod handles invalid fields correctly
    """
    test_data = {"sku": "SKU-1001",
         "warehouse": "west-1",
         "quantity": 25,
         "unit_cost": 12.50,
         "category": "electronics"}

    # replace test data field with parametrized value
    test_data[field] = value

    # we expect to see a error
    with pytest.raises(ValidationError) : RestockItem.model_validate(test_data)

def test_load_manifest_with_path():
    """
    Testing if we get valid and invalid items correctly
    """
    test_valid_items, test_invalid_items = load_manifest("data/restock_manifest.json")

    assert len(test_valid_items) == 8
    assert len(test_invalid_items) == 4

def test_load_manifest_with_no_path():
    """
    Testing load_manifest works with no path and goes to default
    """
    test_valid_items, test_invalid_items = load_manifest()

    assert len(test_valid_items) == 8
    assert len(test_invalid_items) == 4

def test_restock_item_error(tmp_path):
    """
    Testing if custom RestockItemError exceptions works correctly
    """
    # pytest tmp_path gives a temp path so we don't need to create file with bad data
    bad_path = tmp_path / "restock_manifest.json"
    bad_path.write_text("{ bad data", encoding="utf-8")

    with pytest.raises(RestockItemError) : load_manifest(bad_path)

def test_manifest_file_not_found():
    """
    Testing if custom ManifestFileNotFound exception works correctly
    when invalid path is given
    """

    with pytest.raises(ManifestFileNotFoundError) : load_manifest("doesn't/exist")