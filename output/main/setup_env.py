import subprocess
import sys
import os

def setup_virtual_environment(venv_name="venv", requirements_file="requirements.txt"):
    """
    Creates a virtual environment and installs packages from a requirements.txt file.

    Args:
        venv_name (str): The name of the virtual environment directory. Defaults to "venv".
        requirements_file (str): The path to the requirements.txt file.
                                 Defaults to "requirements.txt".
    """
    print(f"Starting virtual environment setup...")

    # 1. Check if requirements.txt exists
    if not os.path.exists(requirements_file):
        print(f"Error: '{requirements_file}' not found in the current directory.")
        print("Please make sure you have a requirements.txt file.")
        return

    # 2. Define the path to the virtual environment
    venv_path = os.path.join(os.getcwd(), venv_name)
    print(f"Virtual environment path: {venv_path}")

    # 3. Create the virtual environment if it doesn't exist
    if not os.path.exists(venv_path):
        print(f"Creating virtual environment '{venv_name}'...")
        try:
            # Use sys.executable to ensure the correct Python interpreter is used
            subprocess.run([sys.executable, "-m", "venv", venv_name], check=True)
            print(f"Virtual environment '{venv_name}' created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating virtual environment: {e}")
            return
    else:
        print(f"Virtual environment '{venv_name}' already exists. Skipping creation.")

    # 4. Determine the path to the pip executable within the virtual environment
    if sys.platform == "win32":
        pip_executable = os.path.join(venv_path, "Scripts", "pip")
    else:
        pip_executable = os.path.join(venv_path, "bin", "pip")

    # 5. Install packages from requirements.txt using the venv's pip
    print(f"Installing packages from '{requirements_file}' into '{venv_name}'...")
    try:
        # Run pip install using the venv's pip executable
        subprocess.run([pip_executable, "install", "-r", requirements_file], check=True)
        print("Packages installed successfully!")
    except FileNotFoundError:
        print(f"Error: pip executable not found at '{pip_executable}'.")
        print("This might indicate an issue with the virtual environment creation.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("\nSetup complete.")
    print(f"To activate the virtual environment, run:")
    if sys.platform == "win32":
        print(f"  .\\{venv_name}\\Scripts\\activate")
    else:
        print(f"  source ./{venv_name}/bin/activate")

if __name__ == "__main__":
    # You can customize the venv_name and requirements_file here if needed
    setup_virtual_environment(venv_name="tts_stt_thesis", requirements_file="requirements.txt")