# dashboard/app.py

import streamlit as st
import requests

API_BASE = st.secrets.get("API_BASE", "http://localhost:8000/api")


st.set_page_config(page_title="Document Intelligence Dashboard", layout="wide")

st.title("Document Intelligence Dashboard")


tab1, tab2, tab3 = st.tabs(["Ingest", "Search", "Extract"])


# -----------------------------
# Ingest
# -----------------------------
with tab1:
    st.header("Upload Document")

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        if st.button("Ingest"):
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}

            response = requests.post(f"{API_BASE}/ingest", files=files)

            if response.status_code == 200:
                st.success("Ingestion started/completed")
                st.json(response.json())
            else:
                st.error(response.text)


# -----------------------------
# Search
# -----------------------------
with tab2:
    st.header("Semantic Search")

    query = st.text_input("Enter search query")

    if st.button("Search"):
        payload = {"query": query}

        response = requests.post(f"{API_BASE}/search", params=payload)

        if response.status_code == 200:
            st.subheader("Results")
            st.json(response.json())
        else:
            st.error(response.text)


# -----------------------------
# Extract
# -----------------------------
with tab3:
    st.header("Entity Extraction")

    document_id = st.text_input("Document ID")

    if st.button("Extract"):
        payload = {"document_id": document_id}

        response = requests.post(f"{API_BASE}/extract", params=payload)

        if response.status_code == 200:
            st.subheader("Extraction Result")
            st.json(response.json())
        else:
            st.error(response.text)