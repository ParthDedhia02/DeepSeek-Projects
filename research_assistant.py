import streamlit as st
from openai import OpenAI
import PyPDF2
import docx

class ResearchAssistant:  
    def __init__(self):
        self.client=OpenAI(
            api_key="ollama",
            base_url="http://localhost:11434/v1",
        )
        self.model="deepseek-r1:1.5b"
    
    def extract_text(self, uploaded_file):
        if uploaded_file is None:
            return "No file uploaded."
        if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc=docx.Document(uploaded_file)
            for para in doc.paragraphs:
                text = para.text + "\n"
        elif uploaded_file.type == "application/pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        else:
            text=str(uploaded_file.read(), "utf-8")
        return text
    def analyze_content(self, text,query):
        prompt = f"""Analyze the following content and answer the question:\n\n{text}\n\nQuestion: {query}\n\nAnswer:
        TEXT:{text[:2000]}...
        QUERY:{query}
        PROVIDE :
        1.Direct answer to the question.
        2.Supporting Evidence
        3.Key findings
        4.Limitations of the analyis
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a research assistant.",
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                stream=True,
            )

            result=st.empty()
            collected_chunks=[]

            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    collected_chunks.append(chunk.choices[0].delta.content)
                    result.markdown(''.join(collected_chunks))
            
            return ''.join(collected_chunks)
        except Exception as e:
            return f"An error occurred: {str(e)}"
    
def main():
    st.set_page_config(page_title="Research Assistant", layout="wide")
    st.title("Research Document Analysis Assistant")
    assistant= ResearchAssistant()

    with st.sidebar:
        st.header("Upload Document")
        uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"],accept_multiple_files=True)

    if uploaded_file:
        st.write(f"{len(uploaded_file)} File uploaded successfully!")

        query = st.text_area("Enter your query:")

        if st.button("Analyze",type="primary"):
            with st.spinner("Analyzing..."):
                for file in uploaded_file:
                    st.write(f" Analysis of : {file.name}")
                    text = assistant.extract_text(file)
                    

                    tab1,tab2,tab3=st.tabs(["Main Analysis","key points","summary"])

                    with tab1:
                        result = assistant.analyze_content(text, query)
                        
                    with tab2:
                        assistant.analyze_content(text, "Extract Key points and findings")
                    
                    with tab3:
                        assistant.analyze_content(text, "Provide a brief summary of the document")
                if len(uploaded_file) > 1:
                    st.write("Cross document analysis.")
                    st.write("comparing findings across documents.")

if __name__ == "__main__":
    main()