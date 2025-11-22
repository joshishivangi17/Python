#Nesting
book = {}
print(book)
book['name'] = 'The secret'
book['price'] = 400
book['chapters'] = (1,2,3,4)
book['topics'] = ['introduction','what is secret','about author','summery']
print(book)
book['topics'][0] = 'index'
print(book)






























