import zipfile


def zip_file(file_path: str):
    zip_file_name = file_path.split("/")[-1].split(".")[0]
    with zipfile.ZipFile(f"{zip_file_name}.zip", "w") as zipf:
        zipf.write(file_path)


def unzip_file(file_path):
    destination_folder = file_path.split("/")[:-2]
    with zipfile.ZipFile(file_path, "r") as zipf:
        zipf.extractall("/".join(destination_folder))


if __name__ == "__main__":
    zip_file("test.txt")
