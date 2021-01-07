from settings import token, channel_chat_id, help_text
import asyncio
from aiogram import Bot, Dispatcher, types
import aiogram
import time
import random
from utils import give_qoute

async def post_quote_in_channel():
	quote = give_qoute()
	await bot.send_message(chat_id=channel_chat_id, text=quote)


async def send_help(event: types.Message):
	await event.answer(help_text)


async def send_quote(event: types.Message):
	quote = give_qoute()
	await event.answer(quote)

def give_dispatcher(bot):
	disp = Dispatcher(bot=bot)
	disp.register_message_handler(send_quote, commands={"quote"})
	disp.register_message_handler(send_help, commands={"help", "start"})
	return disp
	


def repeat_check(coro, loop):
	asyncio.ensure_future(coro(), loop=loop)
	time_for_wait = random.randint(10800, 21600)
	loop.call_later(time_for_wait, repeat_check, coro, loop)

if __name__ == '__main__':
	
	bot = Bot(token=token)
	disp = give_dispatcher(bot)


	loop = asyncio.get_event_loop()
	loop.call_later(5, repeat_check, post_quote_in_channel, loop)
	aiogram.utils.executor.start_polling(disp, skip_updates=True, loop=loop)
