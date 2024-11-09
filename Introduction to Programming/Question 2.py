alphabetical_count = 0
nonalphabetical_count = {}

character_stream = input("Please enter the character stream? ")

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in character_stream:
    if i in alphabet:
        if i.isalpha():
            i=i.lower()
        if i in nonalphabetical_count:
            nonalphabetical_count[i]  += 1
        else:
            nonalphabetical_count[i] = 1
    else:
        if i!= " ":
            alphabetical_count +=1


for ans,count in nonalphabetical_count.items():
    print(ans, "=",count)
print(" ")
print("Number of non alphabitical characters:",alphabetical_count)
