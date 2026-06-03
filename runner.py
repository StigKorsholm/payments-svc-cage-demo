import os

def run_job(cmd):
    # unsafe: command is sent straight to the shell
    return os.system(cmd)

if __name__ == "__main__":
    run_job("echo hello")
