import flask
## --------------------langchian---------------------------------------------
import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

urls=[
    "https://brainlox.com/courses/category/technical"
]

from langchain_community.document_loaders import UnstructuredURLLoader
loader=UnstructuredURLLoader(urls=urls)
data=loader.load()

from langchain.text_splitter import CharacterTextSplitter
text_splitter=CharacterTextSplitter(
    separator='\n',
    chunk_size=250,
)
docs=text_splitter.split_documents(data)

import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
embeddings=OpenAIEmbeddings()

vectorStore_openAI = FAISS.from_documents(docs, embeddings)

from langchain.chains.question_answering import load_qa_chain
from langchain import OpenAI

llm=OpenAI(temperature=0.5,model_name='gpt-3.5-turbo')

chain=load_qa_chain(llm,chain_type="stuff")

##---------------------------------------------------------------------------
app=flask.Flask(__name__)

@app.route('/ask',methods=['POST'])
def ask():
    data=flask.request.get_json()

    if('question' not in data):
        return flask.jsonify({'error': 'Missing question parameter'}), 400

    question = data['question']
    relevent_docs=vectorStore_openAI.similarity_search(question)
    answer=chain.run(input_documents=relevent_docs,question=question)
    print(answer)

    return flask.jsonify({'answer':answer})

if __name__=='__main__':
    app.run(debug=True)