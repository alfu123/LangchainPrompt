from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print(api_key)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0
)

response = llm.invoke("Who is the Prime Minister of India?")

print(response.content)


# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# models = genai.list_models()

# for model in models:
#     print(model.name)