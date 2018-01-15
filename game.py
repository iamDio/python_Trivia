questions= [
  {
'question': 'who is the president of the USA?',
'answers': ['Barack Obama','donald trump','Mike Pence','Joe Biden'],
'correct': 'donald trump'
},
{'question': 'Who is the quarterback for the New England Patriots?',
'answers': ['Peyton Manning','Chad Pennington','tom brady','Mark Sanchez'],
'correct': 'tom brady'
},
{'question': 'Who wrote hamlet?',
'answers': ['George Orwell','Elton Jon','William Shakespeare','Mark Twain'],
'correct': 'william shakespeare'
}
]

for i,d in enumerate(questions):
  print(d['question'])
  print(','.join(d['answers']))
  guess= input()
  if guess.lower() == questions[i]['correct']:
     print('correct')
  else:
    print('incorrect answer!!!')



