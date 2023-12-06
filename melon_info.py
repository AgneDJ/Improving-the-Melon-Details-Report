"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(name, price, seedless, flesh_color=None, rind_color=None, average_weight=None):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s flesh: {flesh_color} \n rind: {rind_color} \n weight {average_weight} \n {have_or_have_not} seeds and are ${price}')


for i in melons:
    print_melon(i, melons[i]["price"], melons[i]["seedlessness"],
                melons[i]["flesh_color"], melons[i]["rind_color"], melons[i]["average_weight"])
