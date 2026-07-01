from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
import os

load_dotenv()
# embeddings = HuggingFaceEmbeddings()
llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct", huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"))
chat = ChatHuggingFace(llm=llm)
print(os.getenv("HUGGINGFACE_API_KEY"))
while True:
    query = input("Enter your query (or type 'exit' to quit): ")
    if query.lower() == 'exit':
        break

    # Generate embeddings for the query
    response = chat.invoke(query)
    
    # Here you would typically compare the query_embedding with your stored embeddings
    # and retrieve relevant information. For demonstration, we'll just print the embedding.
    
    print("Query Embedding:", response)