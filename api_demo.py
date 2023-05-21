from flask import Flask, request, jsonify
from configs.model_config import *
from chains.local_doc_qa import LocalDocQA
import os
import nltk

nltk.data.path = [NLTK_DATA_PATH] + nltk.data.path

app = Flask(__name__)

@app.route('/llm_search', methods=['POST'])
def process_text():
    text = request.json['text']
    
    vs_path = './vector_store/Supplementary knowledge base 3_FAISS_20230521_235442'
    history = []
    
    query = str(text)
    last_print_len = 0
    for resp, history in local_doc_qa.get_knowledge_based_answer(query=query,
                                                                 vs_path=vs_path,
                                                                 chat_history=history,
                                                                 streaming=False):
        results = resp["result"]
        
    return jsonify({'response': results})  # 返回处理结果

if __name__ == '__main__':
    local_doc_qa = LocalDocQA()
    local_doc_qa.init_cfg(llm_model=LLM_MODEL,
                          embedding_model=EMBEDDING_MODEL,
                          embedding_device=EMBEDDING_DEVICE,
                          llm_history_len=LLM_HISTORY_LEN,
                          top_k=VECTOR_SEARCH_TOP_K)
    
    app.run(host='127.0.0.1', port=5000)