from tempfile import NamedTemporaryFile
import os
import streamlit as st
from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.readers.file import PDFReader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="Chat with the PDF",
    page_icon="🦙",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

# Initialize chat messages history if not already present
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about your document!"}
    ]

# File uploader widget
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file:
    bytes_data = uploaded_file.read()
    with NamedTemporaryFile(delete=False) as tmp:
        tmp.write(bytes_data)
        with st.spinner("Indexing document..."):
            reader = PDFReader()
            docs = reader.load_data(tmp.name)
            llm = OpenAI(
                api_key=os.getenv("OPENAI_API_KEY"),
                base_url=os.getenv("OPENAI_API_BASE", "https://api.openai.com"),
                model="gpt-3.5-turbo",
                temperature=0.0,
                system_prompt="You are an expert on the content of the document, provide detailed answers to the questions. Use the document to support your answers.",
            )
            index = VectorStoreIndex.from_documents(docs)
    os.remove(tmp.name)  # Remove the temporary file after use

    # Initialize chat engine in session state
    st.session_state.chat_engine = index.as_chat_engine(
        chat_mode="condense_question", verbose=False, llm=llm
    )

# Chat input box
if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display previous chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Check if chat_engine is initialized and respond to the user's question
    if 'chat_engine' in st.session_state:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Assuming st.session_state.chat_engine.stream_chat(prompt) returns a response object
                    response = st.session_state.chat_engine.stream_chat(prompt)
                    # Assuming response.response_gen yields strings, concatenate them into a single paragraph
                    full_response = ' '.join(response.response_gen)
                    st.write(full_response)  # Display the concatenated response
                except Exception as e:
                    st.error(f"An error occurred: {e}")
else:
    # Inform the user to upload a document first
    with st.chat_message("assistant"):
        st.write("Please upload a document first to start the chat.")
