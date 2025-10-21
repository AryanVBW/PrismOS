import os
import subprocess

def test_install_script_exists():
    """Test that main installation script exists"""
    assert os.path.exists("install.sh")

def test_install_script_executable():
    """Test that install script is executable"""
    assert os.access("install.sh", os.X_OK)

def test_step2_script_exists():
    """Test that step2 installation script exists"""
    assert os.path.exists("step2/step2.sh")
