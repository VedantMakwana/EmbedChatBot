
# EmbedChatBot

Conversational AI Hub: Harnessing Hugging Face Models and FAISS for Dynamic Q&A

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

### Project Overview

**Purpose:** This project builds a Flask application integrating Hugging Face models and FAISS for conversational AI. It handles dynamic Q&A by retrieving and generating responses from a text corpus.

**Key Features:**
- **Conversational AI Endpoint:** API (`POST /conversation`) for real-time question answering.
- **FAISS Integration:** Efficient storage and retrieval of text embeddings for fast data querying.
- **Dynamic QA System:** Uses Hugging Face models to fetch and process relevant information based on user queries.
- **Scalable and Customizable:** Adaptable for diverse AI applications, enhancing user engagement and efficiency.

**Why Use or Contribute:**
- Enhances user interactions with responsive AI capabilities.
- Offers learning opportunities with cutting-edge AI technologies.
- Encourages community collaboration for innovation and improvement in conversational AI solutions.

### Installation Guide

#### Prerequisites

1. **Python**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Virtual Environment (optional but recommended)**: Set up a virtual environment to isolate your project dependencies. You can use `venv` (built-in) or `virtualenv`.

   ```bash
   # Create a virtual environment (optional but recommended)
   python -m venv venv
   # Activate the virtual environment (Windows)
   venv\Scripts\activate
   # Activate the virtual environment (Mac/Linux)
   source venv/bin/activate
   ```

#### Step-by-Step Installation

1. **Clone the Repository**: Clone the project repository from GitHub.

   ```bash
   git clone https://github.com/your_username/your_project.git
   cd your_project
   ```

2. **Install Dependencies**: Install required Python packages listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**: If your project uses environment variables (e.g., for API tokens or configuration), create a `.env` file in the root directory and define them. Example `.env` file:

   ```
   HUGGINGFACE_TOKEN="your_huggingface_token_here"
   ```

   Make sure to replace `"your_huggingface_token_here"` with your actual Hugging Face API token.

4. **Run the Application**: Start the Flask application.

   ```bash
   python app.py
   ```

5. **Access the Application**: Once the application is running, access it locally through your web browser or via API requests to `http://localhost:5000`.

### Additional Notes

- **Configurations**: Modify any additional configurations as needed in `app.py` or other relevant files.
- **Troubleshooting**: If encountering issues, check error messages in the console for guidance.

By following these steps, users should be able to successfully install and run your Flask application locally, utilizing its conversational AI capabilities powered by Hugging Face models and FAISS.

## API Endpoints

### API Endpoints Documentation

#### `POST /conversation`

- **Purpose**: Endpoint for real-time question answering using Hugging Face models and FAISS.
  
- **Expected Input**:
  - JSON payload containing a single field:
    ```json
    {
      "question": "What is your question?"
    }
    ```
    - `question`: String representing the user's query.
  
- **Response Format**:
  - JSON response containing a single field:
    ```json
    {
      "response": "Generated answer based on the question."
    }
    ```
    - `response`: String representing the AI-generated answer based on the input question.



#### Additional Notes:

- Ensure the Flask application (`app.py`) is running and accessible at `http://localhost:5000`.
- Adjust the endpoint URLs or configurations (`app.py`) as per your project's requirements.
- Handle errors gracefully and validate input data to enhance reliability and security.

This endpoint enables seamless integration of conversational AI capabilities into applications, facilitating dynamic interaction and information retrieval based on user queries.

- **POST /conversation**
  - Endpoint to handle incoming JSON requests containing a 'question' field. Responds with a JSON containing a 'response' field with the generated response.

Example request:
```json
{
  "question": "What is your question?"
}
```

Example response:
```json
{
  "response": "Generated answer based on the question."
}
```


Customize this template with specific details about your project, such as additional features, acknowledgments, or troubleshooting tips. Save this content in a file named `README.md` in the root directory of your project. This file will be automatically displayed on your GitHub repository's main page and will help others understand and use your project effectively.
