import subprocess

def name():
    return "demoProject1"

def build():
    try:
        print(f"Building {name()}")
        subprocess.check_call(['gcc', './demoProject/test_program.c', '-o', f'./build/{name()}'])
    except subprocess.CalledProcessError as e:
        print("Build failed", e.output)


def run():
    print(f"Running {name()}")
    subprocess.check_call([f'./build/{name()}'])
