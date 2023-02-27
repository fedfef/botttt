import telebot
from telebot import types

bot = telebot.TeleBot('6140603915:AAF7bA6-pQPxCoSFZGa9yXCU6NNrATRFywo')
TO_CHAT_ID = '@Youtubebirza'


def start_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton(text='Биржа', url='https://t.me/Youtubebirza')
    item2 = types.InlineKeyboardButton(text='Проверить✅', callback_data='check1')
    markup.add(item1, item2)
    return markup


@bot.message_handler(commands=["start"])
def start(message):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id='-1001177710151',
                                    user_id=message.chat.id).status:
            markup = types.InlineKeyboardMarkup(row_width=1)
            item = types.InlineKeyboardButton('Выложить пост', callback_data='post1')
            item1 = types.InlineKeyboardButton('Поддержка', url='https://t.me/youtube_meneger')
            item2 = types.InlineKeyboardButton('Правила', url='https://telegra.ph/Pravila-02-24-32')

            markup.add(item, item1, item2)

            bot.send_message(message.chat.id,
                             f'🚨ВСЕ ОБЪЯВЛЕНИЯ БЕСПЛАТНЫЕ🚨\n\n'
                             f''
                             f'👇Если хотите разместить объявление нажмите на соответствующий раздел ниже👇',
                             parse_mode='html', reply_markup=markup)

            break
    else:
        bot.send_message(message.chat.id, 'Подпишись на биржу!', reply_markup=start_markup())




def check(call):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id='-1001177710151', user_id=call.message.chat.id).status:
            markup = types.InlineKeyboardMarkup(row_width=1)
            item = types.InlineKeyboardButton('Выложить пост', callback_data='post1')
            item1 = types.InlineKeyboardButton('Поддержка', url='https://t.me/youtube_meneger')
            item2 = types.InlineKeyboardButton('Правила', url='https://telegra.ph/Pravila-02-24-32')

            markup.add(item, item1, item2)

            bot.send_message(call.message.chat.id,
                             f'🚨ВСЕ ОБЪЯВЛЕНИЯ БЕСПЛАТНЫЕ🚨\n\n'
                             f''
                             f'👇Если хотите разместить объявление нажмите на соответствующий раздел ниже👇',
                             parse_mode='html', reply_markup=markup)
            break

    else:
        bot.send_message(call.message.chat.id, 'Подпишитесь на биржу!', reply_markup=start_markup())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'check1':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            check(call)

        if call.data == 'post1':
            status = ['creator', 'administrator', 'member']
            for i in status:
                if i == bot.get_chat_member(chat_id='-1001177710151', user_id=call.message.chat.id).status:
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item = types.InlineKeyboardButton('Выложить пост', callback_data='post1')
                    item1 = types.InlineKeyboardButton('Поддержка', url='https://t.me/youtube_meneger')
                    item2 = types.InlineKeyboardButton('Правила',
                                                       url='https://telegra.ph/Pravila-02-24-32')

                    markup.add(item, item1, item2)

                    mesg = bot.send_message(call.message.chat.id, 'Чтобы выложить пост, пришли мне его')

                    @bot.message_handler(commands=["start"])
                    def start(message):
                        bot.send_message(message.chat.id, 'Чтобы пользоваться ботом подпишись на нашу биржу!',
                                         reply_markup=start_markup())
                        return True

                    bot.register_next_step_handler(mesg, post)

                    break

            else:
                bot.send_message(call.message.chat.id, 'Подпишитесь на канал!', reply_markup=start_markup())

        if call.data == 'yes':
            status = ['creator', 'administrator', 'member']
            for i in status:
                if i == bot.get_chat_member(chat_id='-1001177710151', user_id=call.message.chat.id).status:
                    bot.forward_message(TO_CHAT_ID, call.message.chat.id, call.message.message_id - 1)

                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item = types.InlineKeyboardButton('Выложить пост', callback_data='post1')
                    item1 = types.InlineKeyboardButton('Поддержка', url='https://t.me/youtube_meneger')
                    item2 = types.InlineKeyboardButton('Правила', url='https://telegra.ph/Pravila-02-24-32')

                    markup.add(item, item1, item2)

                    bot.send_message(call.message.chat.id, 'Пост был успешно выложен✅', reply_markup=markup)

                    break

                else:
                    bot.send_message(call.message.chat.id, 'Подпишитесь на канал!', reply_markup=start_markup())

        if call.data == 'no':
            status = ['creator', 'administrator', 'member']
            for i in status:
                if i == bot.get_chat_member(chat_id='-1001177710151',
                                            user_id=call.message.chat.id).status:
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item = types.InlineKeyboardButton('Выложить пост', callback_data='post1')
                    item1 = types.InlineKeyboardButton('Поддержка', url='https://t.me/youtube_meneger')
                    item2 = types.InlineKeyboardButton('Правила', url='https://telegra.ph/Pravila-02-24-32')

                    markup.add(item, item1, item2)

                    bot.send_message(call.message.chat.id,
                                     f'🚨ВСЕ ОБЪЯВЛЕНИЯ БЕСПЛАТНЫЕ🚨\n\n'
                                     f''
                                     f'👇Если хотите разместить объявление нажмите на соответствующий раздел ниже👇',
                                     parse_mode='html', reply_markup=markup)

                    break
            else:
                bot.send_message(call.message.chat.id, 'Чтобы пользоваться ботом подпишись на нашу биржу!',
                                 reply_markup=start_markup())



def lrlr(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Выложить пост', callback_data='post1')
    item1 = types.InlineKeyboardButton('Поддержка', url='https://t.me/youtube_meneger')
    item2 = types.InlineKeyboardButton('Правила', url='https://telegra.ph/Pravila-02-24-32')

    markup.add(item, item1, item2)

    bot.send_message(message.chat.id, 'Пост был успешно выложен✅', reply_markup=markup)


def post(message):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id='-1001177710151',
                                    user_id=message.chat.id).status:
            if message.text == '/start':
                start(message)

            else:
                markup = types.InlineKeyboardMarkup(row_width=1)
                item = types.InlineKeyboardButton('Да', callback_data='yes')
                item1 = types.InlineKeyboardButton('Нет', callback_data='no')

                markup.add(item, item1)
                bot.send_message(message.chat.id, 'Вы уверенны, что хотите выложить пост?', reply_markup=markup)

            break
    else:
        bot.send_message(message.chat.id, 'Подпишитесь на канал!',
                         reply_markup=start_markup())

bot.polling(none_stop=True)
