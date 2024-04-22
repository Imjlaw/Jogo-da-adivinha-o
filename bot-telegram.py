import telegram
from telegram.ext import Updater, MessageHandler, filters

# Token
TOKEN = '7018759271:AAGw6hjJEHTE3145VxtNKE6wqG3PeSilmuE'

# IDs dos canais de origem e destino
CANAL_ORIGEM_ID = -1002039397419
CANAL_DESTINO_ID = -1002123195016

# Inicialização do bot
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)

# Função para manipular mensagens recebidas
def handle_message(upadte, context):
    message = updater.message
    if message.chat_id == CANAL_ORIGEM_ID:
        # Extrair texto e imagem da mensagem
        text = message.text
        photo = message.photo[-1] if message.photo else None

        # Modificar o texto conforme necessário (substitua esta parte com sua lógica de modificação)
        # Aqui você pode chamar a função que modifica o texto usando o GPT ou qualquer outra lógica desejada
        new_text = "Texto modificado: " + text
        
        # Enviar a mensagem modificada para o canal de destino
        if photo:
            context.bot.send_photo(chat_id=CANAL_DESTINO_ID, photo=photo.file_id, caption=new_text)
        else:
            context.bot.send_message(chat_id=CANAL_DESTINO_ID, text=new_text)

# Adicionar um manipulador de mensagens
updater.dispatcher.add_handler(MessageHandler(Filters.Text | Filters.photo, handle_message))

# Iniciar o bot
updater.start_polling()
updater.idle()
