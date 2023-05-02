def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        items.insert(1, 'and')
        string = ' '.join(items)
        return string
    else:
        new_items = ',  '.join(items).split('  ')
        new_items.insert(len(items) - 1, 'and')
        string = ' '.join(new_items)
        return string
