import sys

def tip():
    print('How much is your meal? :')
    price = int(sys.stdin.readline())
    print("How much to you want to Tip them? :")
    tip = int(sys.stdin.readline())
    final_tip_amt = price*(tip/100)
    print('You will want to tip them %s'%final_tip_amt + 'Dollars')
