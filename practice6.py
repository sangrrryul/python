person = {'이름':'김상률','나이':33,'키':174}
# print(person['나이'])
# print(person['키'])
# print(person['이름'])
# #print(person['별명'])
# print(person.get('별명'))
# print(person.get('이름'))

print(person)
person['최종학력'] = '유치원'
# print(person)
# person['키']=160
# print(person)
person.update({'키':176, '최종학력':'대학교'})
print(person)
person.pop('나이')
print(person)
#person.clear()
#print(person)
print(person.keys())
print(person.values())
print(person.items())