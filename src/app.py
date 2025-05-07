import gradio as gr
from database import VectorDatabase
from ai_service import AIService

class RealEstateChatbot:
    def __init__(self):
        self.db = VectorDatabase()
        self.ai = AIService()
    
    def generate_suggestions(self, input_user_query: str) -> str:
        """Generate suggestions based on user query."""
        return self.db.generate_suggestions(input_user_query)
    
    def generate_items_in_common(self, input_query: str, database_suggestion: str) -> str:
        """Generate comparison between user requirements and database suggestions."""
        return self.ai.generate_items_in_common(input_query, database_suggestion)

def create_interface():
    """Create and launch the Gradio interface."""
    chatbot = RealEstateChatbot()
    
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column(scale=1):
                query_user = gr.Textbox(label="Introduce what you are looking for in a house!")
                suggestion_button = gr.Button("Generate Suggestion!")

            with gr.Column(scale=1):
                output_database = gr.Textbox(label="Suggested output")
                similarities_button = gr.Button("Find Similarities!")

                suggestion_button.click(
                    chatbot.generate_suggestions,
                    inputs=[query_user],
                    outputs=[output_database]
                )

            with gr.Column(scale=1):
                similarities = gr.Textbox(label="Items in common!")
                similarities_button.click(
                    chatbot.generate_items_in_common,
                    inputs=[query_user, output_database],
                    outputs=[similarities]
                )
    
    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch() 