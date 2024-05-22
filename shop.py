import numpy as np
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from llm_model_class import llm_model_class
from utils.utils import *
from utils.prompt_generate import *


class shop:

    def __init__(self, shop_name : str , shop_link : str ):
        self.shop_name = shop_name
        self.shop_link = shop_link
        self.scrap_data = scrape_and_clean(self.shop_link)


    def generate_chain(self , llm :llm_model_class , *args_fn, input : str = None ):

        input = self.scrap_data if input is None else input

        result = []
        for i in range(len(args_fn)):
            prompt = ChatPromptTemplate.from_messages([
                ("system", args_fn[i]),
                ("user", "{input}")
            ])
        
            chain = prompt | llm.llm | StrOutputParser() 
            x = chain.invoke({"input": input})
            result.append(x)
            
        return result
