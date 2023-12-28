from background import keep_alive
import telebot
from telebot import types
import random
import time

bot = telebot.TeleBot('6971674722:AAEYxppv1TCyeD0T6RAR8PchfCLRdtqvpXU')

active = False
quant_nd = None
quant = None
lvl = None
errors = None

num_1 = None
num_2 = None

result = None
gen_result = None

example = None
gen_example = None
example_error = []


# обработка команды "старт"
@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Начнем!', callback_data='begin'))
    hey1 = f'Добро пожаловать {message.from_user.first_name}! '
    hey2 = ('Я здесь, чтобы помочь тебе стать мастером умножения в уме. '
            'Давай вместе прокачаем твои математические навыки!😉')
    hey3 = hey1 + '\n' * 2 + hey2
    bot.send_message(message.chat.id, hey3, reply_markup=markup)


# остановка тренировки
@bot.message_handler(commands=['stop'])
def main(message):
    global active
    global quant
    active = False
    quant = 0
    print('пользователь остановил тренировку')
    mes = 'Хорошо. Напишите /start, если захотите снова начать тренировку'
    bot.send_message(message.chat.id, 'Вот твои результаты:')
    bot.send_message(message.chat.id, f'Ошибок: {errors}')
    bot.send_message(message.chat.id, mes)


# вызов техподдержки
@bot.message_handler(commands=['help'])
def main(message):
    print('пользователь вызвал техподдержку')
    mes = 'У вас возникли проблемы? За их решением вы можете обратиться в техподдержку - @DunaConceptArtist'
    bot.send_message(message.chat.id, mes)


# обработка фото
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    print('пользователь прислал фото')
    answer = 'К сожалению я не могу обрабатывать фото, лучше обратитесь в техподдержку по команде /help'
    bot.reply_to(message, answer)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJUe2VFCe9UZ2-QrYqaE0B2LRMwKMwfAAINAAPANk8TpPnh9NR4jVMzBA')


