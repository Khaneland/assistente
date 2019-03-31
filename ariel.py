import wikipedia
import wolframalpha

while True:
    input = raw_input ("Q: ")
    
    try:
        #wolframalpha
        app_id = "5395J6-5WTJ3AGLKT"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.result).text
        print answer
    except:
        #wikipedia
        print.wikipedia.summary(input)