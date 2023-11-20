import subprocess
import sys

from Packages import create_cache_dir, clear_cache_dir
from config import CACHE_DIR

if len(sys.argv) != 2:
    print("Usage: python main.py [gui|web]")
    sys.exit(1)

try:
    arg = sys.argv[1]
    create_cache_dir(CACHE_DIR)
    if arg == "gui":
        from GUI.main import main
        main()
    elif arg == "web":
        # todo script path?
        script_path = "api/run_server.sh"
        try:
            subprocess.run(["bash", script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running the script: {e}")
    else:
        print("Invalid argument. Use 'gui' or 'web'")
except Exception as e:
    print(e)
finally:
    clear_cache_dir(CACHE_DIR)
    exit(0)
