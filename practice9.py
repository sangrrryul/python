yellow_card = 1
foul = True
if foul:
    yellow_card += 1
    if yellow_card == 2:
          print('경고 누적 퇴장')
    else:
          print('휴..조심해야지')
else:
    print('주의')          