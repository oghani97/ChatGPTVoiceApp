import asyncio
import re 
from EdgeGPT import Chatbot, ConversationStyle

async def main():
    bot = Chatbot(cookie_path='./cookies.json')
    response = await bot.ask(prompt=input("Ask Bing AI: "), conversation_style=ConversationStyle.creative)
    for message in response["item"]["messages"]:
        if message["author"] == "bot":
            bot_response = message["text"]

    bot_response = re.sub('\[\^\d+\^\]', '', bot_response)

    print("BOT'S RESPONSE:", bot_response)

    await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
