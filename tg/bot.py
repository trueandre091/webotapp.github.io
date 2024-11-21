from utils import *
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

CONFIG = os.path.join(os.path.dirname(__file__), "config", "const.txt")

with open(CONFIG, encoding="utf-8") as f:
    TOKEN = f.readline().split()[1]

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
