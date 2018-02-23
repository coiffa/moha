"""
This is basically practicing some python ~
atm.py
contains ATM class
"""
class ATM:
    """
    initializes atm objcet. Can withdraw money
    """
    def __init__(self, bank_name, balance):
        self._withdrawals_list = []
        self._deposits_list = []
        self._balance = balance
        self._bank_name = bank_name
        print "atm for: ({}) initialized successfully with balance: ({}).\n".format(self._bank_name, self._balance)

    def deposit(self, request):
        """
        add request to balance
        """
        self._balance += request
        self._deposits_list.append(request)
        print "added {} successfully.\n".format(request)

    def withdraw(self, request):
        """
        prints banknote value returned by atm for a request if atm has money
        this works with INTGERS ONLY
        returns the rest of money in balance
        """
        # local variables
        accepted_notes = [100, 50, 10, 5, 1]

        # validating input
        if not type(request) == type(1):
            raise Exception("request must be an INTGER")
        if not request < self._balance:
            raise Exception("atm doesn't have enough money")

        print "============================"
        print "Welcome to {} atm".format(self._bank_name)
        print "Current balance:", self._balance
        print "Withdraw Value:", request
        print "============================"

        # updating variables
        self._balance -= request
        self._withdrawals_list.append(request)

        # main loop
        for note in accepted_notes:
            while request >= note:
                request -= note
                print "give", note

        print "============================"
        print "balance after withdraw:", self._balance
        print "============================\n"

    def show_withdrawals(self):
        for withdrawal in self._withdrawals_list:
            print(withdrawal)

    def show_deposits(self):
        for deposit in self._deposits_list:
            print(deposit)