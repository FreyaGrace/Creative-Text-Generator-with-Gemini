# Philippine History and José Rizal Creative Text Generator
<br>Created and Coded by: Fatima Grace Apinan<br>
West Visayas State University<br>
BSCS-3B AI

# Project Overview
This Streamlit application generates creative text formats about Philippine history and José Rizal using Google API Key to help incoming students in learning and appreciating the rich history of the Philippines. Users can select a category related to Philippine history, choose a specific topic within that category, provide a prompt to guide the text generation, and generate creative text based on their input.


### Functionalities of the Project

1. **Multi-Level Prompting**: The application interacts with users through multiple levels of prompts, refining the creative direction at each level. Users progress through the prompts until reaching the final prompt.

2. **GPT-3 Integration**: OpenAI's GPT-3 API is utilized to generate creative text formats based on the user's prompts and choices. The generated text reflects the input provided by the user.

3. **User Interface**: The Streamlit interface guides users through the prompting process, allowing them to input prompts, make choices, and view the generated creative text. The interface is designed to be intuitive and user-friendly.

### Deliverables

- **Python Code**: Well-structured and documented Python code for the entire system.
- **Streamlit App**: A functional Streamlit application showcasing the multi-level prompting and GPT-3 integration.
- **Github Repository**: Upload your entire project code to a public Github repository.
  
## Project Setup for Users

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/FreyaGrace/Creative-Text-Generator-with-Gemini
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd Creative-Text-Generator-with-Gemini
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up OpenAI API Key:**

    - Sign up for an account on the google cloud platform and obtain your API key.
    - Set your API key as an environment variable and directly replace the placeholder in the `gemini.py` file.

## Features

- **Select Category**: Choose a category related to Philippine history from the dropdown menu.
- **Choose Specific Topic**: Select a specific topic within the chosen category.
- **Provide Prompt**: Describe the main idea or context in the text area provided.
- **Generate Text**: Click the "Generate Text" button to generate creative text based on your input.

## Usage Instructions

1. **Run the Streamlit App:**

    ```bash
    streamlit run app.py
    ```

2. **Use the Application:**

    - Select a category related to Philippine history from the dropdown menu.
    - Choose a specific topic within the chosen category.
    - Describe the main idea or context in the text area provided.
    - Click the "Generate Text" button to generate creative text based on your input.

## Contributors

- [Fatima Grace Apinan](https://github.com/FreyaGrace)
