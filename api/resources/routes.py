from .chatgpt import chatGPT


def initialize_routes(api):
    api.add_resource(chatGPT, "/chatgpt")