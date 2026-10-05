from rag.factory import create_rag_application
from dotenv import load_dotenv
load_dotenv()

rag = create_rag_application()

rag.index(source="data",storage_path="../storage",index_name="my_index")

answer = rag.query(
    "do u know any moby?"
)

print(answer)