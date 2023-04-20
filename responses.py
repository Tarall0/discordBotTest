import random
import numpy as np


def handle_response(message) -> str:
    p_message = message.lower()

    if "ciao" in str(p_message):
        greetings = np.array(["Hey 👋", "Hey!", "Ciao!", "Ciao ❤️", "01101001 ... Whoops scusate, a volte dimentico "
                                                                         "di chattare con umani!"])
        random_var = random.randint(0, 4)
        return greetings[random_var]

    if p_message == '!help':
        return "`👨‍💻 This python bot is currently under developement. Its creation is for testing and educational purposes`"

    if p_message == '!quote':
        return "`Quote of the day lol`"

    if p_message == '!weed':
        gif_list = np.array(["https://media.tenor.com/GGsZ7_cG2bAAAAPo/smoke-cigarettes.gif",
                             "https://media.tenor.com/YVIh-tjCWFEAAAPo/high-guy.gif",
                             "https://media.tenor.com/8LSToAJJFSsAAAPo/smoke-weed.gif"])
        random_var = random.randint(0, 2)
        return gif_list[random_var]

    if p_message == '!666':
        return 'https://media.tenor.com/GnI3700srpAAAAAC/elrond-network-egld.gif'

    if "love" in str(p_message):
        return "love u"

