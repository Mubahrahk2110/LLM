# Gemini Learning Assistant

A simple command-line learning assistant built with Python and the Google Gen AI SDK. It loads a Gemini API key from an environment file, sends your prompt to the model, and prints the response in the terminal.

The assistant is configured to explain concepts clearly and use examples when useful. It also declines to answer mathematics-related questions with:

```text
I am not able to answer questions related to mathematics.
```

## Features

- Interactive prompt entry from the terminal
- Gemini model responses through the Google Gen AI SDK
- System instructions for clear, simple explanations
- Automatic loading of environment variables with `python-dotenv`
- A restricted response behavior for mathematics questions

## Requirements

- Python 3.10 or newer
- A Google Gemini API key
- Internet access

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS or Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## API Key Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

You can obtain a Gemini API key from Google AI Studio. Never commit `.env` or share your API key publicly.

Before publishing this repository to GitHub, add the following entry to `.gitignore` if it is not already present:

```gitignore
.env
venv/
__pycache__/
*.py[cod]
```

## Usage

Run the assistant from the project root:

```bash
python main.py
```

Enter a prompt when asked:

```text
Enter your prompt: Explain photosynthesis simply
```

The generated response will be printed to the terminal.

## Project Structure

```text
.
├── main.py          # Application entry point and Gemini interaction
├── requirements.txt # Python dependencies
├── .env             # Local API key configuration; keep private
├── .vscode/
│   └── settings.json
└── venv/            # Local virtual environment
```

## How It Works

1. `python-dotenv` loads `GEMINI_API_KEY` from `.env`.
2. `google-genai` creates a Gemini client.
3. `main.py` asks the user to enter a prompt.
4. The prompt and system instructions are sent to the configured Gemini model.
5. The response's text output is printed to the terminal.

## Dependencies

The main project dependencies are:

- `google-genai`
- `python-dotenv`
- `requests`

The complete pinned dependency list is available in `requirements.txt`.

## Troubleshooting

### API key not recognized

- Confirm that `.env` exists in the project root.
- Confirm that the variable is named `GEMINI_API_KEY`.
- Restart the terminal or editor after adding or changing the key.

### Module not found

- Activate the virtual environment.
- Reinstall dependencies:

  ```bash
  python -m pip install -r requirements.txt
  ```

### Model or API error

- Verify that the API key is valid and active.
- Check that the configured model is available to your account.
- Confirm that the machine has internet access.

## License

No license file is currently included. Add a license before others use or distribute this project if you want to define reuse and redistribution terms.
