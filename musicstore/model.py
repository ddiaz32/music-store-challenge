from datetime import datetime

# TODO: Add code here

class Transaction:
    SELL = 1
    SUPPLY = 2

    def __init__(self, type: int, copies: int):
        self.type = type
        self.copies = copies
        self.date = datetime.now()


class Disc:
    def __init__(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        self.sid = sid
        self.title = title
        self.artist = artist
        self.sale_price = sale_price
        self.purchase_price = purchase_price
        self.quantity = quantity
        self.transactions = []
        self.song_list = []

    def add_song(self, song: str):

        if song not in self.song_list:
            self.song_list.append(song)

    def sell(self, copies: int) -> bool:
        if copies > self.quantity:
            return False
        
        self.quantity -= copies

        transaction = Transaction(Transaction.SELL, copies)
        self.transactions.append(transaction)
        return True 

    def supply(self, copies: int):
        self.quantity += copies
        transaction = Transaction(Transaction.SUPPLY, copies)
        self.transactions.append(transaction)

    def copies_sold(self) -> int:
        total_sold = 0

        for transaction in self.transactions:
            if transaction.type == Transaction.SELL:
                total_sold += transaction.copies

        return total_sold



    
        

    

    

    







        



    


    
