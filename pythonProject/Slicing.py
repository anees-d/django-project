# slicing = create a substracting by extracting elements from another string

name = "Bro Code"

first_name = name[0:3]
last_name = name[4:]
funkey_name = name[0:8:2]   #[start, stop, step]
test = name[::3]
reversed_name = name[::-1]

print(funkey_name)
print(first_name)
print(last_name )
print(test)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"


slice = slice(7,-4)
print(website1[slice])
print(website2[slice])