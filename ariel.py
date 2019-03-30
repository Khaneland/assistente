import wolframalpha

input = raw_input("Pergunta: ")
app_id = "5395J6-5WTJ3AGLKT"
Client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.result).text

print answer