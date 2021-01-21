#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import environ

from telegram.ext import Updater, MessageHandler, CommandHandler, \
    Filters, CallbackQueryHandler, ConversationHandler, \
    InlineQueryHandler

# Registro de actividades
import logging


class BotTelegram:
    """Clase base para crear instancias de un Bot de Telegram

        >>> MiBot = BotTelegram(token)

    """
    PORT = environ.get('PORT', 5000)

    def __init__(self, token, webhook=False, url=''):
        self.updater = Updater(token=token, use_context=True)
        # Dispatcher: está al pendiente de todas las ventanas donde se encuentra el bot.
        self.dispatcher = self.updater.dispatcher
        if webhook:
            self.updater.start_webhook(listen="0.0.0.0",
                                       port=int(self.PORT),
                                       url_path=token)
            self.updater.bot.setWebhook(url + str(token))
        else:
            self.updater.start_polling()

    def wait_for_command(self, command, function):
        self.dispatcher.add_handler(CommandHandler(command, function))

    def answer_query_with(self, function, pattern=None):
        self.dispatcher.add_handler(CallbackQueryHandler(function, pattern=pattern))

    def answer_message_with(self, funcion):
        self.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), funcion))

    def answer_inline_mode(self, command, pattern=None):
        self.dispatcher.add_handler(InlineQueryHandler(command, pattern=pattern))

    def generate_user_id(self, update):
        try:
            chat_id = update.callback_query.message.chat_id
        except AttributeError:
            try:
                chat_id = update.message.chat_id
            except AttributeError:
                try:
                    chat_id = update.inline_query.from_user.id
                except AttributeError:
                    chat_id = update.callback_query.from_user.id
        return chat_id

    def generate_message_id(self, update):
        try:
            message_id = update.callback_query.message.message_id
        except AttributeError:
            try:
                message_id = update.message.message_id
            except AttributeError:
                try:
                    message_id = update.inline_query.from_user.message_id
                except AttributeError:
                    message_id = update.callback_query.inline_message_id
        return message_id
