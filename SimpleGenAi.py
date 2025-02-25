import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ##LangSmith Tracking 
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# Instead of directly setting environment variables
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
langchain_project = os.getenv("LANGCHAIN_PROJECT")

if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
if langchain_project:
    os.environ["LANGCHAIN_PROJECT"] = langchain_project

os.environ["LANGCHAIN_TRACING_V2"] = "true"

##Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the question asked"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain Demo With LLAMA2")
input_text=st.text_input("What question you have in mind?")

##Call ollama llama2 model
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))


import subprocess
import time
import platform

def start_ollama():
    system = platform.system()
    if system == "Windows":
        # Windows
        subprocess.Popen(["ollama", "serve"], creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        # macOS/Linux
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Wait for Ollama to initialize
    time.sleep(5)