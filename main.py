import telebot
import sqlite3

db = sqlite3.connect("Server.db", check_same_thread=False)
sql = db.cursor()

sql.execute(
    """
    CREATE TABLE IF NOT EXISTS telegram_users (
    user_ID INT,
    user_firstname TEXT,
    user_lastname TEXT

    )
    """
)
db.commit()
bot = telebot.TeleBot("5588570551:AAHWgQOIoHj2KIaBsRYbzsH4IOPc_VOGhwA")


persons = dict()


class User:
    def __init__(self, user_id, first_name, last_name) -> None:
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def getData(self):
        return f"FirstName: {self.first_name}\nLastName: {self.last_name}"

    def addtoDB(self):
        if sql.fetchone() is None:
            sql.execute(
                "INSERT INTO telegram_users VALUES (?,?,?)",
                (self.user_id, self.first_name, self.last_name),
            )
            db.commit()
        else:
            pass


@bot.message_handler(commands=["start"])
def start(message):
    newUser = User(
        message.from_user.id, message.from_user.first_name, message.from_user.last_name
    )
    newUser.addtoDB()

    mess = f"Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


# @bot.message_handler()
# def get_user_texxt(message):
#     if message.text == "hello":
#         bot.send_message(message.chat.id, "Hi, bro!", parse_mode="html")
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Your id: {message.from_user.id}")


@bot.message_handler(commands=["person"])
def get_stored_data(message):
    for value in sql.execute("SELECT * FROM telegram_users"):
        bot.send_message(message.chat.id, value[2])


bot.polling(non_stop=True)
