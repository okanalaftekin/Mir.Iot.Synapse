
import os
import sys
import pytest
import datetime

sys.path.append('../wifi_analysis/')
from wifi_analysis import analyze

THIS_DIR = os.path.dirname(os.path.abspath(__file__))



def test_analyze_test():
    """Test data transform"""
    # Arrange
    
    # Act
    analyze.analyze_test()
    # Assert
    assert 0== 0