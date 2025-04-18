import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Software Architecture Workbench")

st.markdown("This tool takes high-level user requirements and generates a software architecture design using AI.")


user_input = st.text_area("Enter high-level user requirements:")

if st.button("Generate Architecture"):
    if user_input:
        with st.spinner("Generating architecture..."):
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a software architect."},
                    {"role": "user", "content": f"Given this requirement: {user_input}, extract functional and non-functional requirements, suggest architecture components, architecture style, justification, and generate a Mermaid diagram of the architecture."}
                ]
            )

            st.markdown("### Architecture Design")
            st.markdown(response.choices[0].message.content)

            st.markdown("[View & Export Diagram at Mermaid Live](https://mermaid.live)", unsafe_allow_html=True)
                
    else:
        st.warning("Please enter some requirements.")
