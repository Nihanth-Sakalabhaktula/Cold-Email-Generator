# AI Cold Email Generator

An AI-powered desktop application that analyzes job descriptions, identifies relevant skills, retrieves matching portfolio projects, and generates personalized professional cold emails for job applications.

## Features

- Paste any job description into the desktop application
- Extracts role, experience, and required skills using an LLM
- Matches relevant portfolio projects using ChromaDB semantic search
- Generates personalized job application cold emails
- Uses candidate information and verified project data to reduce hallucinations
- Displays matched projects with their tech stacks and GitHub links
- Copy generated emails directly to the clipboard
- Clear the application with one click
- Clean desktop GUI built using PySide6

## Tech Stack

- Python
- PySide6
- LangChain
- Groq API
- ChromaDB
- Pandas
- python-dotenv

## How It Works

1. The user pastes a job description into the application.
2. The LLM extracts the job role, required experience, skills, and description.
3. ChromaDB performs semantic retrieval to find relevant portfolio projects.
4. Retrieved project information and the candidate profile are provided as context to the LLM.
5. The application generates a concise and personalized cold email.
6. The generated email can be copied directly from the GUI.

## Project Structure

```text
Cold-Email-Generator/
│
├── candidate_profile.py
├── email_generator.py
├── gui.py
├── job_parser.py
├── main.py
├── portfolio.py
├── portfolio.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Nihanth-Sakalabhaktula/Cold-Email-Generator.git
cd Cold-Email-Generator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Never commit your `.env` file or API key to GitHub.

## Run the Application

```bash
python gui.py
```

## Example Workflow

Paste a job description into the Job Description section and click **Generate Cold Email**.

The application will display:

- Job Analysis
- Matched Portfolio Projects
- Generated Cold Email

The generated email can then be copied using the **Copy Email** button.

## Project Highlights

This project demonstrates practical implementation of:

- Large Language Models
- Prompt Engineering
- Retrieval-Augmented Generation
- Semantic Search
- Job Description Parsing
- Grounded AI Generation
- Desktop GUI Development
- Environment Variable Management

## Author

**Nihanth Sakalabhaktula**

GitHub: https://github.com/Nihanth-Sakalabhaktula