def get_price(is_vip):
    if is_vip == True:
        return 10000
    else:
        return 15000

price = get_price(True)
price(f'커트 가격은 {price}원 입니다.')
price = get_price(False)
price(f'커트 가격은 {price}원 입니다.')    