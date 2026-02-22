import subprocess
ALLOWED = ["ls", "pwd", "whoami", "date", "uptime"]

def safe_execute(cmd):
    base = cmd.split()[0]
    if base in ALLOWED:
        return subprocess.getoutput(cmd)
    return f"Command not allowed: {cmd}"
