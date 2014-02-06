import re
from plugin import Plugin

class CloudToButt():
    def __init__(self, skype):
        self.replacements = {"cloud": "butt", "Cloud": "Butt", "Butt":"Cloud", "butt": "cloud", "the cloud": "my butt", "The cloud": "My butt"}

    def message_received(self, msg, status):

        text = msg.Body
        if "cloud" in text.lower() or "butt" in text.lower():
            newText = self.multiple_replace(self.replacements, text)
            msg.Chat.SendMessage(newText)

    def multiple_replace(self, dict, text):
        regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
        return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)