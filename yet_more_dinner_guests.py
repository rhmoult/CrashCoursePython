guests = ['Alice Cooper', 'Vincent Price', 'Bela Lugosi', 'Stan Lee']

print(f"{len(guests)} guests invited!")
for guest in guests:
    print(f"Welcome to the party, {guest}!")

user_who_cancelled = guests.pop()

guests.append('H.P. Lovecraft')

print(f"{len(guests)} guests invited!")
print(f"Unfortunately, {user_who_cancelled} can't make it to the party.")

for guest in guests:
    print(f"Thanks for being here, {guest}!")

print("I found a larger table, so we can invite more guests!")

guests.insert(0, 'Frankenstein')
guests.insert(2, 'Dracula')
guests.append('The Mummy')

print(f"{len(guests)} guests invited!")
for guest in guests:
    print(f"Welcome to the party, {guest}!")

print("Oh my goodness!  I can only invite two people to the party because the table isn't ready!")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to the party.")

print(f"{len(guests)} guests invited!")
for guest in guests:
    print(f"You're still invited, {guest}!")

del guests[:]
print(f"The guest list is now empty. See: {guests}?")

