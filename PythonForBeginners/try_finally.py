try:
    stream = open('output.txt', 'wt')
    stream.write('Lorem Ipsum Dolor')
finally:
    stream.close # VERY IMPORTANT!
    