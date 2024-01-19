import streamlit as st
from googletrans import LANGUAGES, Translator

def translate_text(text, source_language, target_language):
    translator = Translator()
    translated_text = translator.translate(text, src=source_language, dest=target_language).text
    return translated_text

# UI layout
st.title("Language Translator")

# Dropdowns for selecting languages
from_language = st.selectbox("From", list(LANGUAGES.values()))
to_language = st.selectbox("To", list(LANGUAGES.values()))

# Button to trigger translation
if st.button("Start"):
    st.text("Translation in progress...")
    
    # Your translation logic here
    text_to_translate = "Hello, world!"  # Replace this with the actual text you want to translate
    translated_result = translate_text(text_to_translate, from_language, to_language)
    
    # Display the translated text
    st.text(f"Translated text from {from_language} to {to_language}:")
    st.text(translated_result)

# Display status
st.text("Status: Ready")
