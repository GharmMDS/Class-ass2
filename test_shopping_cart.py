import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shopping_cart import calculate_total
from localization import MESSAGES 

def test_calculate_total_zero_items():
    """Test calculating total with an empty list of items."""
    assert calculate_total([]) == 0.0

def test_calculate_total_one_item():
    """Test calculating total with a single item."""
    items = [(10.50, 2)] 
    assert calculate_total(items) == 21.0

def test_calculate_total_multiple_items():
    """Test calculating total with multiple items."""
    items = [
        (5.0, 3),   # 15.0
        (2.25, 4),  #  9.0S
        (100.0, 1)  # 100.0
    ]
    assert calculate_total(items) == pytest.approx(124.0)

def test_calculate_total_zero_quantity():
    """Test calculating total when quantity is zero."""
    items = [(50.0, 0)]
    assert calculate_total(items) == 0.0

def test_calculate_total_zero_price():
    """Test calculating total when price is zero."""
    items = [(0.0, 5)]
    assert calculate_total(items) == 0.0

