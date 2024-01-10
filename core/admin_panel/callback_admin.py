from aiogram import F

from core.dispatcher import dp
from aiogram.types import CallbackQuery
from core.db.questions.functions_db import delete_question_from_db

question_info = dict()


async def question_info_for_answer(question):
    global question_info
    question_info = question


@dp.callback_query(F.data == "not_now")
async def not_now(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()


@dp.callback_query(F.data == "delete_question")
async def delete_question(callback: CallbackQuery):
    await delete_question_from_db(question_info)
    await callback.answer()
    await callback.message.delete()
