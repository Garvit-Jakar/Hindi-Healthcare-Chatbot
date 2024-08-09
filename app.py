import rasa.core.agent
import gradio as gr
import asyncio

# Load your trained Rasa model
agent = rasa.core.agent.Agent.load('models')
history = []

async def chat(message):
    global history
    responses = await agent.handle_text(message)
    response_text = " ".join([response["text"] for response in responses if "text" in response])
    history.append("User: "+ message)
    history.append("Bot: "+ response_text +"\n")

    return "\n".join(history)


# Create the Gradio interface
interface = gr.Interface(
    fn=chat, 
    inputs=["text"],
    outputs="text",
    title="Hindi healthcare chatbot (हिंदी हेल्थकेयर चैटबॉट)",
    description="This is a simple chatbot powered by Rasa and Gradio."
)


if __name__ == "__main__":
    interface.launch()
