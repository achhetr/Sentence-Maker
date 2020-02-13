sentance = ''
question = ("how","when","what","where","who","whom","why","which",'whose')
while(True):
    # input sentance from user
    say_something = input("Say something: ")

    # break the loop if '/end' is entered
    if say_something == '/end':
        break
    
    # find out whether statement is a question
    sign = '.'
    for q in question:
        if say_something.find(q) != -1:
            sign = '?'
    
    sent = "%s%s%s " % (sentance,say_something.capitalize(),sign)

print(sent)