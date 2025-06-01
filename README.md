# langchain79

This repository contains Python scripts and experiments using the [Groq API](https://console.groq.com/) and various AI tools for language, image, and audio processing. The project demonstrates how to interact with Groq's LLMs, perform text-to-speech, analyze images, and fetch financial data using agents.

## Features

- **Language Models:** Query Groq LLMs for text generation and analysis.
- **Text-to-Speech:** Convert text to speech using Groq's TTS models.
- **Image Analysis:** Send images to LLMs for content description.
- **Financial Data:** Fetch and display financial data using agent tools.
- **Multi-Agent Orchestration:** Coordinate multiple agents for complex tasks.

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/DWARAKA1/langchain79.git
    cd langchain79
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv .venv
    .venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**
    - Create a `.env` file in the root directory with your Groq API key:
      ```
      GROQ_API_KEY=your_groq_api_key_here
      ```

## Usage

- **Run a script:**
    ```sh
    python app.py
    ```

- **Text-to-Speech:**
    ```sh
    python texttospeech.py
    ```

- **Image Analysis:**
    ```sh
    python image.py
    ```

- **Multi-Agent Example:**
    ```sh
    python multiagents.py
    ```

## Notes

- For some Groq models (like `playai-tts`), you must accept terms of use in the [Groq Console](https://console.groq.com/playground?model=playai-tts) before using them.
- Ensure your `.env` file is present and contains a valid API key.
- This project is for educational and demonstration purposes only. Do not use it for any malicious or unauthorized activities.

## License

This project is licensed under the MIT License.