# Deepseek Project

## Project Description

This repository contains a collection of AI assistants powered by the Deepseek language model via Ollama. The project provides multiple tools for coding assistance, document research, and text analysis through user-friendly Streamlit interfaces.

## Features

### Code Assistant

- **Code Generation**: Creates Python code based on user requirements
- **Code Explanation**: Provides detailed explanations of existing code
- **Code Review**: Analyzes code for improvements, bugs, and best practices

### Research Document Assistant

- **Document Analysis**: Extracts and analyzes text from PDF, DOCX, and TXT files
- **Query-based Research**: Answers specific questions based on document content
- **Key Points Extraction**: Identifies main findings and concepts from documents
- **Document Summarization**: Generates concise summaries of uploaded content
- **Cross-document Analysis**: Compares findings across multiple documents

### Basic Deepseek Implementation

- Simple implementation showing how to use the Deepseek model with the OpenAI API format

## Setup Instructions

### Prerequisites

- Python 3.6+
- Ollama installed and running locally (https://ollama.ai/)
- Deepseek model pulled in Ollama (`ollama pull deepseek-r1:1.5b`)

### Dependencies

- streamlit
- PyPDF2
- python-docx
- openai
- pandas

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/deepseek_project.git

# Navigate to the project directory
cd deepseek_project

# Install dependencies
pip install -r requirement.txt

# Make sure Ollama is running with Deepseek model
# If not already pulled, run:
ollama pull deepseek-r1:1.5b
```

## Usage

### Run the Code Assistant

```bash
streamlit run code_assitant.py
```

### Run the Research Document Assistant

```bash
streamlit run research_assistant.py
```

### Run the Basic Deepseek Example

```bash
python deepseek.py
```

## Project Structure

```
deepseek_project/
├── code_assitant.py      # Multi-tool AI assistant for code tasks
├── research_assistant.py # Document analysis and research tool
├── deepseek.py           # Basic implementation of Deepseek with Ollama
├── requirement.txt       # Project dependencies
└── README.md             # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## How It Works

This project leverages the Deepseek language model running locally through Ollama. The integration is done using the OpenAI API format, allowing for a familiar development experience while keeping all processing local.

The Streamlit interfaces provide an easy way to interact with the different AI assistants, making them accessible to users without requiring coding knowledge.

## Requirements

- Ollama must be running locally on the default port (11434)
- The Deepseek model (deepseek-r1:1.5b) must be pulled in Ollama
- Sufficient system resources to run the Deepseek language model
