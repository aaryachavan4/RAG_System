import pdfplumber as pdfp
from sentence_transformers import SentenceTransformer
import psycopg

#Extracting the text
all_text= ''
file_name= "test_file.pdf"
with pdfp.open(file_name) as pdf:
    for pg in pdf.pages:
        all_text+= all_text+ pg.extract_text()

#chunking hte code into parts
def chunking_text(text,chunk_size=500, overlap=50):
    chunk=[]
    words= text.split()
    for i in range(0,len(words),chunk_size-overlap):
        c= " ".join(words[i:i+chunk_size])
        chunk.append(c)
        return chunk
    
chunk= chunking_text(all_text)

#embedding using the sentence transformer and inserting thingies into the database
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

with psycopg.connect("dbname=rag_db user=postgress") as conn:
    with conn.cursor() as cur:
    
        for i in range(0, len(chunk)):
            embedding= model.encode(chunk[i])
            cur.execute("INSERT INTO documents (pdf_source, chunk_no, chunk_text, embedded_vector) VALUES (%s,%s,%s, %s)",(file_name,i,chunk[i],embedding))
            conn.commit()


            
    
