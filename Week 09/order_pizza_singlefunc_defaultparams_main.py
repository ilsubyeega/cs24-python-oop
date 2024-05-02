PRICE_OF_TOPPING = 1.50


def order_pizza(size, style='regular', topping=None):
    if size == 'small':
        price = 10.00
    elif size == 'medium':
        price = 14.00
    else:
        price = 18.00

    if style == 'deepdish':
        price = price + 2.00

    line = 'You have ordered a ' + size + ' ' + style + ' pizza with '
    if topping is None:
        print(line + 'no topping')
    else:
        print(line + topping)
        price = price + PRICE_OF_TOPPING

    print(f'The price is ${price}.')
    print()


order_pizza('large')

order_pizza('large', style='regular')

order_pizza('medium', style='deepdish', topping='mushrooms')

order_pizza('small', topping='mushrooms')
