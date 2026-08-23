import subprocess

def hello():
    output = subprocess.check_output(["whoami"], text=True)
    return f"Hacked by Joex!! your username: {output}"
