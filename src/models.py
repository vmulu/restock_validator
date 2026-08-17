"""
Defining our data model RestockItem using pydantic
"""

from typing import Literal
from pydantic import BaseModel, Field

Category = Literal["electronics", "perishable", "apparel", "hardware"]

class RestockItem(BaseModel):
    """
    Blueprint for RestockItem objects
    """

    sku : str
    warehouse : str
    quantity : int = Field(gt=0)
    unit_cost : float = Field(gt=0)
    category : Category