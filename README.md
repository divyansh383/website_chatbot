# Website Chatbot

Welcome to the documentation for the website chatbot powered by LangChain!

## Installation

To get started, make sure you have the required dependencies installed. You can install them using the following command:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_CHATBOT_NAME.git
cd YOUR_CHATBOT_NAME

# Install dependencies
pip install -r requirements.txt

# Run the Flask API
python app.py

# Posting Request
curl -X POST -H "Content-Type: application/json" -d '{"question": "YOUR_QUESTION_HERE"}' localhost:5000/ask



