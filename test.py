# from huggingface_hub import InferenceClient
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = InferenceClient(
#     api_key=os.getenv("HUGGINGFACE_API_KEY")
# )

# models = client.list_deployed_models()

# print(models)

from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HUGGINGFACE_API_KEY")
)

response = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Hello"
        }
    ]
)

print(response.choices[0].message.content)