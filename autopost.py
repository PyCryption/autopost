from telethon.sync import TelegramClient, events
import asyncio
import logging

api_id = 29725939
api_hash = '1562de0630b4e8734d746a0ed037963a'
mychan = -1001843145329
channels = [-1001422173447, -1001582794312, -1001474692357, -1001637808937, -1001689202235, -1001485321811, -1001583082275, -1001235272807, -1001481743976, -1001410755300, -1001348255490, -1001711197908, -1001766543888, -1001908862660, -1001511957114, -1001711197908, -1001902745157, -1001456762552, -1001645887804, -1001514736608, -1001560872857, -1001237848972, -1001776358085]

client = TelegramClient('negri', api_id, api_hash)
print("[+] activate")

def to_lower(word: str):
    return word.lower()

badtext_words = {'bam', 'Доступ', 'канал', 'БЕСПЛАТНЫЙ', 'Бесплатно', 'Заливают', 'ДОСТУП', 'доступ', 'поиск', 'Поиск', 'ЖМИ', 'жми', 'ссылку', 'Смотри', 'тут', 'Слитый', 'архив', 'Искали', 'фулл?', 'залетай', 'Даю', 'ссылку', 'Проверь', 'подругу', 'Слив', 'шкур', 'бот', 'Telegram', 'ИНТИМ', 'ПОИСК', 'Приватный', 'контент', 'Подруга', 'Держи', 'ссылку', 'Подборки', 'Фулл', 'закрепе', 'Чат', 'Доступ', 'приватный', 'канал', 'Вписки', 'Пароль', 'PormHub', 'Полное', 'видео', 'Зайди', 'Смотреть', 'Тут', 'сливают', 'Архив', 'Места', 'Нашли', 'сексе', 'секс', 'обувь', 'Больше', 'тут', 'Больше', 'тут', 'ЭФИР', 'Секретные', 'Нате', 'Сборка', 'бесплатный', 'кончай', 'удалю', 'Заработал', 'Ссылка', 'Приватные', 'ПОРНО', 'Каналы', 'Ссылки', 'Залили', 'ОП', 'Канала', 'Бесплатные', 'ПОРН0', 'Активны', 'ССылка', 'наигру', 'Читать', 'далее', 'Читать', 'Лучшие', 'промокод', 'Внимание', 'Новый', 'Переходи', '#реклама', 'ссылке', 'для', 'Подписывайся', 'Надоело', 'канале', 'нашем', 'мемы', 'Такое', 'увидишь', 'подписаться', 'Лижет', 'фото', 'фотки', 'больше', 'еще', 'больше', 'подписчиками', 'цена', 'дешево', 'покупай', 'присоединяйся', 'телеграм', '2023', 'сюда', 'сестру', 'разденет', 'посмотреть', 'покупателей', 'город', 'городе', 'довольных', 'городе', 'Тысячи', 'уже', 'твоем', 'тысячи', 'тысяча', 'переплатой', 'оригинал', 'дешевле', 'других', 'кроссовки', 'ставки', 'спорт', 'казино', 'попробуй', 'нашла', 'полное', 'обмен', 'фуллы', 'домашка', 'сношу', 'нахуй', 'оставляю', 'нейронка', 'голенькими', '100%'}
logging.basicConfig(level=logging.INFO, filename='logs.txt', filemode='a')
logger = logging.getLogger()

@client.on(events.Album(chats=channels))
async def handler(event):
    message_text_lowered = event.raw_text.lower()
    found_word = next((word for word in badtext_words if word in message_text_lowered), None)

    if not found_word:
        try:
            await client.send_message(
                mychan,
                file=event.messages,
                message="🔥 Школьный Надзор 🔥\n https://t.me/+698KX7nr1GVlOGYx \n❤️ Купить приватку ❤️\n@GirlNadzor_bot"
            )
            logger.info("Сообщение успешно отправлено в канал.")
        except Exception as e:
            logger.error("Ошибка при отправке сообщения: %s", str(e))

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    message_text_lowered = event.raw_text.lower()
    found_word = next((word for word in badtext_words if word in message_text_lowered), None)

    if not found_word:
        try:
            if event.message.video and not event.grouped_id:
                await client.send_file(
                    mychan,
                    file=event.message,
                    caption="🔥 Школьный Надзор 🔥\n https://t.me/+698KX7nr1GVlOGYx \n❤️ Купить приватку ❤️\n@GirlNadzor_bot"
                )
                logger.info("Сообщение успешно отправлено в канал.")
        except Exception as e:
            logger.error("Ошибка при отправке сообщения: %s", str(e))

with client:
    client.run_until_disconnected()