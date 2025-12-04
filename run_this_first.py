import os
import sys
import subprocess
import platform
import shutil

PROJECT_NAME = "OFFLINE-AI"
REQUIRED_FILES = [
    "launcher.py",
    "launcher_gui.py",
    "requirements.txt",
    "config/features.json"
]

REQUIRED_DIRS = [
    "models",
    "web",
    "plugins",
    "scripts",
    "optional_features",
    "config"
]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def title():
    print("=" * 60)
    print(f"{PROJECT_NAME} — FIRST TIME SETUP & SYSTEM CHECK")
    print("=" * 60)
    print()


def check_python():
    print("[1/7] Checking Python...")
    if sys.version_info < (3, 9):
        print("❌ Python version too old! Need 3.9+")
        sys.exit(1)
    print(f"✅ Python OK ({sys.version.split()[0]})")


def check_files():
    print("[2/7] Checking required files...")
    missing = []
    for f in REQUIRED_FILES:
        if not os.path.exists(f):
            missing.append(f)

    if missing:
        print("❌ Missing required files:")
        for f in missing:
            print(" -", f)
        print("\nFix this before continuing.")
        sys.exit(1)

    print("✅ All required files found.")


def check_dirs():
    print("[3/7] Checking directories...")
    for d in REQUIRED_DIRS:
        if not os.path.exists(d):
            print(f"⚠ Missing folder: {d} → Creating it.")
            os.makedirs(d)
    print("✅ Directory structure OK.")


def create_venv():
    print("[4/7] Setting up virtual environment...")
    if os.path.exists("venv"):
        print("✅ venv already exists.")
        return

    subprocess.check_call([sys.executable, "-m", "venv", "venv"])
    print("✅ venv created.")


def get_pip_path():
    if os.name == "nt":
        return os.path.join("venv", "Scripts", "pip")
    else:
        return os.path.join("venv", "bin", "pip")


def get_python_path():
    if os.name == "nt":
        return os.path.join("venv", "Scripts", "python")
    else:
        return os.path.join("venv", "bin", "python")


def install_dependencies():
    print("[5/7] Installing dependencies...")
    pip_path = get_pip_path()

    if not os.path.exists(pip_path):
        print("❌ pip not found in venv.")
        sys.exit(1)

    subprocess.check_call([pip_path, "install", "--upgrade", "pip"])
    subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])
    print("✅ Dependencies installed.")


def safe_config_check():
    print("[6/7] Verifying SAFE DEFAULT configuration...")
    config_path = "config/features.json"

    if not os.path.exists(config_path):
        print("⚠ features.json not found → creating SAFE DEFAULT config")

        safe_config = """
{
  "enable_gpu_check": false,
  "enable_auto_update": false,
  "enable_model_downloader": false,
  "enable_telemetry": false,
  "enable_cloud_bridge": false,
  "enable_plugins": false,
  "enable_license_system": false,
  "enable_web_dashboard": false,
  "enable_system_monitor": false
}
"""
        with open(config_path, "w", encoding="utf-8") as f:
            f.write(safe_config.strip())

    print("✅ SAFE DEFAULT config verified.")


def offer_launch():
    print("\n[7/7] Setup complete.")
    print("=" * 60)
    answer = input("✅ Do you want to start OFFLINE-AI now? (y/n): ").lower()

    if answer == "y":
        python_path = get_python_path()
        if os.path.exists("launcher_gui.py"):
            subprocess.call([python_path, "launcher_gui.py"])
        else:
            subprocess.call([python_path, "launcher.py"])


def main():
    clear()
    title()
    check_python()
    check_files()
    check_dirs()
    create_venv()
    install_dependencies()
    safe_config_check()
    offer_launch()

    print("\n✅ FIRST TIME SETUP FINISHED SUCCESSFULLY.")
    input("Press ENTER to exit...")


if __name__ == "__main__":
    main()
