import subprocess

result = subprocess.run(
    [
        "apptainer",
        "exec",
	"--containall",
        "--bind", f"../workspace:/mnt",
        "python-testing.sif",
        "python",
        "/mnt/temp.py"
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
