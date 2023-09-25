from filestack import Client

client = Client("AR6FAKdsgQQCMFgZ4gnjnz")
host = "http://localhost:8000/cdn/"

def upload_file(path):
    store_params = {
        "mimetype": "image/jpg"
    }
    new_filelink = client.upload(filepath=path,store_params=store_params)
    print(f"Get the link to acces you file using the following handle {new_filelink.handle}")

def get_file(handle):
    url = host + handle
    print(f"Access your file using the following link {url}")

handle = upload_file("image.jpg")

get_file(handle)