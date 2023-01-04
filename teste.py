import openai
from PIL import Image
import requests
from requests.structures import CaseInsensitiveDict
import io
import json

QUERY_URL = "https://api.openai.com/v1/images/generations"

def generate_images(prompt, model, api_key):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {api_key}"
    
    data = """
    {
        """
    data += f'"model": "{model}",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":1,
        "size":"256x256",
        "response_format":"url"
    }
    """

    resp = requests.post(QUERY_URL, headers=headers, data=data)

    print(f"Status code: {resp.status_code}")
    print(f"Response text: {resp.text}")

    if resp.status_code != 200:
        raise ValueError("Failed to generate image")

    response_text = json.loads(resp.text)
    return response_text['data'][0]['url']

prompt = "anime draw of a cat chasing mouse"
model = "image-alpha-001"
openai.api_key = "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"

# Gerar imagem usando o DALL-E
image_url = generate_images(prompt, model, openai.api_key)

# Fazer download da imagem
response = requests.get(image_url)

# Carregar imagem em um objeto de imagem
image = Image.open(io.BytesIO(response.content))

# Salvar imagem em um arquivo .png
image.save("image1.png")


#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
