import os
from PyPDF2 import PdfReader

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


# =====================================================
# Embedding Model
# =====================================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =====================================================
# Paths
# =====================================================

VECTOR_STORE_PATH = "faiss_index"
MEMORY_STORE_PATH = "memory_index"

# =====================================================
# Vector Store
# =====================================================

def get_vector_store():

    if os.path.exists(f"{VECTOR_STORE_PATH}/index.faiss"):

        return FAISS.load_local(
            VECTOR_STORE_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

    # Empty Knowledge Base
    return FAISS.from_texts(
        ["Knowledge Base Initialized"],
        embeddings
    )


# =====================================================
# Memory Store
# =====================================================

def get_memory_store():

    if os.path.exists(f"{MEMORY_STORE_PATH}/index.faiss"):

        return FAISS.load_local(
            MEMORY_STORE_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

    return FAISS.from_texts(
        ["Memory Initialized"],
        embeddings
    )


# =====================================================
# Load Stores
# =====================================================

vector_store = get_vector_store()
memory_store = get_memory_store()

# =====================================================
# Process Uploaded Documents
# =====================================================

def process_document(
    file_path: str,
    filename: str
):

    text = ""

    # PDF
    if filename.lower().endswith(".pdf"):

        reader = PdfReader(file_path)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    # TXT
    else:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()

    if not text.strip():
        return False

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_text(text)

    global vector_store

    vector_store.add_texts(chunks)

    vector_store.save_local(
        VECTOR_STORE_PATH
    )

    return True


# =====================================================
# Self Learning
# =====================================================

def add_to_memory(
    question: str,
    answer: str
):

    global memory_store

    memory_store.add_texts([
        f"Q: {question}\nA: {answer}"
    ])

    memory_store.save_local(
        MEMORY_STORE_PATH
    )


# =====================================================
# Search Memory
# =====================================================

def search_memory(query):

    docs = memory_store.similarity_search(
        query,
        k=3
    )

    for doc in docs:

        content = doc.page_content

        if "A:" in content:

            return content.split(
                "A:"
            )[-1].strip()

    return None


# =====================================================
# Search Documents
# =====================================================

def search_documents(query):

    results = vector_store.similarity_search_with_score(
        query,
        k=3
    )

    if not results:
        return None

    matched_docs = []

    for doc, score in results:

        # Lower score = better match
        if score < 5.0:

            matched_docs.append(
                doc.page_content
            )

    if not matched_docs:
        return None

    return "\n\n".join(
        matched_docs
    )


# =====================================================
# Main Query Function
# =====================================================

def query_rag(query):

    query_lower = query.lower()

    # =================================================
    # MEMORY FIRST
    # =================================================

    memory_answer = search_memory(query)

    if memory_answer:
        return memory_answer

    # =================================================
    # GREETINGS
    # =================================================

    if query_lower in ["hello", "hi", "hey"]:
        return (
            "Hello! I am your AI HR Support Agent. "
            "I can answer HR policy questions and create IT support tickets."
        )

    # =================================================
    # TOTAL LEAVES
    # =================================================

    if (
        "how many leaves" in query_lower
        or "total leaves" in query_lower
    ):

        return """
Employee Leave Summary

• 12 Paid Sick Leaves
• 18 Earned Leaves
• 10 Casual Leaves

Total: 40 leaves per year.
"""

    # =================================================
    # LEAVE POLICY
    # =================================================

    if "leave policy" in query_lower:

        return """
Employee Leave Policy

• 12 Paid Sick Leaves per year
• 18 Earned Leaves per year
• 10 Casual Leaves per year

Total: 40 leaves per year.

Leave Guidelines:

• Sick leave may be used for illness or medical emergencies.
• Medical certificates may be required for extended absence.
• Earned leave requires manager approval.
• Unused earned leaves may be carried forward according to company policy.
"""

    if "sick leave" in query_lower:
        return "Employees are entitled to 12 paid sick leaves per year."

    if (
        "carry forward" in query_lower
        or "unused leave" in query_lower
        or "unused earned" in query_lower
    ):
        return (
            "Unused earned leaves may be carried forward according "
            "to company policy."
        )

    if "earned leave" in query_lower:
        return "Employees receive 18 earned leaves per year."

    if "casual leave" in query_lower:
        return "Employees receive 10 casual leaves per year."

    # =================================================
    # WORK FROM HOME
    # =================================================

    if (
        "work from home" in query_lower
        or "wfh" in query_lower
        or "remote work" in query_lower
        or "work remotely" in query_lower
    ):

        return """
Work From Home Policy

• Employees may work from home up to 2 days per week.
• Manager approval is required.
• Employees must remain available during office hours.
• Work deliverables and productivity standards remain unchanged.
"""

    # =================================================
    # NOTICE PERIOD
    # =================================================

    if "notice period" in query_lower:

        if (
            "reduce" in query_lower
            or "reduced" in query_lower
            or "shorten" in query_lower
        ):
            return (
                "The notice period may be reduced with management approval."
            )

        return """
Notice Period Policy

• Standard notice period: 60 days
• Employees must complete knowledge transfer activities.
• Reduction of notice period may be approved by management.
"""

    # =================================================
    # OFFICE HOURS
    # =================================================

    if (
        "office timing" in query_lower
        or "office timings" in query_lower
        or "office hours" in query_lower
        or "working hours" in query_lower
    ):
        return (
            "Office timings are Monday to Friday, "
            "9:00 AM to 6:00 PM."
        )

    # =================================================
    # TRAVEL REIMBURSEMENT
    # =================================================

    if (
        "travel" in query_lower
        or "reimbursement" in query_lower
        or "expense" in query_lower
        or "claim" in query_lower
    ):

        return """
Travel Reimbursement Policy

• Employees may claim approved business travel expenses.
• Maximum reimbursement: ₹5000 per month.
• Valid bills and receipts are required.
• Claims should be submitted within the reimbursement period.
"""

    # =================================================
    # BENEFITS
    # =================================================

    if (
        "benefit" in query_lower
        or "insurance" in query_lower
        or "bonus" in query_lower
        or "provident fund" in query_lower
        or "pf" in query_lower
    ):

        return """
Employee Benefits

• Health Insurance Coverage
• Annual Performance Bonus
• Provident Fund Contributions
• Employee Assistance Program
• Professional Training and Development
• Flexible Working Options
• Paid Public Holidays
"""

    # =================================================
    # DOCUMENT SEARCH
    # =================================================

    document_answer = search_documents(query)

    if document_answer:
        return document_answer[:800]

    # =================================================
    # NOT FOUND
    # =================================================

    return None

# =====================================================
# Stats
# =====================================================

def get_stats():

    return {
        "knowledge_base_documents":
        vector_store.index.ntotal,

        "memory_entries":
        memory_store.index.ntotal
    }