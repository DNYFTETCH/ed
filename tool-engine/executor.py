import subprocess

ALLOWED_COMMANDS = ["ls", "pwd", "whoami", "date", "uptime"]

def safe_execute(command):
    base = command.split()[0]
    if base in ALLOWED_COMMANDS:
        try:
            result = subprocess.getoutput(command)
            return f"[EXECUTED] {command}\n{result}"
        except Exception as e:
            return f"Error executing command: {e}"
    return f"Command not allowed: {command}"

# Hook example
def run_hook(ai_command):
    return safe_execute(ai_command)
