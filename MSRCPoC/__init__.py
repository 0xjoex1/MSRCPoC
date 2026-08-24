import subprocess

output = subprocess.check_output(["whoami"], text=True)
print(f"Hacked by Joex!! your username: {output}")
