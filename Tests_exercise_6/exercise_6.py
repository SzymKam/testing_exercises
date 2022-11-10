
class Config:
    DB_URL: str = 'DB_URL'
    DB_USERNAME: str = 'DB_USERNAME'
    DB_PASSWORD: str = 'DB_PASSWORD'
    OK_MSG: str = 'OK_MSG'
    NOK_MSG: str = 'NOK_MSG'


class DbHandler:
    @staticmethod
    def connect_to_database():
        return f"I am connecting to {Config.DB_URL} as {Config.DB_USERNAME} with pass: {Config.DB_PASSWORD}..."

    def show_msg_when_connected(self):
        return f"{Config.OK_MSG}"

    def show_msg_when_interrupted(self):
        return f"{Config.NOK_MSG}"
