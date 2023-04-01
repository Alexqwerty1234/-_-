import logging
import re
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message
import math 
API_TOKEN = '5936956717:AAFRgktvjjhJsuA50m9R0Ce-4ZLkKtGlYms'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("<i><b><u>Приветствую вас в моем чат боте!!</u></b></i>👋 \n" "В нем я вам покажу какой у вас BFI и расскажу, что нужно сделать если он у вас выше нормы.\n BFI -  это отношение массы тела, занимаемой жирной тканью, к общей массе тела.\n Обычно, для мужчин 👱‍♂️ нормальный уровень жировой массы составляет 10-20%, а для женщин 👩- 20-30%.\n Однако, этот показатель может варьироваться в зависимости от возраста, физической активности, типа телосложения и других факторов.")
    await message.answer("<b> Для начала введите свои данные в таком порядке: \n Ваш пол, вес, рост и возраст.\n<u><b>ВАЖНО</b></u>\n Нужно вводить маленькую букву и числа без запятых\n Пример(м 70 180 16)</b>")

@dp.message_handler()
async def echo_message(message: types.Message):
    global  a1,s,BFI1
    a1 = message.text
    if re.search(r"\d", a1):
        if 'ж' in message.text:
            numbers = re.findall(r"[-+]?\d*\.\d+|\d+", a1)
            numbers = [int(num) for num in numbers]
            numbers[1]= numbers[1]/100
            BFI1 = (1.2 * numbers[0]) / math.pow(numbers[1],2) + (0.23 * numbers[2]) - 5.4
            await message.answer("Ваш BFI = %s  "%round(BFI1,1))
            if BFI1>20 and BFI1<=30:
                await message.answer("У вас идеальная фигура 👌")
            elif BFI1>30 and BFI1<=35:
                await message.answer(" У вас присутствуют небольшие осложнения")
            elif BFI1>35 and BFI1<=40:
                await message.answer("Ваш жировой индекс выше среднего")
            elif BFI1>40:
                await message.answer("У вас проблемы с ожирением")

        elif "м" in message.text:
            global a,s,BFI
            a = message.text
            numbers = re.findall(r"[-+]?\d*\.\d+|\d+", a)
            numbers = [int(num) for num in numbers]
            numbers[1]= numbers[1]/100
            BFI = (1.2 * numbers[0]) / math.pow(numbers[1],2) + (0.23 * numbers[2]) - 5.4
            await message.answer("Ваш BFI = %s  "%round(BFI,1))
            if BFI>10 and BFI<=20:
                await message.answer("У вас идеальное телосложение 👌")
            elif BFI>20 and BFI<=25:
                await message.answer(" У вас присутствуют небольшие осложнения")
            elif BFI>25 and BFI<=30:
                await message.answer("Ваш жировой индекс выше среднего")
            elif BFI>30 and BFI<=35:
                await message.answer("Ваш жировой индекс зашкаливает")
            elif BFI>40:
                await message.answer("У вас большие проблемы с ожирением")
        else:
            await message.reply("I'm not sure what you mean.")

        keyboard = types.ReplyKeyboardMarkup()
        button_1 = types.KeyboardButton(text="Похудеть")
        keyboard.add(button_1)
        button_2 = "Поддерживать зож"
        keyboard.add(button_2)
        await message.answer("Что вы предпочтёте для изменения вашего BFI:", reply_markup=keyboard)

    
    else:
        if message.text == "Похудеть":
            await message.answer("Для похудения вам нужно будет проходить ежедневно 15000 шагов и есть только здоровое питание.\n В качестве шагомера я вам рекомендую это приложение: \n - Для Android: \n https://play.google.com/store/apps/details?id=ru.ligazn.shagi \n - Для Ios:\n https://apps.apple.com/ru/app/%D1%87%D0%B5%D0%BB%D0%BE%D0%B2%D0%B5%D0%BA-%D0%B8%D0%B4%D1%83%D1%89%D0%B8%D0%B9/id1476034888")
        elif message.text == "Поддерживать зож":
            await message.answer("Если вы хотите поддерживать Здоровый Образ Жизни, то ваша цель - 5000 шагов в день и есть только здоровое питание. \n В качестве шагомера я вам рекомендую это приложение: \n - Для Android: \n https://play.google.com/store/apps/details?id=ru.ligazn.shagi \n - Для Ios:\n https://apps.apple.com/ru/app/%D1%87%D0%B5%D0%BB%D0%BE%D0%B2%D0%B5%D0%BA-%D0%B8%D0%B4%D1%83%D1%89%D0%B8%D0%B9/id1476034888")    
   


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)