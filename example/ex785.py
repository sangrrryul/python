# drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']
# for x in drama:
#     if x == '시즌3':
#         print('재미없대, 그만보자')
        #   break
#     print(f'{x} 시청')

#1----------------------------------------------
# drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']
# for x in drama:
#     if x == '시즌3':
#         print('재미없대, 건너뛰자')
#         continue
#     print(f'{x} 시청')

#ex804
for x in range(11):
    if x % 2 == 1:
       continue   
    print(x)