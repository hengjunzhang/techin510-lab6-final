Lab 6 - Chat with PDF
This project allows users to interact with a chatbot that can understand and respond to queries based on the content of a uploaded PDF document. It utilizes Streamlit for the web interface, the OpenAI API for processing natural language queries, and a custom PDF processing mechanism to extract text from documents.

Getting Started
Follow these instructions to get the project up and running on your local machine for development and testing purposes.

Prerequisites
Before you start, ensure you have Python installed on your system. This project was developed with Python 3.8+, but it should be compatible with newer versions.

Installation
Create a Virtual Environment: This isolates your project dependencies from other Python projects.

bash
Copy code
python -m venv venv
Activate the Virtual Environment: The command differs slightly between operating systems.

On macOS and Linux:

bash
Copy code
source venv/bin/activate
On Windows:

bash
Copy code
.\venv\Scripts\activate
Install Dependencies: This installs the project's required libraries.

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables: Copy the sample environment variables and then modify them to fit your configuration.

bash
Copy code
cp .env.sample .env
After copying, open the .env file and replace the placeholders with your actual OpenAI API key and other necessary configurations.

Run the Application: Start the Streamlit application. Ensure your virtual environment is activated.

bash
Copy code
streamlit run app.py
Usage
After starting the application, navigate to the URL displayed in your terminal. Typically, Streamlit runs on http://localhost:8501.

Upload a PDF: Use the file uploader to select a PDF document.
Ask Questions: Type your questions into the chat input box. The application will provide answers based on the content of the uploaded PDF.
Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License - see the LICENSE file for details.
