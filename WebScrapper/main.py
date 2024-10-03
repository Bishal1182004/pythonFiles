import streamlit as st
from scrape import scrape_website, split_dom_content, extract_body_content, clean_body_content
from parse import parse_with_gemini
import google.generativeai as genai
from parse_gemini import gemini_calling

st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

if st.button("Scrape Website"):
    st.write("Scraping the website...")

    try:
        result = scrape_website(url)
        if result:
            body_content = extract_body_content(result)
            cleaned_content = clean_body_content(body_content)

            st.session_state.dom_content = cleaned_content

            with st.expander("View DOM Content"):
                st.text_area("DOM Content", cleaned_content, height=300)
        else:
            st.error("Failed to scrape the website. Please check the URL or try again.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")
            try:
                dom_chunks = split_dom_content(st.session_state.dom_content)
                result = parse_with_gemini(dom_chunks, parse_description)
                st.write(result)
            except Exception as e:
                st.error(f"An error occurred during parsing: {str(e)}")
