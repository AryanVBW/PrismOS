#!/usr/bin/env python3
"""
Test Runner Script for PrismOS Installation Tests
"""
import subprocess
import sys

def run_tests():
    """Run all tests and display summary"""
    print("🚀 Running PrismOS Installation Tests...")
    print("=" * 50)
    
    # Run unit tests
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        "tests/unit/", "-v", "--tb=short"
    ], capture_output=True, text=True)
    
    print("UNIT TESTS RESULTS:")
    print(result.stdout)
    
    if result.returncode != 0:
        print("❌ Some tests failed!")
        return result.returncode
    else:
        print("✅ All tests passed!")
        return 0

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)
