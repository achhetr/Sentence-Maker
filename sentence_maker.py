# global variable of list sentence
sentence = []

# find out whether statement is a question
def add_question_mark(phrase):
    question = ("how","when","what","where","who","whom","why","which",'whose')
    for q in question:
        if phrase.find(q) != -1:
            return "%s?" % (phrase)
    return "%s." % (phrase)

# take list and return report
def list_to_report(phrase):
    '''This function returns after joining list'''
    return " ".join(phrase)


# main script
while(True):
    # input sentance from user
    say_something = input("Say something: ")

    # break the loop if '/end' is entered
    if say_something == '/end':
        break
    
    # adding to list after capitalize
    sentence.append(add_question_mark(say_something).capitalize())

print(list_to_report(sentence))