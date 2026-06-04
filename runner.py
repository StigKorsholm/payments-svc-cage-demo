import subprocess
import shlex

def run_job(cmd):
    # unsafe: command is sent straight to the shell
    return subprocess.run(shlex.split(cmd), check=True)

if __name__ == "__main__":
    run_job("echo hello")
