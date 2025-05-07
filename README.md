# Real Estate Chatbot

A chatbot application that helps users find their ideal property in New York City by matching their requirements with available properties in the database.

## Features

- Property search based on user requirements
- Similarity matching between user requirements and available properties
- Interactive web interface using Gradio
- Vector database for efficient property search
- OpenAI integration for natural language processing

## Overview

The Real Estate Chatbot consists of two main components:

1. **Personalized Listing Generator**: A user-friendly interface with dropdowns and sliders to generate detailed house listings.
![Personalized Listing Generator Interface](https://github.com/apolanco3225/Real-State-ChatBot/assets/16232171/8c21faca-0140-401a-a3ef-a5029c416eaf)

2. **Property Matching Chatbot**: An interactive interface where users can:
   - Enter their property requirements
   - Get property suggestions based on similarity
   - Compare their requirements with suggested properties
![Property Matching Interface](https://github.com/apolanco3225/Real-State-ChatBot/assets/16232171/846cca5d-00f1-4763-a0a9-5dd0317779fb)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/apolanco3225/Real-State-ChatBot/tree/main
cd Real-State-ChatBot
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Running the Application

1. Start the application:
```bash
python src/app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://127.0.0.1:7860)

### Using the Chatbot

1. Enter your property requirements in the text box
2. Click "Generate Suggestion" to find the most similar property in the database
3. Click "Find Similarities" to see the common and uncommon items between your requirements and the suggested property

## Project Structure

```
Real-State-ChatBot/
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   └── ai_service.py
├── requirements.txt
├── README.md
└── .env
```

## Requirements

- Python 3.9+
- OpenAI API key
- Internet connection for API calls

## License

This project is licensed under the MIT License - see the LICENSE file for details.
