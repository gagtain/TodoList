from rest_framework.authentication import TokenAuthentication



class BotTokenAuthentication(TokenAuthentication):
    keyword = "EnvToken"