
# 📝 Cover Letter Generator

A streamlined **Cover Letter Generator** that scrapes job descriptions from URLs and creates personalized cover letters tailored to job postings. This project leverages powerful AI models for NLP tasks, including job posting extraction and cover letter generation, helping you easily craft professional cover letters for job applications.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

The **Cover Letter Generator** is designed to help job seekers automate the process of writing tailored cover letters. By providing a URL of a job posting, the app scrapes the job description, identifies key details like skills and requirements, and uses an AI language model to draft a personalized cover letter. The system also integrates a portfolio matching system to include relevant project links.

---

## Features

- 🌐 **URL Scraping**: Input any job posting URL, and the app scrapes the relevant content for further processing.
- 🔍 **AI-Based Job Analysis**: Automatically extracts important details from job descriptions such as role, experience, skills, and job descriptions.
- ✉️ **Personalized Cover Letters**: Generates customized cover letters tailored to the job posting and includes relevant projects from your portfolio.
- 🧑‍💼 **Portfolio Integration**: Matches job-required skills with your portfolio and inserts relevant project links in the cover letter.
- 🚀 **Easy to Use**: An intuitive interface built with Streamlit for an easy and smooth user experience.

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, LangChain, ChromaDB, pandas
- **AI Model**: LangChain's integration with large language models (LLMs)
- **Environment Management**: Anaconda
- **Scraping**: LangChain's `WebBaseLoader`
- **Vector Database**: ChromaDB for skill-to-project matching

---

## Installation

### Prerequisites

- Python 3.9+
- Anaconda (for environment management)
- A `.env` file containing your **Groq API Key** (`groq_api_key`)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/cover-letter-generator.git
    cd cover-letter-generator
    ```

2. **Set up the virtual environment**:
    - If using Anaconda:
      ```bash
      conda create --name cover_letter_generator python=3.9
      conda activate cover_letter_generator
      ```

3. **Set up your `.env` file**:
    - Create a `.env` file in the root directory of the project:
      ```bash
      touch .env
      ```
    - Add your Groq API Key to the `.env` file:
      ```
      groq_api_key='your_api_key_here'
      ```

4. **Run the Streamlit app**:
    ```bash
    streamlit run app/main.py
    ```

---

## Usage

1. **Enter the URL**: Input the job posting URL (for example, from LinkedIn, Amazon, etc.).
2. **Submit**: Click on the "Submit" button to scrape the job posting.
3. **Generate the Cover Letter**: The app extracts the job details and generates a tailored cover letter using the AI model, including relevant projects from your portfolio.
4. **View the Cover Letter**: The generated cover letter will appear on the screen in markdown format.

---

## Project Structure

```
cover-letter-generator/
│
├── app/
│   ├── main.py              # Main Streamlit app
│   ├── chains.py            # Handles LLM chains and prompts
│   ├── portfolio.py         # Portfolio handling and project matching
│   └── resource/
│       └── my_portfolio.csv  # CSV file with portfolio data (tech stack and links)
│
├── utils.py                 # Helper functions, e.g., text cleaning
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not in the repo, needs to be created)
└── README.md                # Project documentation
```

---

## Contributing

Contributions are welcome! If you'd like to improve the project or fix any issues, please follow the steps below:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Special thanks to all the open-source libraries and tools that made this project possible!

---

### 🛠️ Happy Coding & Job Hunting! 🎯

---

You can modify this template further to suit your project needs, especially the Acknowledgments or Contributing sections if you have specific guidelines for contributors.
