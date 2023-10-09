import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a soccer and cricket expert analyst. Your name is Zinels."}]

def ZinelsChat(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    
    # Override system message response to set the bot's name as "Zinels"
    if "whats your name" in user_input.lower():
        ChatGPT_reply = "My name is Zinels."
    
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

zinels_interface = gradio.Interface(fn=ZinelsChat, inputs="text", outputs="text", title="Zinels")

zinels_interface.launch(share=True)

