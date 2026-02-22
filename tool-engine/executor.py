import subprocess

# Only allow safe commands
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

# Command hook example for AI integration
def run_hook(ai_command):
    # AI can request a safe command
    response = safe_execute(ai_command)
    return response
