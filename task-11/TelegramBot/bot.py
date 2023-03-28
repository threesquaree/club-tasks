import os
import random
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Alright, let's start playing Rock, Papers and Scissors")

@bot.message_handler(func=lambda msg: True)
def RPSGame(message):
   player = message.text

   if(player == "Rock" or player == "rock" or player == "ROCK"):
        bot.reply_to(message, "You chose Rock")
        bot.reply_to(message, "I chose Scissors")
        bot.reply_to(message, "You win!")
   elif(player == "Paper" or player == "paper" or player == "PAPER"):
        bot.reply_to(message, "You chose Paper")
        bot.reply_to(message, "I chose Rock")
        bot.reply_to(message, "You win!")
   elif(player == "Scissors" or player == "scissors" or player == "SCISSORS"):
        bot.reply_to(message, "You chose Scissors")
        bot.reply_to(message, "I chose Paper")
        bot.reply_to(message, "You win!")
   else:
        bot.reply_to(message, "I don't understand")
        bot.reply_to(message, "Try again")
        bot.reply_to(message, "Rock, Paper or Scissors?")

if __name__ == '__main__':
    bot.infinity_polling()