from .rag import rag_application
from .db import faqs_collection

def get_response(question):
    """Generate a response to a question by checking MongoDB FAQs or using the RAG pipeline."""
    print(f"The question is: \n{question}")
    # Check FAQs in MongoDB
    faq_doc = faqs_collection.find_one({"question": question})
    if faq_doc:
        print(f"::Answering from the MongoDB FAQ database::")
        faq_response = faq_doc["answer"]
        print(f"::The MongoDB FAQ response is: \n{faq_response}")
        return faq_response
    # If not in FAQs, use the RAG pipeline
    print(f"::Answering from the RAG pipeline::")
    rag_response = rag_application.run(question)
    print(f"::The RAG pipeline response is: \n{rag_response}")
    return rag_response