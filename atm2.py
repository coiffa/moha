def ATM(money, requests):
    for request in requests:
        if request > money:
            print("please check your request")
        elif request < 0:
            print("please check your request")
        else:
            money = cash(request, money)
        print("Current balance : " + str(money))


def cash(request, money):
    while request > 0:
        if request >= 100:
            print("give 100")
            request -= 100
            money = money - 100
        elif request >= 50:
            print("give 50")
            request -= 50
            money = money - 50
        elif request >= 10:
            print("give 10")
            request -= 10
            money = money - 10
        elif request >= 5:
            print("give 5")
            request -= 5
            money = money - 5
        elif request >= 2:
            print("give 2")
            request -= 2
            money = money - 2
        else:
            print("give " + str(request))
            money = money - request
            request = 0
    print("================")
    return money


money = 500
requests = [1000, 227, 10, 900, -10, 50, 100, 140, 113]
ATM(money, requests)