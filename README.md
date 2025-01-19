# **Legal Intake AI Backend Prototype**

## **Overview**

The **Legal Intake AI Backend Prototype** is a comprehensive backend system designed for automating and streamlining the intake process for legal services. It enables users to inquire about services, book appointments with lawyers, and interact via voice commands. The backend integrates various technologies including machine learning, NLP (Natural Language Processing), speech recognition, and text-to-speech to deliver accurate and responsive services.

This project includes the following features:
- **User inquiry handling** with responses from a pre-populated FAQ database or using a RAG (retrieval-augmented generation) pipeline for dynamic responses.
- **Appointment booking** system that stores user details and appointment information in MongoDB.
- **Voice interaction** capability for hands-free user engagement.
- **Email notifications** for appointment booking confirmations.

## **Features**

- **Inquiries**: Respond to user queries related to services, fees, lawyer availability, and more.
- **Appointment Booking**: Capture appointment details and send confirmation emails to users.
- **Voice Input/Output**: Allow users to interact with the system using voice commands, with text-to-speech responses.
- **Email Confirmation**: Send appointment confirmation emails using the Mailtrap service.

## **Technologies Used**

- **FastAPI**: A modern web framework for building APIs with Python.
- **MongoDB**: NoSQL database for storing FAQ data and appointment records.
- **RAG (Retrieval-Augmented Generation)**: Uses a combination of document retrieval and language models to generate accurate responses.
- **Llama 3.1 (8b)**: A language model for response generation.
- **Sentence Transformers**: Used for embedding and vectorizing the documents.
- **SKLearn VectorStore**: Stores document embeddings for retrieval.
- **Speech Recognition (speech_recognition)**: Converts user voice input into text.
- **pyttsx3**: Converts text to speech for voice output.
- **Mailtrap**: Simulates sending emails for testing the appointment confirmation feature.

## **System Architecture**

The backend consists of the following core components:
1. **API Layer**: FastAPI server handling HTTP requests for user interactions, voice inquiries, and appointment bookings.
2. **Database Layer**: MongoDB for storing FAQs and appointment records.
3. **AI Layer**: The RAG pipeline handles queries not found in the FAQ database by retrieving documents from a static webpage and generating responses using Llama 3.1.
4. **Speech Processing Layer**: Allows voice-based interactions using speech recognition for input and pyttsx3 for output.
5. **Email Layer**: Sends appointment confirmation emails to users.

## **Installation**

### Prerequisites
1. **Python 3.7+**
2. **MongoDB**: Set up a MongoDB instance or use MongoDB Atlas for cloud-based deployment.
3. **Mailtrap Account**: For simulating email sending.

### Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/legal-intake-ai-backend.git
   cd legal-intake-ai-backend
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   Create a `.env` file in the root of the project and add the following variables:
   ```bash
   MONGO_URI="mongodb://your-mongo-uri"
   MONGO_DB_NAME="your-db-name"
   EMAIL_SENDER="your-email@example.com"
   SMTP_SERVER_HOST="smtp.mailtrap.io"
   SMTP_SERVER_PORT=587
   SMTP_SERVER_LOGIN="your-mailtrap-login"
   SMTP_SERVER_PASSWORD="your-mailtrap-password"
   ```

4. **Run the Application**
   ```bash
   uvicorn main:app --reload
   ```
   This will start the FastAPI server locally at `http://127.0.0.1:8000`.

## **API Endpoints**

### **1. POST `/inquiry/`**
- **Description**: Respond to a user query.
- **Request**:
   ```json
   {
     "question": "What services do you offer?"
   }
   ```
- **Response**:
   ```json
   {
     "response": "Raffay Legal Services offers a wide range of legal expertise including business law, family law, criminal defense, and estate planning."
   }
   ```

### **2. GET `/voice-inquiry/`**
- **Description**: Listen to user voice input and provide a spoken response.
- **Response**:
   - The server listens for voice input and speaks back the response using text-to-speech.

### **3. POST `/book-appointment/`**
- **Description**: Book an appointment for a client.
- **Request**:
   ```json
   {
     "client_name": "John Doe",
     "date_time": "2025-01-20T10:00:00",
     "case_description": "Consultation on business law",
     "email": "john.doe@example.com",
     "lawyer_name": "Jane Smith",
     "lawyer_phone": "123-456-7890",
     "lawyer_email": "jane.smith@example.com"
   }
   ```
- **Response**:
   ```json
   {
     "message": "Appointment booked successfully!"
   }
   ```

## **Testing**

You can test the endpoints using tools like **Postman** or **cURL**. Ensure that MongoDB is running and the environment variables are properly configured.

---

## **Contribution**

Feel free to fork the repository, make changes, and submit pull requests. If you encounter any bugs or have suggestions for improvements, please create an issue on GitHub.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**

- **FastAPI**: For providing a fast and efficient framework for building APIs.
- **MongoDB**: For its easy-to-use, flexible NoSQL database.
- **Langchain**: For providing document loading, text splitting, and vector store functionalities.
- **SpeechRecognition and pyttsx3**: For enabling speech-to-text and text-to-speech functionalities.

---

This `README.md` provides a complete guide to the installation, usage, and API documentation for the **Legal Intake AI Backend Prototype**. Let me know if you need further assistance!