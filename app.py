import os

from decouple import config
from fastapi import FastAPI
#from fastapi_key_auth import AuthorizerMiddleware
from langchain_groq import ChatGroq
from langserve import add_routes
from chain import get_refactor_chain

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')
os.environ['X_API_KEY'] = config('X_API_KEY')


model = ChatGroq(model='llama-3.3-70b-versatile')

app = FastAPI(
  title = "AI API",
  version='1.0',
  description='API for AI using Llama-3.3 70b'
)

# app.add_middleware(
#   middleware_class=AuthorizerMiddleware,
#   public_paths=('/docs','/redoc','/openapi.json'),
#   key_pattern ='X_API_KEY',
# )

add_routes(
  app,
  model,
  path='/chatbot')

add_routes(
  app,
  get_refactor_chain(),
  path='/translator'
)

if __name__ == '__main__':
  import uvicorn
  
  uvicorn.run(app, host='localhost', port=8000)