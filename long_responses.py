import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"


def R_GREET1():
    response = ["Wow, I'm glad! Nice to meet you too",
                "Yeah buddy!!... That\'s what I\'m talking about!!",
                "Ma Man...",
                "I..C..E.. TO SEE UU..",
                "Asta Lavista Baby!!"][random.randrange(5)]
    return response


def unknown():
    response = ['Could you please re-phrase that',
                "...",
                "Sounds about right",
                "What does that mean"][random.randrange(4)]
    return response