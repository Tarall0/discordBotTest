import random
import numpy as np


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'ciao' or p_message == 'salve' or p_message == 'buonasera' or p_message == 'we' or p_message == 'hey':
        greetings = np.array(["Ciao 👋", "Ehilà fattone!", "Hai già rollata il tuo joint prima di scrivere?", "Ciao ❤️",
                              "01101001 ... Whoops scusate... "
                              "Ciao!",
                              "Perché la marijuana è illegale? Cresce naturalmente sul nostro pianeta. L'idea di "
                              "rendere la natura illegale non vi sembra un po'... innaturale?"])
        random_var = random.randint(0, 4)
        return greetings[random_var]

    if p_message == 'love u tarallo' or p_message == 'love tarallo':
        return 'Yes we love tarallo :heart:'

    if p_message == '!rank':
        return "athena n'agg capit c vuo fa co u !rank"

    if p_message == '!help':
        return "`👨‍💻 This python bot is currently under developement. Its creation is for testing and educational " \
               "purposes`"

    if p_message == '!quote':
        quotes = np.array(["`“Perché bere e guidare quando puoi fumare e volare?”\r\r- Bob Marley`",
                           "`“L'erba è come la frutta. Ti mantiene in forma e ti libera la mente.”\r\r- Bob Marley`",
                           "`“Meno Gesù più Maria.”`",
                           "`“L'erba cattiva non muore mai, l'erba buona finisce subito.”`"])
        random_quote = random.randint(0, 3)
        return quotes[random_quote]

    if p_message == '!random':
        test_array = np.array(["Ciao", "Test", "Test2", "Test2", "test3"])
        random_var = random.randint(0, 4)
        return test_array[random_var]

    if p_message == '!weed':
        gif_list = np.array(["https://media.tenor.com/GGsZ7_cG2bAAAAPo/smoke-cigarettes.mp4",
                             "https://media.tenor.com/YVIh-tjCWFEAAAPo/high-guy.mp4",
                             "https://media.tenor.com/8LSToAJJFSsAAAPo/smoke-weed.mp4"])
        random_var = random.randint(0, 2)
        return gif_list[random_var]

    if p_message == '!666':
        return 'what?'
