import subprocess

result = subprocess.run(
    [
        "pylint",
        "./badcode.py",
        "-v"
    ],
    capture_output=True,
    text=True,
    timeout=30
)

print("Exit code:", result.returncode)
print("STDOUT:")
print(result.stdout)
print("STDERR:")
print(result.stderr)

print("=========== CODE QUALITY ==========")
print(result)
print("=========== END ==========")

import re
match = re.findall(r'Your code has been rated at (\d+(?:\.\d+)?/\d+)', str(result))
resultcode = "error"
# print("--->", result.split("=========================")[-2], "<---")
if len(match)!=0:
    print("->", match)
    print("->", match[-1])
