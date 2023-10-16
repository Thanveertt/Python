colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print('Black' in colours)
colours.append('Black')
colours.append('White')
print('Black' in colours)
more_colours = ['Gray', 'Navy', 'Pink']
colours.extend(more_colours)
print(colours)
