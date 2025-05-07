from langchain_openai import OpenAI
from langchain.prompts import ChatPromptTemplate
from .config import COMPLETION_MODEL_NAME, TEMPLATE_GENERATE_FEATURES, TEMPLATE_COMPARISON

class AIService:
    def __init__(self):
        self.inference_bot = OpenAI(
            model_name=COMPLETION_MODEL_NAME,
            temperature=0.0,
        )
        self.features_template = ChatPromptTemplate.from_template(TEMPLATE_GENERATE_FEATURES)
        self.comparison_template = ChatPromptTemplate.from_template(TEMPLATE_COMPARISON)
    
    def generate_items_in_common(self, input_query: str, database_suggestion: str) -> str:
        """
        Generate a comparison between user requirements and database suggestions.
        
        Args:
            input_query (str): The user's query
            database_suggestion (str): The suggestion from the database
            
        Returns:
            str: The comparison results
        """
        try:
            # Generate features from user query
            prompt_features = self.features_template.format_messages(
                query_user=input_query,
            )
            bot_response_features = self.inference_bot.invoke(prompt_features)

            # Compare features with database suggestion
            prompt_comparison = self.comparison_template.format_messages(
                user_list_requirements=bot_response_features,
                output_database=database_suggestion
            )
            bot_response_comparison = self.inference_bot.invoke(prompt_comparison)
            
            return bot_response_comparison
        except Exception as e:
            raise Exception(f"Error generating items in common: {str(e)}") 