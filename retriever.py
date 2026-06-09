import chromadb
from chromadb.utils import embedding_functions
from config import CHROMA_COLLECTION, CHROMA_PATH, EMBEDDING_MODEL, N_RESULTS


_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)

_client = chromadb.PersistentClient(path=CHROMA_PATH)

_collection = _client.get_or_create_collection(
    name=CHROMA_COLLECTION,
    embedding_function=_ef,
    metadata={"hnsw:space": "cosine"},
)


def get_collection():
    """Return the ChromaDB collection. Used by app.py during ingestion."""
    return _collection


def embed_and_store(chunks):
    """
    Embed a list of document chunks and store them in the vector database.

    This function is already implemented — read through it before moving on.

    _collection.add() takes three parallel lists built from the chunks
    returned by chunk_document():

    - documents : raw text strings. ChromaDB's embedding function converts
                    these into vector embeddings automatically using
                    sentence-transformers.

    - metadatas : one dictionary per chunk, stored alongside the vector
                    so that retrieve() can surface which NCCU resource
                    (Student Handbook, Academic Calendar, Scholarships, etc.)
                    a result came from.

    - ids       : unique chunk_id strings used to identify each chunk
                    in the vector database.

    You do not generate embeddings manually here — you pass the text
    chunks to ChromaDB, and the embedding function handles the vector
    creation automatically.
    """
    _collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[
            {
                "source": c.get("source", c.get("game", "Unknown Source")),
                "filename": c.get("filename", "Unknown File"),
            }
            for c in chunks
        ],
        ids=[c["chunk_id"] for c in chunks],
    )

    print(f"Stored {_collection.count()} total chunks in the vector database.")


def retrieve(query, n_results=N_RESULTS):
    """
    Retrieve the most relevant NCCU document chunks for a user question.
    """
    if _collection.count() == 0:
        return []

    results = _collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    matches = []

    for doc, metadata, distance in zip(documents, metadatas, distances):
        matches.append(
            {
                "text": doc,
                "source": metadata.get("source", "Unknown Source"),
                "filename": metadata.get("filename", "Unknown File"),
                "distance": distance,
            }
        )

    return matches