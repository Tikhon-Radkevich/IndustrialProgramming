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
        ...
        # from web.main import web_main_function
        # web_main_function()
    else:
        print("Invalid argument. Use 'gui' or 'web'")
except Exception as e:
    print(e)
finally:
    clear_cache_dir(CACHE_DIR)
    exit(0)
