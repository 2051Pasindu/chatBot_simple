import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:   # checking every word by word
        if word in recognised_words:
            message_certainty += 1  # if the user entered word is in the recognised word set certain +1

    percentage = float(message_certainty) / float(len(recognised_words))    # Gives how much percentage is recognised from the user input

    for word in required_words:
        if word not in user_message:
            has_required_words = False  # This will prevent us wrongly matching a word
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #Responses-------------------------------------------------------------------------

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('I\'m fine, thank you', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Nice... Let\'s begin then !!!', ['i', 'love', 'to', 'code'], required_words=['love', 'code'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_GREET1(), ['nice', 'to', 'meet', 'you'], required_words=['nice', 'meet'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())    # splits all the words entered by the user separately and lowercase aall the letters of the user eneters
    response = check_all_messages(split_message)
    return response


#to always get new responses an infinite while loop

while True:
    print("Bot: " + get_response(input("You: ")))

