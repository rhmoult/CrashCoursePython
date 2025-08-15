guests = ['Alice Cooper', 'Vincent Price', 'Bela Lugosi', 'Stan Lee']

for guest in guests:
    print(f"Welcome to the party, {guest}!")

user_who_cancelled = guests.pop()
guests.append('H.P. Lovecraft')
print(f"Unfortunately, {user_who_cancelled} can't make it to the party.")

for guest in guests:
    print(f"Thanks for being here, {guest}!")

print("I found a larger table, so we can invite more guests!")

guests.insert(0, 'Frankenstein')
guests.insert(2, 'Dracula')
guests.append('The Mummy')

for guest in guests:
    print(f"Welcome to the party, {guest}!")