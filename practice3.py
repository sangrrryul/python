s='나도고등학교'
print(s.startswith('나도'))
print(s.endswith('초등학교'))
print(s.endswith('고등학교'))

s='...나도고등학교...'
print(s.strip('.'))

s='나도고등학교'
print(s.replace('고등학교','고교'))

s='나도고교너도고교'
print(s.replace('고교','고등학교'))

s='나도고등학교'
print(s.find('학교'))
print(s.find('너도'))
print(s.center(10,'-'))