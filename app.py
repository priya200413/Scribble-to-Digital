import streamlit as st
from PIL import Image
from utils.ocr_processor import extract_text
from utils.ai_processor import process_notes
from utils.file_export import export_txt, export_pdf, export_docx

st.title("✍️ Scribble to Digital")
st.write("Convert handwritten notes into clean digital text using OCR and AI")

uploaded_file = st.file_uploader("Upload handwritten image", type=["png","jpg","jpeg"])

if uploaded_file:

    image = Image.open(uploaded_file)

    st.subheader("Uploaded Image")
    st.image(image)

    if st.button("Process Notes"):

        with st.spinner("Processing..."):

            raw_text, enhanced = extract_text(image)

            st.subheader("Enhanced Image")
            st.image(enhanced)

            st.subheader("Raw OCR Text")
            st.text_area("", raw_text, height=150)

            ai_result = process_notes(raw_text)

            st.subheader("AI Corrected Notes & Tasks")
            st.text_area("", ai_result, height=300)

            txt_file = export_txt(ai_result)
            pdf_file = export_pdf(ai_result)
            docx_file = export_docx(ai_result)

            st.download_button(
                "Download TXT",
                txt_file,
                file_name="notes.txt"
            )

            st.download_button(
                "Download PDF",
                pdf_file,
                file_name="notes.pdf"
            )

            st.download_button(
                "Download DOCX",
                docx_file,
                file_name="notes.docx"
            )