#kmh = int(input("Enter km/h: "))
#mph =  0.6214 * kmh
#print("Speed:", kmh, "KM/H = ", mph, "MPH")

question1= [{
'question': 'who is the president of the USA?',
'answers': ['Barack Obama','donald trump','Mike Pence','Joe Biden'],
'correct': 'donald trump'
}]


print(question1[0]['question'])
print(','.join(question1[0]['answers']))

guess= input()

if guess.lower() == question1[0]['correct']:
  print('correct')
#guess= input()
