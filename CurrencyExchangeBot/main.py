import telebot
from config import Backyard as by
from extensions import API, APIException

bot = telebot.TeleBot(by.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, by.TEXT_HELLO, parse_mode="html")


@bot.message_handler(commands=['help', 'помощь', '?'])
def help(message):
    bot.send_message(message.chat.id, by.TEXT_HELP, parse_mode="html")


@bot.message_handler(commands=['BOT'])
def example(message):
    bot.send_message(message.chat.id, 'Например:\nдоллар рубль 100')


@bot.message_handler(commands=['values', 'валюты', '!'])
def values(message):
    text = 'Список конвертируемых валют:'
    for num, key in enumerate(by.KEYS, 1):
        text += f'\n{num:>3}.  {key:20} {by.KEYS[key][1]:<20}'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        text_msg = message.text.lower().replace(',', '.')
        msg_list = text_msg.split(' ')
        if len(msg_list) != 3:
            raise APIException('Неверное число аргументов\n     /BOT как надо')
        quote, base, amount = msg_list
        if float(amount) < 0:
            raise APIException('Количество должно быть положительным числом!')
        if quote == base:
            raise APIException('Нельзя конвертировать валюту саму в себя!')
        try:
            quote in by.KEYS[quote][0]
        except KeyError:
            raise APIException(f'Я не знаю валюту "{quote.upper()}".\n'
                               f'Смотри список допустимых валют /values')
        try:
            base in by.KEYS[base][0]
        except KeyError:
            raise APIException(f'Я не знаю валюту "{base.upper()}".\n'
                               f'Смотри список допустимых валют /values')
    except APIException as error:
        bot.reply_to(message, f'Ошибка:\n{error}')
    except ValueError:
        bot.reply_to(message, f'Неправильный ввод данных')
    else:
        rate, sum_money = API.get_price(base, quote, amount)
        text = f'По состоянию на сегодня, <i>{by.date}</i>,\nкурс составил:  {rate} ' \
               f'{by.KEYS[base][0].lower()}\n{"_" * 40}\n{amount} {by.KEYS[quote][0].lower()}' \
               f' = <b>{round(float(sum_money), 2)}</b> {by.KEYS[base][0].lower()}'
        bot.send_message(message.chat.id, text, parse_mode="html")

bot.polling(none_stop=True)
