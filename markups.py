from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --- Main Menu ---
btnprice = KeyboardButton('OZON')
btnreviews = KeyboardButton('Wildberries')
btnsale = KeyboardButton('Обращение')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnprice).add(btnreviews).add(btnsale)

# ---Back Menu ---
backmenu = KeyboardButton('1. Вернуться в начало')
backerMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(backmenu)