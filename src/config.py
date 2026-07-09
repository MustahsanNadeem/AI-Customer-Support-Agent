from pathlib import Path

# =====================================================
# Project Root
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# =====================================================
# Data Paths
# =====================================================

DATA_DIR = PROJECT_ROOT / "data"

KNOWLEDGE_FILE = DATA_DIR / "customer_support_knowledge.txt"

TICKETS_FILE = DATA_DIR / "support_tickets.csv"


# =====================================================
# Vector Database
# =====================================================

VECTOR_DB_DIR = PROJECT_ROOT / "vector_db"


# =====================================================
# Text Splitter Settings
# =====================================================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200


# =====================================================
# Embedding Model
# =====================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"