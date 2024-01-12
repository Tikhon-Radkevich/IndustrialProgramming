from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

from time import sleep


def test_file_uploading(link, file_path, file_option, crypt_key):
    driver = webdriver.Chrome()
    try:
        driver.get(link)
        print("start of test in 5 sec...")
        sleep(5)

        file_input = driver.find_element(By.ID, "file")
        file_input.send_keys(file_path)
        print("file is selected -", file_path.split("/")[-1])
        sleep(3)

        file_option_dropdown = driver.find_element(By.ID, "fileOption")
        file_option_dropdown.send_keys(file_option)
        print("file option selected -", file_option)
        sleep(3)

        key_input = driver.find_element(By.ID, "keyInput")
        key_input.send_keys(crypt_key)
        print("crypt key typed -", crypt_key)
        sleep(3)

        confirm_button = driver.find_element(By.ID, "uploadConfirmButton")
        confirm_button.click()
        print("confirm button pressed.")

        print("end of test")
        sleep(10)

    finally:
        # Close the browser window
        driver.quit()


def main():
    FILE_PATH = "/home/tikhon/PycharmProjects/IndustrialProgramming/data/working/zip_crypt.zip"
    CRYPT_KEY = "VHnr250hvOL4g_Bt2ASwcY0ZTkcxmXoYKZuxS26uT1E="
    FILE_OPTION = "Decrypt -> Unzip"
    LINK = "http://127.0.0.1:8000/"

    print("downloading chromedriver...")
    chromedriver_autoinstaller.install()

    test_file_uploading(LINK, FILE_PATH, FILE_OPTION, CRYPT_KEY)


if __name__ == "__main__":
    main()
