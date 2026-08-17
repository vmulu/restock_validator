"""




"""

import json
from pathlib import Path
from src.models import RestockItem
from pydantic import ValidationError

class RestockItemError(Exception):
    """
    Base exception for all errors in this mod
    """

class ManifestFileNotFound(RestockItemError):
    """
    Exception raised when the manifest file doesn't exist on disk
    """

def load_manifest(path) -> tuple[list[RestockItem], list[dict]]:
    """
    Loads items from JSON file
    """

    resolved_path = Path(path).parent / "data" / "restock_manifest.json"

    # try reading
    try:
        raw_text = resolved_path.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        raise ManifestFileNotFound(f"No restock items found at {resolved_path}") from e

    # load info
    try:
        rows = json.loads(raw_text)
    except json.JSONDecodeError as e:
        raise RestockItemError(f"Item data could not be loaded from {resolved_path}") from e

    valid_items : list[RestockItem] = []
    invalid_items : list[dict] = []

    # adding valid and invalid items
    for row in rows:
        try:
            valid_items.append(RestockItem.model_validate(row))
        except ValidationError as e:
            invalid_items.append(row)

    return valid_items, invalid_items