import zipfile


def zip_file(file_path: str):
    zip_file_name = file_path.split("/")[-1]
    zip_file_path = file_path.split(zip_file_name)[0]
    zip_file_path = f"{zip_file_path}{zip_file_name.split('.')[0]}.zip"
    with zipfile.ZipFile(zip_file_path, "w") as zipf:
        zipf.write(file_path, arcname=zip_file_name)
    return zip_file_path


def unzip_file(file_path):
    destination_folder = "/".join(file_path.split("/")[:-1])
    with zipfile.ZipFile(file_path, "r") as zipf:
        file_name = zipf.namelist()[0]
        zipf.extractall(destination_folder)
    return f"{destination_folder}/{file_name}"


if __name__ == "__main__":
    zip_file("test.txt")
