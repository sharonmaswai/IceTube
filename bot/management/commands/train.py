from django.core.management.base import BaseCommand
import os
class Command(BaseCommand):

	'''
	A django management command for calling a chatbots training method
	'''

	help = 'Trains the database used by the chat bot'
	can_import_settings = True

	def handle(self, *args, **options):
		from chatterbot import ChatBot 
		from chatterbot.ext.django_chatterbot import settings 
		from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

		chatbot = ChatBot(
		    'IcedKonnect',
		    trainer='chatterbot.trainers.ListTrainer',
		    storage_adapter='chatterbot.storage.SQLStorageAdapter',
		    database_uri='sqlite:///database.sqlite3',
		)
		trainer=ListTrainer(chatbot)
		trainer.train([
				"Hallo",
			    "Hi, can I help you?",
			    "I have an issue with my crops",
			    "Click  here to get assistance http://127.0.0.1:8000/profile/"
			])
		

		if hasattr(self.style, 'SUCCESS'):
			style = self.style.SUCCESS
		else:
			style = self.style.NOTICE

		self.stdout.write(style('Starting training...'))
		training_class = trainer.__class__.__name__
		text='ChatterBot trained using {tc}'.format(tc=training_class)
		self.stdout.write(style(text))
