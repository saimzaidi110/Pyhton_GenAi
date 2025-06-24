# # from together import Together
# # from dotenv import load_dotenv
# # import os

# # load_dotenv()
# # api_key =os.getenv("TOGETHER_API_KEY")
# # client = Together(api_key=api_key) # auth defaults to os.environ.get("TOGETHER_API_KEY")

# # response = client.chat.completions.create(
# #     model="deepseek-ai/DeepSeek-V3",
# #     messages=[
# #       {
# #         "role": "user",
# #         "content": "Who is Imran Khan"
# #       }
# #     ]
# # )
# # print(response.choices[0].message.content)



# from together import Together
# from dotenv import load_dotenv
# import os

# def main():
#     load_dotenv()
#     api_key = os.getenv("TOGETHER_API_KEY")
#     if not api_key:
#         print("Error: TOGETHER_API_KEY environment variable not set.")
#         return

#     client = Together(api_key=api_key)

#     system_message = {
#         "role": "system",
#         "content": (
#             "You are a helpful assistant who is an expert only in Physics. "
#             "If the user asks anything unrelated to Physics, politely say that you don't know "
#             "and that you are only a Physics expert."
#         )
#     }

#     print("Physics Expert Chatbot started! Type 'exit' to quit.")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'exit':
#             print("Chatbot stopped.")
#             break

#         messages = [
#             system_message,
#             {"role": "user", "content": user_input}
#         ]

#         response = client.chat.completions.create(
#             model="deepseek-ai/DeepSeek-V3",
#             messages=messages
#         )

#         bot_reply = response.choices[0].message.content
#         print("Bot:", bot_reply)


# if __name__ == "__main__":
#     main()





# import gradio as gr
# from together import Together
# from dotenv import load_dotenv
# import os

# load_dotenv()

# api_key = os.getenv("TOGETHER_API_KEY")
# client = Together(api_key=api_key)

# system_message = {
#     "role": "system",
#     "content": (
#         "You are a helpful assistant who is an expert only in Physics. "
#         "If the user asks anything unrelated to Physics, politely say that you don't know "
#         "and that you are only a Physics expert."
#     )
# }

# def physics_chatbot(user_input, history):
#     messages = [system_message]
#     for h in history:
#         messages.append({"role": "user", "content": h[0]})
#         messages.append({"role": "assistant", "content": h[1]})
#     messages.append({"role": "user", "content": user_input})

#     response = client.chat.completions.create(
#         model="deepseek-ai/DeepSeek-V3",
#         messages=messages
#     )

#     bot_reply = response.choices[0].message.content
#     history.append((user_input, bot_reply))
#     return history, history

# with gr.Blocks() as demo:
#     gr.Markdown("## Physics Expert Chatbot")
#     chatbot = gr.Chatbot()
#     user_input = gr.Textbox(placeholder="Ask me anything about Physics...")
#     state = gr.State([])  # to keep chat history

#     def respond(user_message, chat_history):
#         return physics_chatbot(user_message, chat_history)

#     user_input.submit(respond, inputs=[user_input, state], outputs=[chatbot, state])
#     user_input.submit(lambda: "", None, user_input)  # clear input box after submit

# demo.launch()
