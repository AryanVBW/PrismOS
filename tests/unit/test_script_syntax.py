import subprocess
import os

def test_install_sh_syntax():
    """Test that install.sh has valid bash syntax"""
    if os.path.exists("install.sh"):
        result = subprocess.run(["bash", "-n", "install.sh"], capture_output=True, text=True)
        assert result.returncode == 0, f"install.sh has syntax errors: {result.stderr}"

def test_step2_sh_syntax():
    """Test that step2.sh has valid bash syntax"""
    if os.path.exists("step2/step2.sh"):
        result = subprocess.run(["bash", "-n", "step2/step2.sh"], capture_output=True, text=True)
        assert result.returncode == 0, f"step2.sh has syntax errors: {result.stderr}"
