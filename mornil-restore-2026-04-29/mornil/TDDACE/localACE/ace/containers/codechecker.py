import subprocess

print("YOU HAVE REACHED CODECHECKER")

result = subprocess.run(
    [
        "apptainer",
        "exec",
	"--containall",
        "--bind", "workspace:/mnt",
        "containers/python-testing.sif",
        "pytest",
        "/mnt/tests",
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
