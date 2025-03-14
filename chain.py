import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


GROQ_API_KEY = os.environ.get("GROQ_API_KEY")


def get_refactor_chain():
  model = ChatGroq(
    model='llama-3.3-70b-versatile'
    )
  refactor_prompt = ChatPromptTemplate.from_template(
    'Refactor this python code to be more pythonic: {text}'
  )
  refactor_chain = refactor_prompt | model | StrOutputParser()
  return refactor_chain