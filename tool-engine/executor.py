import subprocess

ALLOWED_COMMANDS = ["ls", "pwd", "whoami"]

def safe_execute(command):
    base = command.split()[0]
    if base in ALLOWED_COMMANDS:
        return subprocess.getoutput(command)
    return "Command not allowed."
