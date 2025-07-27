import importlib
import subprocess
import sys

# List of required packages
required_packages = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "xgboost",
    "statsmodels",
    "jupyter"
]

def install(package):
    """Install a package using pip."""
    print(f"Installing missing package: {package}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install(packages):
    """Check for packages, install if missing."""
    for package in packages:
        try:
            importlib.import_module(package)
            print(f"{package} is already installed.")
        except ImportError:
            install(package)

if __name__ == "__main__":
    check_and_install(required_packages)
    print("All packages are installed and ready.")