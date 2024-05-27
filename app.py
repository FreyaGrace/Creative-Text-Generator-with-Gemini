# app.py
import streamlit as st
from gemini import generate_text

def main():
    st.title("Philippine History and Rizal Creative Text Generator")
    st.write("Generate creative text formats about Philippine history and José Rizal with Gemini")

    category = st.selectbox("Choose a category:", ["José Rizal", "Philippine Revolution", "Spanish Colonization", "American Colonization", "World War II in the Philippines"])

    if category:
        specific_topic = st.selectbox(f"Choose a specific topic in {category}:", get_specific_topics(category))

        if specific_topic:
            prompt = st.text_area("Describe the main idea or context:")

            if st.button("Generate Text"):
                final_prompt = f"Write a detailed narrative about {specific_topic} in the context of {category}. {prompt}"
                generated_text = generate_text(final_prompt)
                st.write("### Generated Text")
                st.write(generated_text)

def get_specific_topics(category):
    topics = {
        "José Rizal": ["Life and Works", "Noli Me Tangere", "El Filibusterismo", "Martyrdom"],
        "Philippine Revolution": ["Katipunan", "Battle of Manila", "Cry of Pugad Lawin", "Aguinaldo's Leadership"],
        "Spanish Colonization": ["Galleon Trade", "Spanish Missions", "Colonial Government", "Propaganda Movement"],
        "American Colonization": ["Philippine-American War", "Commonwealth Era", "Japanese Occupation", "Independence"],
        "World War II in the Philippines": ["Bataan Death March", "Battle of Leyte Gulf", "Liberation of Manila", "Guerrilla Warfare"]
    }
    return topics.get(category, [])

if __name__ == "__main__":
    main()
