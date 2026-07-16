import os
import sys

# Ensure project root is on sys.path so 'src' package can be imported in tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
