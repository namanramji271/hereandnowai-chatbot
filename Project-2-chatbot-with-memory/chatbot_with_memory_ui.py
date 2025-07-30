import gradio as gr
from chatbot_with_memory import get_response
import json
import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "branding.json"))) as f:
    brand_info = json.load(f)["brand"]

with gr.Blocks(theme = "default",title=brand_info["organizationName"]) as app:
    gr.HTML(f"""<div style ="display":flex; justify-content:center; margin-bottom:20px;">
            <img src="{brand_info["logo"]["title"]}" alt="{brand_info["organizationName"]} Logo" style="height:100px;">
            </div>""")
    
    gr.ChatInterface(
        fn=get_response,
        chatbot=gr.Chatbot(height = 500,avatar_images=(None,brand_info["chatbot"]["avatar"]),type="messages"),
        description=brand_info["slogan"],
        title=brand_info["organizationName"],
        type="messages",
        examples=[
            ["How to stay focused?"],
            ["Give me hope"],
            ["How long will it take for being successful?"]
        ]
    )

if __name__ == "__main__":
    app.launch()
    