from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from module_14.crud_functions import *

prod_base = get_all_products()

api = '*****'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
kb.add(button1)
kb.insert(button2)
kb.add(button3)
kb.add(button4)

ikb = InlineKeyboardMarkup(resize_keyboard=True)
i_button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
i_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ikb.add(i_button1)
ikb.add(i_button2)

ikb2 = InlineKeyboardMarkup(resize_keyboard=True)
ikb2_button1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
ikb2_button2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
ikb2_button3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
ikb2_button4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
ikb2.add(ikb2_button1)
ikb2.insert(ikb2_button2)
ikb2.add(ikb2_button3)
ikb2.insert(ikb2_button4)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=ikb)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for product in prod_base:
        await  asyncio.sleep(0.65)
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
        with open(f'{product[1]}.png', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=ikb2)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    try:
        int(data["weight"])
        int(data["growth"])
        int(data["age"])
        calorie_norm = (10 * int(data["weight"])) + (6.25 * int(data["growth"])) - (5 * int(data["age"]))
        await message.answer(f'Ваша норма калорий в сутки: {calorie_norm}')
        await state.finish()
    except ValueError:
        await message.answer('Введены неверные данные! Начните расчет заново и вводите целые числа.')
        await state.finish()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State('1000')

@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    user_data = await state.get_data()
    add_user(user_data['username'], user_data['email'], user_data['age'])
    await message.answer('Регистрация прошла успешно')
    await state.finish()

@dp.message_handler()
async  def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
