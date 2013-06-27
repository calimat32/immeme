import requests, json

def upload_to_imgur(image64):
    headers = {"Authorization": "Client-ID 1bc61a0a912b4fc"}
    url = "https://api.imgur.com/3/image"
    payload = {
                "image": image64,
                "type": "base64"
    }
    response = requests.post(url, data=payload, headers=headers)
    try:
        image_id = response.json()["data"]["id"]
        return image_id
    except KeyError:
        return "failed to upload"
