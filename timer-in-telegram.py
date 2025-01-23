import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


def start_timers(chat_id, question):
    message_id = bot.send_message(chat_id, "Сейчас пойдёт!!")
    bot.create_countdown(
        parse(question),
        send_update_message,
        chat_id=chat_id,
        message_id=message_id,
        question=question,
    )
    bot.create_timer(
        parse(question),
        send_finish_message,
        chat_id=chat_id,
        question=question
    )


def send_finish_message(chat_id, question):
    message = ("Время вышло!")
    bot.send_message(chat_id, message)


def send_update_message(secs_left, chat_id, message_id, question):
    count = -secs_left + parse(question)
    progressbar = render_progressbar(parse(question), count)
    bot.update_message(
        chat_id, 
        message_id, 
        f"Осталось {secs_left} секунд! \n{progressbar}"
    )


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    load_dotenv()
    TG_TOKEN = os.getenv('TG_TOKEN')
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(start_timers)
    bot.run_bot()
