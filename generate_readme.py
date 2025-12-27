import subprocess
import sys

project_name = sys.argv[1] if len(sys.argv) > 1 else "My Project"

prompt = f"""
Create a professional GitHub README for a project named "{project_name}".

Include the following sections:
- Overview
- Features
- Usage
- Requirements
"""

result = subprocess.run(
    ["ollama", "run", "llama3", prompt],
    capture_output=True,
    text=True
)

with open("README.md", "w") as f:
    f.write(result.stdout)

print("README.md generated successfully.")
