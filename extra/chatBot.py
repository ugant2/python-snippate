chat_bot = []

while True:
    text = input("submit your thoughts(Press x or X to quit)")
    if text == 'x' or text == 'X':
        break
    chat_bot.append(text)

print(chat_bot)