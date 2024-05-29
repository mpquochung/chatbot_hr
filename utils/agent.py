import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from .query import query_cv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain

from utils.llm_api import get_llm
from utils.reasoning import get_reason_response
from utils.retransforming import retransform
from utils.embedding_search_pg import get_similarity_search_results
from cohere_aws import Client

#co = Client(region_name="us-east-1")
#co.connect_to_endpoint(endpoint_name="cohere-rerank-v3-endpoint")

def decide(input_text, memory):

    llm = get_llm(model = "anthropic.claude-3-haiku-20240307-v1:0", temperature=0)

    def _parse(text):
        return text.strip('"').strip("**")


    prompt = PromptTemplate(input_variables=['history', 'input'], 
                            template="""The below conversation is between a HR and an AI assistant.
                            Now the AI is to decide whether to start a tool finding for suitable applicant or not.
                            \nThe current conversation is: {history}
                            \nA HR is asking/saying:{input}. 
                            \nIf the HR do not require to find CVs or seeking for somebody new, AI simply decide "No".
                            In case the HR require to find somebody/CV then AI decide "Yes".
                            HR may require to find anotherone if the former query is not good, in this case AI decide "Yes".
                            If the HR want to discuss more about anyone that AI found in the current conversation, AI will decide "No".
                            The AI only simple answer "Yes" or "No" and nothing else.
                            AI:""")
    conversation_with_summary = ConversationChain( #create a chat client
        llm = llm,
        memory = memory, #with the summarization memory
        prompt = prompt,
    )
    chat_response = conversation_with_summary.invoke(input_text) #pass the user message and summary to the model
    return chat_response['response']


def get_memory(): #create memory for this chat session
    
    #ConversationSummaryBufferMemory requires an LLM for summarizing older messages
    llm = get_llm(model = "anthropic.claude-3-haiku-20240307-v1:0")
    
    memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=512) #Maintains a summary of previous messages
    
    return memory

def get_chat_response(input_text, memory, streaming_callback): #chat client function
    
    llm = get_llm(model = "anthropic.claude-3-haiku-20240307-v1:0",streaming_callback = streaming_callback)

    conversation_with_summary = ConversationChain( #create a chat client
        llm = llm,
        memory = memory, #with the summarization memory
    )
    chat_response = conversation_with_summary.invoke(input_text) #pass the user message and summary to the model
    return chat_response['response']

def execute_response(input_query, index, memory, streaming_callback):
    llm_decision = decide(input_text=input_query,memory=memory)

    if "no" in llm_decision.lower():
        response = get_chat_response(input_text = input_query, memory = memory, streaming_callback=streaming_callback)
        return response
    else:   
        retransformed_query = retransform(input_query, memory = memory)
        search_results = get_similarity_search_results(index=index, question = retransformed_query, top_k = 5)
        #rerank_results = co.rerank(documents=search_results, query=retransformed_query, rank_fields=['content'], top_n=5)
        #cv_ids = [result.document['cv'] for result in rerank_results]
        # if do not use rerank, use this line:
        cv_ids = [result['cv'] for result in search_results]
        cv_information = query_cv(cv_ids)
        response = get_reason_response(results = cv_information['data'], query = input_query, memory = memory, streaming_callback=streaming_callback)
        return response

if __name__ == "__main__":
    input_query = "CV này tệ quá, bạn tìm những người khác có được không?"
    