import requests
import sys
import json

project_name = sys.argv[1] if len(sys.argv) > 1 else "My Project"

prompt = f"""
Create a professional GitHub README for a project named "{project_name}".

Include the following sections:
- Overview
- Features
- Usage
- Requirements
"""

url = "http://localhost:11434/api/generate"

payload = {
    "model": "mistral",
    "prompt": prompt,
    "stream": True
}

print("Generating README using Ollama...\n")

response = requests.post(url, json=payload, stream=True)

output = []

for line in response.iter_lines():
    if line:
        data = json.loads(line.decode("utf-8"))
        token = data.get("response", "")
        output.append(token)
        print(token, end="", flush=True)

readme_text = "".join(output)

with open("README.md", "w") as f:
    f.write(readme_text)

print("\n\nREADME.md generated successfully.")

