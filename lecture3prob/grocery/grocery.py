d = {}

while True:
    try:
        grocery = input ("").upper()
        if grocery in d:
            d[grocery] += 1 #d[] gives the key a value, add 1 count if appeared before
        else:
            d[grocery] = 1 #if d[grocery] first appeared, give it 1 count
    except EOFError:
        print ()
        break
    except KeyError:
        pass

#sorted() by alphabetical order
#.items -> use to retrive key-value pairs from the dictionary
#so below can print out count, item
sort_dict = sorted(d.items())

#join and form new line for each output
#(f"{count} {item}" for item,count in sort_dict) is a generator expression
#.join can be used with iterable = generator expression
final_list = "\n".join(f"{count} {item}" for item,count in sort_dict)

print (final_list)
