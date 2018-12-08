# Sarah Isaacs, Student 12, Assignment 5
print("Sarah Isaacs, Student 12")

friends = ['Jazmine', 'Mariana', 'Lauren', 'Alexis']
message = "I am friends with " + friends[0].title() + "."
print(message)
message = "I am friends with " + friends[1].title() + "."
print(message)
message = "I am friends with " + friends[2].title() + "."
print(message)
message = "I am friends with " + friends[3].title() + "."
print(message)

message = "I hope you have a good day, " + friends[0].title() + "."
print(message)
message = "I hope you have a good day, " + friends[1].title() + "."
print(message)
message = "I hope you have a good day, " + friends[2].title() + "."
print(message)
message = "I hope you have a good day, " + friends[3].title() + "."
print(message)

transportations = ['outback', 'camaro', 'jetta', 'bike']
message = "I would like to own a " + transportations[0].title() + "."
print(message)
message = "I would like to own a " + transportations[1].title() + "."
print(message)
message = "I would like to own a " + transportations[2].title() + "."
print(message)
message = "I would like to own a " + transportations[3] + "."
print(message)

guests = ['Kortney', 'Tyler', 'Shawn']
message = guests[0].title() + ", come to my dinner fest tonight."
print(message)
message = guests[1].title() + ", come to my dinner fest tonight."
print(message)
message = guests[2].title() + ", come to my dinner fest tonight."
print(message)

guests = ['Kortney', 'Tyler', 'Shawn', 'Chris']
print(guests)

too_busy = 'Shawn'
guests.remove(too_busy)
print(guests)
print("\n" + too_busy.title() + " is too busy to come over.")

guests = ['Kortney', 'Tyler', 'Shawn', 'Nick', 'Carlos']
print(guests)

guests[2] = 'Chris'
print(guests)

guests = ['Kortney', 'Tyler', 'Chris']
message = guests[0].title() + ", come to my dinner fest tonight."
print(message)
message = guests[1].title() + ", come to my dinner fest tonight."
print(message)
message = guests[2].title() + ", come to my dinner fest tonight."
print(message)

guests.insert(0, 'Nick')
guests.insert(0, 'Maria')
guests.insert(0, 'Angelica')
print(guests)

guests = ['Angelica', 'Maria', 'Nick', 'Kortney', 'Tyler', 'Chris']
guests_leaving = guests.pop(0)
guests = ['Angelica', 'Maria', 'Nick', 'Kortney', 'Tyler', 'Chris']
guests_leaving = guests.pop(1)
guests = ['Angelica', 'Maria', 'Nick', 'Kortney', 'Tyler', 'Chris']
guests_leaving = guests.pop(2)
guests = ['Angelica', 'Maria', 'Nick', 'Kortney', 'Tyler', 'Chris']
guests_leaving = guests.pop(5)
print('Only Kortney and Tyler will be coming because, ' + guests_leaving + 'the others could not.')

places = ['Ireland', 'Scotland', 'Japan', 'Britain', 'New Zealand']
places.sort()
print(places)
places.sort(reverse=True)
print(places)

places = ['Ireland', 'Scotland', 'Japan', 'Britain', 'New Zealand']
print(places)
places.reverse()
print(places)

guests = ['Angelica', 'Maria', 'Nick', 'Kortney', 'Tyler', 'Chris']
len(guests)