# обработка кнопочек
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global active
    global quant_nd
    global quant
    global example
    global example_error
    global lvl
    global result
    global errors
    global num_1
    global num_2

    # выбор уровня подготовки
    if callback.data == 'begin':
        print('пользователь выбирает уровень подготовки')
        active = False
        lvl = 0
        quant = 0
        example_error = []
        markup1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('I', callback_data='oneLvl')
        btn2 = types.InlineKeyboardButton('II', callback_data='twoLvl')
        markup1.add(btn1, btn2)
        btn3 = types.InlineKeyboardButton('III', callback_data='threeLvl')
        markup1.row(btn3)
        msg = 'Выберите уровень подготовки. На его основе будет подобран алгоритм генерации примеров'
        bot.send_message(callback.message.chat.id, msg, reply_markup=markup1)

    # первый уровень подготовки
    if callback.data == 'oneLvl':
        print('пользователь выбрал первый уровень подготовки')
        lvl = 1
        print('пользователь выбирает количество примеров')
        markup1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('10', callback_data='ten')
        btn2 = types.InlineKeyboardButton('15', callback_data='fifteen')
        markup1.add(btn1, btn2)
        btn3 = types.InlineKeyboardButton('20', callback_data='twenty')
        btn4 = types.InlineKeyboardButton('25', callback_data='twenty_fifth')
        markup1.row(btn3, btn4)
        msg = 'Выбери количество примеров, которое ты хочешь получить'
        bot.send_message(callback.message.chat.id, msg, reply_markup=markup1)

    # второй уровень подготовки
    if callback.data == 'twoLvl':
        print('пользователь выбрал второй уровень подготовки')
        lvl = 2
        print('пользователь выбирает количество примеров')
        markup1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('10', callback_data='ten')
        btn2 = types.InlineKeyboardButton('15', callback_data='fifteen')
        markup1.add(btn1, btn2)
        btn3 = types.InlineKeyboardButton('20', callback_data='twenty')
        btn4 = types.InlineKeyboardButton('25', callback_data='twenty_fifth')
        markup1.row(btn3, btn4)
        msg = 'Выбери количество примеров, которое ты хочешь получить'
        bot.send_message(callback.message.chat.id, msg, reply_markup=markup1)

    # третий уровень подготовки
    if callback.data == 'threeLvl':
        print('пользователь выбрал третий уровень подготовки')
        lvl = 3
        print('пользователь выбирает количество примеров')
        markup1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('10', callback_data='ten')
        btn2 = types.InlineKeyboardButton('15', callback_data='fifteen')
        markup1.add(btn1, btn2)
        btn3 = types.InlineKeyboardButton('20', callback_data='twenty')
        btn4 = types.InlineKeyboardButton('25', callback_data='twenty_fifth')
        markup1.row(btn3, btn4)
        msg = 'Выбери количество примеров, которое ты хочешь получить'
        bot.send_message(callback.message.chat.id, msg, reply_markup=markup1)

    # десять примеров
    elif callback.data == 'ten':
        quant_nd = 10

        errors = 0

        active = True

        quant = 1


    # пятнадцать примеров
    elif callback.data == 'fifteen':
        quant_nd = 15

        errors = 0

        active = True

        quant = 1

    # двадцать примеров
    elif callback.data == 'twenty':
        quant_nd = 20

        errors = 0

        active = True

        quant = 1

    # двадцать пять примеров
    elif callback.data == 'twenty_fifth':
        quant_nd = 25

        errors = 0

        active = True

        quant = 1

    # алгоритм
    if active:
        print('пользователь начал тренировку')
        bot.send_message(callback.message.chat.id, 'Хорошо, напишите /example, чтобы получить первый пример')
        while active:
            # алгоритм первого уровня
            if active and lvl == 1 and quant != quant_nd + 1:
                print('алгоритм первого уровня')
                bot.send_message(callback.message.chat.id,
                                 'Хорошо, напишите /stop, если захотите остановить тренировку')
                while quant != quant_nd + 1:
                    if int(quant) == 1:
                        print('первый пример')
                        num_1 = random.randint(6, 9)
                        num_2 = random.randint(6, 9)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if int(quant) == 2:
                        print('второй пример')
                        num_1 = random.randint(6, 9)
                        num_2 = random.randint(11, 29)
                        while num_2 % 10 == 0:
                            num_2 = random.randint(11, 29)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if int(quant) == 3:
                        print('третий пример')
                        num_1 = random.randint(11, 15)
                        num_2 = random.randint(29, 31)
                        while num_1 % 10 == 0:
                            num_1 = random.randint(11, 15)
                        while num_2 % 10 == 0:
                            num_2 = random.randint(29, 31)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if 6 > int(quant) >= 4:
                        print('четвертый - пятый пример')
                        num_1 = random.randint(12, 19)
                        num_2 = random.randint(12, 19)
                        if int(quant) == 4:
                            while num_1 % 10 == 0 or num_1 * num_2 > 400:
                                num_1 = random.randint(12, 19)
                            while num_2 % 10 == 0 or num_1 * num_2 > 400:
                                num_2 = random.randint(12, 19)
                        if int(quant) == 5:
                            while num_1 % 10 == 0 or num_1 * num_2 > 500:
                                num_1 = random.randint(12, 19)
                            while num_2 % 10 == 0 or num_1 * num_2 > 500:
                                num_2 = random.randint(12, 19)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if 10 > int(quant) >= 6:
                        print('шестой - девятый пример')
                        num_1 = random.randint(12, 29)
                        num_2 = random.randint(12, 29)
                        if int(quant) == 6:
                            while num_1 % 10 == 0 or 300 > num_1 * num_2 > 600:
                                num_1 = random.randint(12, 29)
                            while num_2 % 10 == 0 or 300 > num_1 * num_2 > 600:
                                num_2 = random.randint(12, 29)
                        if int(quant) == 7:
                            while num_1 % 10 == 0 or 300 > num_1 * num_2 > 700:
                                num_1 = random.randint(12, 29)
                            while num_2 % 10 == 0 or 300 > num_1 * num_2 > 700:
                                num_2 = random.randint(12, 29)
                        if 10 > int(quant) >= 8:
                            while num_1 % 10 == 0 or 400 > num_1 * num_2 > 800:
                                num_1 = random.randint(12, 29)
                            while num_2 % 10 == 0 or 400 > num_1 * num_2 > 800:
                                num_2 = random.randint(12, 29)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if int(quant) >= 10:
                        print('десятый - двадцать пятый пример')
                        num_1 = random.randint(21, 28)
                        num_2 = random.randint(21, 28)
                        while num_1 % 10 == 0 or num_1 * num_2 < 600:
                            num_1 = random.randint(12, 34)
                        while num_2 % 10 == 0 or num_1 * num_2 < 600:
                            num_2 = random.randint(12, 34)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if quant > quant_nd:
                        print('тренировка закончилась')
                        active = False
                        bot.send_message(callback.message.chat.id, 'Молодец! Тренировка закончилась')
                        bot.send_message(callback.message.chat.id, 'Вот твои результаты:')
                        bot.send_message(callback.message.chat.id, f'Ошибок: {errors}')
                        if errors != 0:
                            bot.send_message(callback.message.chat.id, '\n'.join(example_error))
                        bot.send_sticker(callback.message.chat.id,
                                         'CAACAgIAAxkBAAJUgWVFItTcElyotiIzQOC-rTArAAGMeQACEwADwDZPE6qzh_d_OMqlMwQ')
                        time.sleep(5)
                        bot.send_message(callback.message.chat.id,
                                         'Напиши /start, если захочешь снова начать тренировку')

            # алгоритм второго уровня
            if active and lvl == 2 and quant != quant_nd + 1:
                print('алгоритм второго уровня')
                bot.send_message(callback.message.chat.id,
                                 'Хорошо, напишите /stop, если захотите остановить тренировку')
                while quant != quant_nd + 1:
                    if int(quant) == 1:
                        print('первый пример')
                        num_1 = random.randint(6, 9)
                        num_2 = random.randint(6, 9)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if int(quant) == 2:
                        print('второй пример')
                        num_1 = random.randint(6, 9)
                        num_2 = random.randint(11, 29)
                        while num_2 % 10 == 0:
                            num_2 = random.randint(11, 29)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if int(quant) == 3:
                        print('третий пример')
                        num_1 = random.randint(11, 15)
                        num_2 = random.randint(31, 49)
                        while num_1 % 10 == 0 and num_1 * num_2 < 450:
                            num_1 = random.randint(11, 15)
                        while num_2 % 10 == 0 and num_1 * num_2 < 450:
                            num_2 = random.randint(31, 49)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if 6 > int(quant) >= 4:
                        print('четвертый - пятый пример')
                        num_1 = random.randint(21, 29)
                        num_2 = random.randint(21, 29)
                        if int(quant) == 4:
                            while num_1 % 10 == 0 or num_1 * num_2 > 700:
                                print('перегенерация')
                                num_1 = random.randint(21, 39)
                            while num_2 % 10 == 0 or num_1 * num_2 > 700:
                                print('перегенерация')
                                num_2 = random.randint(21, 39)
                        if int(quant) == 5:
                            while num_1 % 10 == 0 or num_1 * num_2 > 800:
                                print('перегенерация')
                                num_1 = random.randint(21, 39)
                            while num_2 % 10 == 0 or num_1 * num_2 > 800:
                                print('перегенерация')
                                num_2 = random.randint(21, 39)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if 10 > int(quant) >= 6:
                        print('шестой - девятый пример')
                        num_1 = random.randint(22, 39)
                        num_2 = random.randint(22, 39)
                        if int(quant) == 6:
                            while num_1 % 10 == 0 or 400 > num_1 * num_2 > 800:
                                num_1 = random.randint(22, 39)
                            while num_2 % 10 == 0 or 400 > num_1 * num_2 > 800:
                                num_2 = random.randint(22, 39)
                        if int(quant) == 7:
                            while num_1 % 10 == 0 or 500 > num_1 * num_2 > 900:
                                num_1 = random.randint(22, 39)
                            while num_2 % 10 == 0 or 500 > num_1 * num_2 > 900:
                                num_2 = random.randint(22, 39)
                        if 10 > int(quant) >= 8:
                            while num_1 % 10 == 0 or 700 > num_1 * num_2 > 1000:
                                num_1 = random.randint(22, 39)
                            while num_2 % 10 == 0 or 700 > num_1 * num_2 > 1000:
                                num_2 = random.randint(22, 39)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if int(quant) >= 10:
                        print('десятый - двадцать пятый пример')
                        num_1 = random.randint(21, 49)
                        num_2 = random.randint(21, 49)
                        while num_1 % 10 == 0 or 900 > num_1 * num_2:
                            num_1 = random.randint(21, 49)
                        while num_2 % 10 == 0 or 900 > num_1 * num_2:
                            num_2 = random.randint(21, 49)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if quant > quant_nd:
                        print('тренировка закончилась')
                        active = False
                        bot.send_message(callback.message.chat.id, 'Молодец! Тренировка закончилась')
                        bot.send_message(callback.message.chat.id, 'Вот твои результаты:')
                        bot.send_message(callback.message.chat.id, f'Ошибок: {errors}')
                        if errors != 0:
                            bot.send_message(callback.message.chat.id, '\n'.join(example_error))
                        bot.send_sticker(callback.message.chat.id,
                                         'CAACAgIAAxkBAAJUgWVFItTcElyotiIzQOC-rTArAAGMeQACEwADwDZPE6qzh_d_OMqlMwQ')
                        time.sleep(5)
                        bot.send_message(callback.message.chat.id,
                                         'Напиши /start, если захочешь снова начать тренировку')

            # алгоритм третьего уровня
            if active and lvl == 3 and quant != quant_nd + 1:
                print('алгоритм третьего уровня')
                bot.send_message(callback.message.chat.id,
                                 'Хорошо, напишите /stop, если захотите остановить тренировку')
                while quant != quant_nd + 1:
                    if int(quant) == 1:
                        print('первый пример')
                        num_1 = random.randint(7, 12)
                        num_2 = random.randint(7, 12)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if int(quant) == 2:
                        print('второй пример')
                        num_1 = random.randint(7, 12)
                        num_2 = random.randint(15, 32)
                        while num_2 % 10 == 0:
                            num_2 = random.randint(11, 29)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if int(quant) == 3:
                        print('третий пример')
                        num_1 = random.randint(12, 17)
                        num_2 = random.randint(34, 52)
                        while num_1 % 10 == 0:
                            num_1 = random.randint(12, 17)
                        while num_2 % 10 == 0:
                            num_2 = random.randint(34, 52)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if 6 > int(quant) >= 4:
                        print('четвертый - пятый пример')
                        num_1 = random.randint(24, 32)
                        num_2 = random.randint(24, 32)
                        if int(quant) == 4:
                            while num_1 % 10 == 0 or num_1 * num_2 > 900:
                                num_1 = random.randint(24, 32)
                            while num_2 % 10 == 0 or num_1 * num_2 > 900:
                                num_2 = random.randint(24, 32)
                        if int(quant) == 5:
                            while num_1 % 10 == 0 or num_1 * num_2 > 900:
                                num_1 = random.randint(24, 32)
                            while num_2 % 10 == 0 or num_1 * num_2 > 900:
                                num_2 = random.randint(24, 32)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if 10 > int(quant) >= 6:
                        print('шестой - девятый пример')
                        num_1 = random.randint(26, 42)
                        num_2 = random.randint(26, 42)
                        if int(quant) == 6:
                            while num_1 % 10 == 0 or 500 > num_1 * num_2 > 1100:
                                num_1 = random.randint(26, 42)
                            while num_2 % 10 == 0 or 500 > num_1 * num_2 > 1100:
                                num_2 = random.randint(26, 42)
                        if int(quant) == 7:
                            while num_1 % 10 == 0 or 600 > num_1 * num_2 > 1100:
                                num_1 = random.randint(26, 42)
                            while num_2 % 10 == 0 or 600 > num_1 * num_2 > 1100:
                                num_2 = random.randint(26, 42)
                        if 10 > int(quant) >= 8:
                            while num_1 % 10 == 0 or 700 > num_1 * num_2 > 1300:
                                num_1 = random.randint(26, 42)
                            while num_2 % 10 == 0 or 700 > num_1 * num_2 > 1300:
                                num_2 = random.randint(26, 42)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if int(quant) >= 10:
                        print('десятый - двадцать пятый пример')
                        num_1 = random.randint(44, 69)
                        num_2 = random.randint(44, 69)
                        while num_1 % 10 == 0 or num_1 * num_2 < 1600:
                            num_1 = random.randint(44, 69)
                        while num_2 % 10 == 0 or num_1 * num_2 < 1600:
                            num_2 = random.randint(44, 69)
                        example = f'{num_1} * {num_2}'
                        result = num_1 * num_2
                        time.sleep(3)

                    if quant > quant_nd:
                        print('тренировка закончилась')
                        active = False
                        bot.send_message(callback.message.chat.id, 'Молодец! Тренировка закончилась')
                        bot.send_message(callback.message.chat.id, 'Вот твои результаты:')
                        bot.send_message(callback.message.chat.id, f'Ошибок: {errors}')
                        if errors != 0:
                            win_sticker = 'CAACAgIAAxkBAAJUgWVFItTcElyotiIzQOC-rTArAAGMeQACEwADwDZPE6qzh_d_OMqlMwQ'
                            bot.send_message(callback.message.chat.id, '\n'.join(example_error))
                            bot.send_sticker(callback.message.chat.id, win_sticker)
                        time.sleep(5)
                        bot.send_message(callback.message.chat.id,
                                         'Напиши /start, если захочешь снова начать тренировку')


