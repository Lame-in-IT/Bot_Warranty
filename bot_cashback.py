from tokin_bot import TOKIN, id_user
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

from database import read_bd, create_user, create_appeal_True, read_appeal_True, create_appeal
from database import create_screenshot

bot = Bot(token=TOKIN, parse_mode="HTML")
dp = Dispatcher(bot)
    
@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    user_id = read_bd(str(message.from_user.id))
    if user_id == True:
        mass_text = "start"
        create_appeal_True(message.from_user.id, mass_text)
    elif user_id == False:
        create_user(message.from_user)
    await bot.send_message(message.from_user.id, 'Здравствуйте {0.first_name}!\n'
                           'Для начала, хотим сказать спасибо за выбор нашей компании. Это нас очень радует!\n'
                           'А еще, для нас важно ваше впечатление о нашем продукте.\n'
                           'Мы предоставив вам гарантию на вакуумный упаковщик после пары шагов.\n\n'
                           '1. Сообщите нам в каком из маркетплейсов вы его купили. Нажав соответствующую кнопку.\n\n'
                           '2. Напишите дату покупки.\n\n'
                           '3. Если у вас возникла гарантийная ситуация, вы можите написать нам, после нажатия кнопки "Обращение"'.format(message.from_user), reply_markup=nav.mainMenu)
    
    
@dp.message_handler(text="OZON")
async def bot_message(message: types.Message):
    mass_text = "OZON"
    create_appeal_True(message.from_user.id, mass_text)
    await bot.send_message(message.from_user.id, 'Отлично {0.first_name}. Спасибо вам!\n'
                           'Теперь напишите сюда дату когда вы приобрели вакуумный упаковщик.'.format(message.from_user), reply_markup=nav.backerMenu)
    
@dp.message_handler(text="Wildberries")
async def bot_message(message: types.Message):
    mass_text = "Wildberries"
    create_appeal_True(message.from_user.id, mass_text)
    await bot.send_message(message.from_user.id, 'Отлично {0.first_name}. Спасибо вам!\n'
                           'Теперь напишите сюда дату когда вы приобрели вакуумный упаковщик.'.format(message.from_user), reply_markup=nav.backerMenu)

@dp.message_handler(text="Обращение")
async def bot_message(message: types.Message):
    mass_text = "Обращение"
    create_appeal_True(message.from_user.id, mass_text)
    await bot.send_message(message.from_user.id, 'Если у вас возник вопрос или проблема, вы можете написать тут и менеджер получит ваше сообщение.'.format(message.from_user), reply_markup=nav.backerMenu)


@dp.message_handler(text="1. Вернуться в начало")
async def bot_message(message: types.Message):
    mass_text = "1. Вернуться в начало"
    create_appeal_True(message.from_user.id, mass_text)
    await command_start(message)
       
@dp.message_handler()
async def bot_message(message: types.Message):
    read_appeal_text = read_appeal_True(message.from_user.id)
    if read_appeal_text == "Обращение":
        create_appeal(message.from_user.id, message.text)
        await bot.send_message(chat_id=id_user[0], text=f"Пользователь с именем https://t.me/{message.from_user.username} отправил сообщение.\n\n{message.text}".format(message.from_user))
        await bot.send_message(message.from_user.id, 'Ваше обращение принято в работу. В ближайшее время наш менеджер свяжется с Вами😊 Также у нашего менеджера есть рабочий график и на выходных он отдыхает😜'.format(message.from_user), reply_markup=nav.backerMenu)
    elif read_appeal_text in ["OZON", "Wildberries"]:
        date_sale = create_screenshot(message.from_user.id, message.text)
        await bot.send_message(message.from_user.id, f'{date_sale}'.format(message.from_user))
    else:
        await bot.send_message(message.from_user.id, 'Я вас не понял'.format(message.from_user))   
       
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)