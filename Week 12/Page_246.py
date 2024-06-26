import pygwidgets

BLACK = (0, 0, 0)

class DisplayMoney(pygwidgets.DisplayText):

    def __init__(self, window, loc, value=None,
                 fontName=None, fontSize=24, width=150, height=None, 
                 textColor=BLACK, backgroundColor=None,
                 justified='left', nickname=None, currencySymbol='$',
                 currencySymbolOnLeft=True, showCents=True, multiplier=1.0):

        self.currencySymbol = currencySymbol
        self.currencySymbolOnLeft = currencySymbolOnLeft
        self.showCents = showCents
        self.multiplier = multiplier
        if value is None:
            value = 0.00

        super().__init__(window, loc, value, fontName, fontSize,
                            width, height, textColor, backgroundColor,
                            justified, nickname)

    def setValue(self, money):
        if money == '':
            money = 0.00

        money = float(money)
        
        money *= self.multiplier

        if self.showCents:
            money = '{:,.2f}'.format(money)
        else:
            money = '{:,.0f}'.format(money)

        if self.currencySymbolOnLeft:
            theText = self.currencySymbol + money
        else:
            theText = money + self.currencySymbol

        super().setValue(theText)