from gtts import gTTS
import os

quotes = '''Stay committed to your goal; success doesn't come overnight.

Struggle leads to capability, In challenges, opportunities arise.

Change according to your dreams; if not, the world will change you.

Failure is temporary; success comes gradually.

Trust in your abilities and courage; you have the power to shape your own destiny.

Positive thoughts open new perspectives and pave the way for a new journey.

Success is in dedication and perseverance; failure is not the end but a lesson.

Aim for complete fulfillment in your goals; small goals lead to significant outcomes.

Every defeat is an opportunity for a new effort.

Your hard work and dedication hold the key to realizing your dreams'''


def play_sound(text):
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save("sound.mp3")
    os.system("mpg321 sound.mp3")
    os.remove("sound.mp3")


quotes_list = quotes.replace("\n", "").split(".")
for quote in quotes_list:
    play_sound(quote)
