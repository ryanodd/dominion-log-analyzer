# a value (with any type), and a collection of messages accompanying that value to be seen on frontend.
# This will probably get bigger
class ValueReport:
    def __init__(self, value, messages):
        self.value = value
        self.messages = messages
