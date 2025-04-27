import chainlit as cl

@cl.on_message
async def main(message: cl.Message):        
    response =f"Hi,how are you:{message.content}"
    await  cl.Message(content=response).send()

