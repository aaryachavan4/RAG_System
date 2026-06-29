# RAG_System

-> get the user input and then:
    pdf-> storage pipeline :|
    1. extracting the text form the pdf [pdfplumber]


DATABASE:
CREATE TABLE documents(id SERIAL PRIMARY KEY, pdf_source VARCHAR(255), chunk_no INT, chunk_text TEXT, embedded_vector vector(384), created_at TIMESTAMP DEFAULT NOW());
