import random

from services.rag_service import query_rag


def process_query(query: str):

    query_lower = query.lower()

    # IT Support Ticket Creation

    issue_keywords = [
        "laptop",
        "wifi",
        "printer",
        "network",
        "vpn",
        "software",
        "email",
        "system"
    ]

    if any(word in query_lower for word in issue_keywords):

        return {
            "action": "ticket",
            "ticket_id": f"IT-{random.randint(1000,9999)}",
            "issue": query,
            "status": "Open"
        }

    # RAG Search

    answer = query_rag(query)

    if answer:

        return {
            "answer": answer
        }

    return {
        "answer":
        "Sorry, I could not find information related to your question. Please ask an HR or IT support related question."
    }