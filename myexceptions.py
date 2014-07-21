class AuthenticationException(Exception):
    """
        authentication related exceptions
    """
    def __init__(self, message_text):
        self.message_text = message_text

    def get_message(self):
        return self.message_text
