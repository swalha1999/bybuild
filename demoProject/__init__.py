import subprocess

def name():
    
    """
    Return the name of the project.
    """
    
    return "demoProject1"

def build():
    
    """
    Run the build process for the project.
    """
    
    try:
        print(f"Building {name()}")
        subprocess.check_call(['gcc', './demoProject/test_program.c', '-o', f'./build/{name()}'])
    except subprocess.CalledProcessError as e:
        print("Build failed", e.output)

def run():
    
    """
    Run the build process for the project.
    """

    print(f"Running {name()}")
    subprocess.check_call([f'./build/{name()}'])

def test():
    
    """
    Run the test process for the project.
    """
    
    print(f"Testing {name()}")


def clean():
    
    """
    Run the clean process for the project.
    """
    
    print(f"Cleaning {name()}")


def deps():
    
    """
    Return the dependencies for the project.
    we use this to determine the order in which to build the projects.
    """
    
    return ['demoProject2']