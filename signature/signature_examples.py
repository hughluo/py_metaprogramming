from signature import Structure, add_signature


class SpamTheOldWay:
    def __init__(self, name, price):
        self.name = name
        self.price = price


@add_signature("name", "price")
class Spam(Structure):
    pass


if __name__ == "__main__":
    spam_0 = Spam(price=0.618, name="wexort")
    print(spam_0.name, spam_0.price)
    spam_1 = Spam("hughluo", 42)
    print(spam_1.name, spam_1.price)
