from streamlit import title, sidebar, text_input, button, write, success, error
from streamlit import cache
from streamlit import SessionState
from streamlit import st
from langchain_community.chat_models.ollama import ChatOllama

from crewai import Agent
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI


class LLMS:
    ollama_llama3 = lambda **kwargs: Ollama(model="llama3", **kwargs)
    ollama_chat_llama3 = lambda **kwargs: ChatOllama(model="llama3", **kwargs)
    ollama_openhermes = lambda **kwargs: Ollama(model="openhermes", **kwargs)
    ollama_chat_openhermes = lambda **kwargs: ChatOllama(model="openhermes", **kwargs)
    openai_gpt_4o = lambda **kwargs: ChatOpenAI(model="gpt-4o", **kwargs)
    openai_gpt_3 = lambda **kwargs: ChatOpenAI(model="gpt-3.5-turbo", **kwargs)


class Llama3Agent(Agent):
    def __init__(self, goal: str, backstory: str, role: str, **kwargs):
        super().__init__(
            goal=goal,
            backstory=backstory,
            role=role,
            system_template="<|start_header_id|>system<|end_header_id|>\n\n{{ .System }}<|eot_id|>",
            prompt_template="<|start_header_id|>user<|end_header_id|>\n\n{{ .Prompt }}<|eot_id|>",
            response_template="<|start_header_id|>assistant<|end_header_id|>\n\n{{ .Response }}<|eot_id|>",
            llm=LLMS.ollama_openhermes(),
            allow_delegation=kwargs.pop("allow_delegation", False),
            **kwargs,
        ),
