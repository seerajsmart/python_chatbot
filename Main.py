import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response = False, required_words=[]):
    message_cetrtainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_cetrtainty += 1

            #Calculates the percent in each predefined message
            percentage = float (message_cetrtainty) / float(len(recognised_words))

            for word in required_words:
                if word not in user_message:
                    has_required_words = False
                    

def get_response(user_input):
    spilt_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages (spilt_message)
    return response


#Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))

    


    


 















