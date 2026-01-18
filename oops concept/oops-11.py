'''
Abstraction : hiding the internal implementation and showing only the essential features to the user.
abstraction is typically implemented using abstract classes and methods via the abc module.

key Point :
1.To hide complex logic from the user
2.To enforce a blueprint for subclasses
3.To improve maintainability and security 
4.Abstract classes cannot be instantiated directly.
5.Any subclass must implement all abstract methods.
6.Useful when you want to define a contract or interface for subclasses.

Abstract Class: A class that cannot be instantiated directly and is meant to be inherited by other classes.

Abstract Method: A method declared but not implemented in the abstract class; child classes must implement it.

'''

from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def Pay(self,amount):
        pass


class CreditPayment(Payment):
    def Pay(self, amount):
        return print(f"Processing credit card payment of ₹{amount}")

class PaypalPayment(Payment):
    def Pay(self, amount):
        return print(f"Processing Paypal payment of ₹{amount}")
    

class UpiPayment(Payment):
    def Pay(self, amount):
        return print(f"Processing UPI payment of ₹{amount}")
    
def process_payment(payment_method: Payment, amount: float):
    payment_method.Pay(amount)

creadit = CreditPayment()
paypal = PaypalPayment()
upi = UpiPayment()

process_payment(creadit, 1000)
process_payment(paypal, 5000)
process_payment(upi, 100)