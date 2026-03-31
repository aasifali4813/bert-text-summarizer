import os
import streamlit as st
import requests

BACKEND_URL = os.getenv("BACKEND_URL", "https://bert-text-summarizer.onrender.com")

st.set_page_config(page_title="BERT Summarizer", page_icon="📝")
st.title("📝 BERT Text Summarizer")
st.markdown("Extracts the most important sentences from your text.")

text_input = st.text_area("Paste your text here", height=250)
num_sentences = st.slider("Number of sentences in summary", 1, 10, 5)

if st.button("Summarize", type="primary"):
    if text_input.strip():
        with st.spinner("Summarizing..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/summarize",
                    json={"text": text_input, "num_sentences": num_sentences}
                )
                if response.status_code == 200:
                    summary = response.json()["summary"]
                    st.success("Done!")
                    st.subheader("Summary")
                    st.write(summary)
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Cannot reach backend: {e}")
    else:
        st.warning("Please enter some text first.")
