import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import soma

def test_soma():
    assert soma(1, 2) == 3