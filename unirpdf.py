import streamlit as st
import PyPDF2
from io import BytesIO

def merge_pdfs(pdfs):
    merged_pdf = BytesIO()
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdfs:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

    pdf_writer.write(merged_pdf)
    return merged_pdf

def main():
    st.title("Mesclar Arquivos PDF")
    
    uploaded_files = st.file_uploader("Escolha os arquivos PDF que deseja mesclar", type="pdf", accept_multiple_files=True)
    
    if uploaded_files:
        st.write("Arquivos selecionados:")
        for pdf_file in uploaded_files:
            st.write(pdf_file.name)
        
        if st.button("Mesclar Arquivos"):
            pdf_files = [pdf_file for pdf_file in uploaded_files]
            merged_pdf = merge_pdfs(pdf_files)
            st.write("Arquivos PDF foram mesclados com sucesso!")
            st.download_button("Baixar PDF Mesclado", data=merged_pdf, file_name="pdf_mesclado.pdf")

if __name__ == "__main__":
    main()