# тренировка
@bot.message_handler(commands=['example'])
def main(message):
    global example
    global gen_example
    global result
    global gen_result
    print('генерируется пример')
    if example is not None:
        gen_result = result
        gen_example = example
        bot.send_message(message.chat.id, 'Генерирую пример..')
        bot.send_message(message.chat.id, f'{gen_example}')
    else:
        bot.send_message(message.chat.id, 'Пример еще не сгенерировался. Немного отдохните и нажмите '
                                          '/example через 2-3 секунды')


# обработка результата
@bot.message_handler(content_types=['text'])
def send_text(message):
    if active:
        print('происходит проверка')
        global gen_result
        global errors
        global quant
        global quant_nd
        global example
        global gen_example
        global example_error
        if message.text == str(gen_result):
            print("пользователь ответил верно")
            print(f"правильный ответ: {gen_result}")
            print(f"результат пользователя: {message.text}")
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(3)
            if quant != quant_nd:
                bot.send_message(message.chat.id, 'Напишите /example, чтобы получить следующий пример')
            example = None
            quant += 1
            print('прибавляется 1 решенный пример')
            print(f'количество примеров равно {quant}')

        elif message.text != str(gen_result):
            print('пользователь ошибся')
            print(f"правильный ответ: {gen_result}")
            print(f"результат пользователя: {message.text}")
            print(example_error)
            if example_error is None:
                example_error = []
            example_error.append(f'Ошибка {gen_example} ваш ответ {message.text}, правильный {gen_result}')
            errors += 1
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(3)
            if quant != quant_nd:
                bot.send_message(message.chat.id, 'Напишите /example, чтобы получить следующий пример')
            example = None
            quant += 1


keep_alive()
bot.polling()
