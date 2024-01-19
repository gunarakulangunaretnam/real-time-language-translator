import streamlit as st
from googletrans import LANGUAGES, Translator

# Create a mapping between language names and language codes
language_mapping = {name: code for code, name in LANGUAGES.items()}

def get_language_code(language_name):
    return language_mapping.get(language_name, language_name)

def translate_text(text, source_language, target_language):
    translator = Translator()
    translated_text = translator.translate(text, src=source_language, dest=target_language).text
    return translated_text

# UI layout
st.title("Language Translator")

# Dropdowns for selecting languages
from_language_name = st.selectbox("From", list(LANGUAGES.values()))
to_language_name = st.selectbox("To", list(LANGUAGES.values()))

# Convert language names to language codes
from_language = get_language_code(from_language_name)
to_language = get_language_code(to_language_name)

# Button to trigger translation
if st.button("Start"):
    st.text("Translation in progress...")

    print(from_language)
    print(to_language)
    
    # Your translation logic here
    text_to_translate = "Hello, world!"  # Replace this with the actual text you want to translate
    translated_result = translate_text(text_to_translate, from_language, to_language)
    
    # Display the translated text
    st.text(f"Translated text from {from_language_name} to {to_language_name} ({from_language} to {to_language}):")
    st.text(translated_result)

# Display status
st.text("Status: Ready")
