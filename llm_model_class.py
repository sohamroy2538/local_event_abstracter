from langchain_anthropic import ChatAnthropic
from langchain_community.llms import Ollama
#from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv


load_dotenv()


class llm_model_class:
    def __init__(self, model_name : str):
        if(model_name == 'anthropic'):
            self.llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.2, max_tokens=2048, api_key = os.getenv('anthropic_key') )
        
        if(model_name == 'openai' ):
            self.llm = ChatOpenAI(api = "TODO")
        
        if(model_name == 'ollama'):
            # make sure llama 3 local server is running in cmd
            self.llm = Ollama(model="llama3")
