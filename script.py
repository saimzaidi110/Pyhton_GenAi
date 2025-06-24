import gradio as gr
from together import Together
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

if not api_key:
    raise ValueError("TOGETHER_API_KEY environment variable not set")

client = Together(api_key=api_key)

system_message = {
    "role": "system",
    "content": (
        "You are a helpful assistant who is an expert only in Physics. "
        "If the user asks anything unrelated to Physics, politely say that you don't know "
        "and that you are only a Physics expert."
        "Always respond only in English or roman english, no matter what language the user uses."
    )
}

def physics_chatbot(user_input, history):
    # Prepare messages for the model with history included
    messages = [system_message]
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        messages.append({"role": "assistant", "content": h[1]})
    messages.append({"role": "user", "content": user_input})

    # Get response from Together API
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=messages
    )

    bot_reply = response.choices[0].message.content
    history.append((user_input, bot_reply))
    return history, history

with gr.Blocks() as demo:
    gr.Markdown("## Physics Expert Chatbot")
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(placeholder="Ask me anything about Physics...")
    state = gr.State([])  # To store conversation history

    def respond(user_message, chat_history):
        return physics_chatbot(user_message, chat_history)

    user_input.submit(respond, inputs=[user_input, state], outputs=[chatbot, state])
    user_input.submit(lambda: "", None, user_input)  # Clear input box after submit

demo.launch()
