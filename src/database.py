from langchain.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from .config import DATABASE_PATH

class VectorDatabase:
    def __init__(self):
        self.embeddings_generator = OpenAIEmbeddings()
        self.vector_database = Chroma(
            persist_directory=DATABASE_PATH,
            embedding_function=self.embeddings_generator
        )
    
    def generate_suggestions(self, input_user_query: str, k: int = 1) -> str:
        """
        Generate suggestions based on user query using vector similarity search.
        
        Args:
            input_user_query (str): The user's query
            k (int): Number of results to return
            
        Returns:
            str: The most relevant suggestion from the database
        """
        try:
            search_result = self.vector_database.similarity_search(
                input_user_query,
                k=k
            )
            return search_result[0].page_content
        except Exception as e:
            raise Exception(f"Error generating suggestions: {str(e)}") 