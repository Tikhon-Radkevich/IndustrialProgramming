import logging
import subprocess
import sys

from Packages import create_cache_dir, clear_cache_dir
from config import CACHE_DIR


def main():



    try:
        if len(sys.argv) != 2:
            logging.error("Usage: python main.py [gui|web]")
            sys.exit(1)

        arg = sys.argv[1]
        create_cache_dir(CACHE_DIR)

        if arg == "gui":
            from GUI.main import main as gui_main
            gui_main()
        elif arg == "web":
            script_path = "api/run_server.sh"
            try:
                logging.info("Starting the web server...")
                subprocess.run(["bash", script_path], check=True)
            except subprocess.CalledProcessError as e:
                logging.error(f"Error running the script: {e}")
        else:
            logging.error("Invalid argument. Use 'gui' or 'web'")
    except Exception as e:
        logging.exception(f"An error occurred: {e}")
    finally:
        logging.info("Cleaning up...")
        clear_cache_dir(CACHE_DIR)
        logging.info("Exiting.")


if __name__ == "__main__":
    main()
