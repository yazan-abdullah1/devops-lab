import subprocess
import sys

result = subprocess.run(
    [sys.executable, "app.py"],
    capture_output=True,
    text=True
)

assert result.returncode == 0

assert "My name is Yazan" in result.stdout

print("Test passed!")
