"""This file should have our melon-type classes in it."""
# default price = $5
# casabas and ogen += $1
# if imported = 1.5x more
# if square = 2x more
# Deal: 3 or more Wmelons = 0.75x
# Deal: 5 or more Cant = 0.5x

class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        # TODO, calculate the real amount!
        total = qty * 5.00
        if qty >= 3:
            total *= 0.75

        return total

        
class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        # TODO, calculate the real amount!
        total = qty * 5.00
        if qty >= 5:
            total *= 0.5

        return total

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        # TODO, calculate the real amount!
        total = (qty * (5.00 + 1.00)) * 1.50
       
        return total

class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        # TODO, calculate the real amount!
        total = (qty * 5.00) * 1.50
       
        return total

class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        # TODO, calculate the real amount!
        total = (qty * 5.00) * 1.50
       
        return total

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        # TODO, calculate the real amount!
        total = qty * 5.00
       
        return total

class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        # TODO, calculate the real amount!
        total = qty * 5.00
        
        if self.imported == True:
            total *= 1.5
        
        return total

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        # TODO, calculate the real amount!
        
        total = qty * 5.00
  
        if self.imported == True:
            total *= 1.50

        if self.shape == "square":
            total *= 2.00
        
        return total

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        # TODO, calculate the real amount!
        total = qty * 5.00
        
        if self.imported == True:
            total *= 1.50

        if self.shape == "square":
            total *= 2.00
        
        return total

        # if self.name == "Casaba" or self.name == "Ogen":
        # qty += 1.00