# EduQuery AI - README

## Overview  
**EduQuery AI** is a human-language NLP chatbot designed to assist users in exploring and discovering the best courses available on Analytics Vidhya. Leveraging Retrieval-Augmented Generation (RAG) methodology and the Google Gemini model, EduQuery AI is capable of answering queries in a precise, optimized manner. The chatbot provides detailed yet concise responses to course-related questions, ensuring a user-friendly and highly informative experience.

---

## Features  
- **Natural Language Understanding:** Processes human-language queries with advanced NLP capabilities.  
- **RAG (Retrieval-Augmented Generation):** Combines retrieval-based information extraction with generative model responses for accurate results.  
- **Google Gemini Model:** Utilizes Google's cutting-edge Gemini model for embedding and response generation.  
- **Course Discovery:** Provides optimized searches for Analytics Vidhya courses, including descriptions, topics covered, and specializations.  
- **Safe and Responsible AI:** Ensures all responses are contextually relevant to courses in data science, machine learning, deep learning, NLP, CV, business analytics, robotics, and related fields.  
- **Custom Response Format:** Delivers results in a structured format for clarity:
  ```
  Here are related best searches for you:
  "Course Name" - Course description (100 words or fewer).
  ```

---

## How It Works  
1. **Input Query:** Users provide a question, such as "What are the best deep learning courses?"  
2. **Document Parsing:** The chatbot searches through pre-uploaded PDF files of course content.  
3. **Embedding Generation:** The text is embedded using the Google Gemini model for precise context matching.  
4. **Relevant Retrieval:** Retrieves the most relevant sections from the document using Chroma vector storage.  
5. **Response Generation:** Crafts an optimized response using the Gemini model in a user-friendly format.

---

## Components  
### 1. `gen_ai.py`  
Contains all backend implementations, including:  
- PDF document processing.  
- Embedding generation using the Google Gemini model.  
- Vector storage with Chroma.  
- Query handling and RAG-based response generation.

### 2. `app.py`  
The Streamlit-based frontend application:  
- Allows users to input their queries.  
- Displays the chatbot's generated responses.  
- Provides a clean and interactive user interface for seamless interaction.

---

## Installation  
### Prerequisites  
- Python 3.8 or later  
- Libraries: `streamlit`, `PyPDF2`, `chromadb`, `langchain`, `langchain-google-genai`, and other dependencies.  

### Steps  
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/eduquery-ai.git
   ```
2. Navigate to the project directory:
   ```bash
   cd eduquery-ai
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## Usage  
1. Upload the relevant course content PDF files to the `data/` directory.  
2. Launch the application by running the Streamlit app.  
3. Enter your question in the provided input field.  
4. View the optimized course suggestions in the structured format.  

---

## Example Queries  
- "What are the best NLP courses available?"  
- "Can you recommend robotics courses with detailed descriptions?"  
- "List data science courses for beginners."  

---

## Future Enhancements  
- Support for additional document types (e.g., Word, Excel).  
- Multi-language support for global users.  
- Enhanced visualization of course recommendations.  

---

## Contribution  
Feel free to contribute to the development of EduQuery AI. Fork the repository, make changes, and submit a pull request.  

---


---

**EduQuery AI - Empowering learners with knowledge at their fingertips.**
