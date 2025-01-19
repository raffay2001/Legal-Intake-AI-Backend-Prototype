from pymongo import MongoClient
from .config import MONGO_URI, MONGO_DB_NAME

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME] 
appointments_collection = db.appointments  
faqs_collection = db.faqs

FAQs = {
    # 1st FAQ question
    "what services do you offer": "Raffay Legal Services offers a wide range of legal expertise to meet the diverse needs of our clients. Below is a detailed breakdown of our key service areas. Our first service is business law in which we provide support for business formation, contract drafting, mergers and acquisitions, regulatory compliance, intellectual property rights, and dispute resolution. Our attorneys are skilled in handling complex corporate legal issues to ensure your business thrives. Our second service is family law in which our compassionate family law attorneys assist with divorce proceedings, child custody agreements, adoption cases, prenuptial agreements, and spousal support. Our third service is criminal defense in which whether you are facing charges for theft, assault, fraud, or other criminal allegations, our seasoned criminal defense team provides aggressive representation to protect your interests and secure favorable outcomes. Our last and fourth service is estate planning in which we do from drafting wills and trusts to navigating probate, our estate planning services help you protect your legacy and ensure your loved ones are cared for according to your wishes.",

    # 2nd FAQ question
    "how much do the consultation cost": "We believe in transparent pricing to help you plan your legal journey effectively. Below are the consultation fees for our services: initial consultation of thirty minutes is for hundred dollars only whereas the detailed one hour legal advice session is for two hundred dollars only and finally the case review and strategy planning session is for three fifty dollars only and lastly any follow-up consultations will cost you one fifty dollars per hour",

    # 3rd FAQ question
    "when can I meet the lawyers": "You can meet the lawyers of Raffay Legal Services on Monday to Friday from ten A M to six P M. The available lawyers are John Doe, Jane Smith, and Michael Brown. Appointments are required to ensure availability, which can be booked by calling or using their online portal. The consultation fees for an initial meeting with one of the lawyers would be hundred dollars for a thirty minute session. Please note that the appointments should be scheduled in advance as walk-ins may not be accommodated."
}

def save_appointment(appointment):
    """Save an appointment to the database."""
    return appointments_collection.insert_one(appointment).inserted_id

def save_faqs():
    """Save FAQ data to MongoDB."""
    faq_docs = [{"question": question, "answer": answer} for question, answer in FAQs.items()]
    # Insert the FAQs into the collection
    faqs_collection.insert_many(faq_docs)
    print("FAQs saved to MongoDB.")