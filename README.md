# Nikola Tesla: Back To Life

This repository provides a lightweight command-line chatbot that emulates
Nikola Tesla using [LangChain](https://python.langchain.com/) and
Google's Gemini models. You can ask about his inventions, ideas, and
legacy, and the assistant will reply in Tesla's voice.

<img></img>
![Nikola Tesla!](images/nikola.jpg)


## Requirements

- Python 3.10 or later
- A Google Generative AI API key with access to Gemini models

## Installation

1. (Optional) Create and activate a virtual environment.
2. Install the Python dependencies:
   ```bash
   cd src
   pip install -r requirements.txt
   ```
3. Configure your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and add your GOOGLE_API_KEY
   ```

## Usage

Run the chatbot from the `src` directory:

```bash
python chat.py
```

You will be greeted with an interactive prompt. Type your questions and
press enter to hear Tesla's response. Type `exit` or `quit` (or press
`Ctrl+C`) to stop the conversation.

## Environment Variables

| Variable             | Description                                                |
|----------------------|------------------------------------------------------------|
| `GOOGLE_API_KEY`     | Required. Your Google Generative AI API key.               |
| `GEMINI_MODEL`       | Optional. Gemini model name to use (defaults to `gemini-1.5-flash-latest`). |
| `GEMINI_TEMPERATURE` | Optional. Sampling temperature for the model (defaults 0.7)|

# Nicola_Tesla_Back_To_Life
