invities = ['Dylan','Van','Ify','Ben', 'Jermaine']

print(invities)

message = "\nHello " + invities[0] + ". " + "How are you? \nI would like to invite you for a special dinner"
print(message)
message = "\nHello " + invities[1] + ". " + "How are you? \nI would like to invite you for a special dinner"
print(message)
message = "\nHello " + invities[2] + ". " + "How are you? \nI would like to invite you for a special dinner"
print(message)
message = "\nHello " + invities[3] + ". " + "How are you? \nI would like to invite you for a special dinner"
print(message)
message = "\nHello " + invities[4] + ". " + "How are you? \nI would like to invite you for a special dinner"

print(message)

cancelled = 'Ify'
invities.remove(cancelled)
invities.insert(2, 'Ayden')

print("\nSecond set of invitations")

##print("\n")

message = "Hello " + invities[0] + ". " + "Unfortunaetly, " + cancelled + " " + "\nhad cancelled as he will be busy. So I have invited " + invities[2] + " " + "to come along." 
print(message)
message = "\nHello " + invities[1] + ". " + "Unfortunaetly, " + cancelled + " " + "\nhad cancelled as he will be busy. So I have invited " + invities[2] + " " + "to come along."
print(message)
message = "\nHello " + invities[2] + ". " + "How are you? \nI would like to invite you for a special dinner"
print(message)
message = "\nHello " + invities[3] + ". " + "Unfortunaetly, " + cancelled + " " + "\nhad cancelled as he will be busy. So I have invited " + invities[2] + " " + "to come along."
print(message)
message = "\nHello " + invities[4] + ". " + "Unfortunaetly, " + cancelled + " " + "\nhad cancelled as he will be busy. So I have invited " + invities[2] + " " + "to come along."

print(message)

print("\nUnfortunaetly, " + cancelled + " " + "had cancelled as he will be busy.")

print("\n")
print(invities)

invities.insert(0, 'Desmond')
invities.insert(3, 'Stephen')
invities.append('Bjorn')

print("\n Third set of invitation")
message = "\nHello " + invities[0] + ". " + "How are you? \nI would like to invite you for a special dinner"
print(message)

message = "\nHello " + invities[1] + ". " + "\nI have found three more spaces available so I will invite three other friends."
print(message)

message = "\nHello " + invities[2] + ". " + "\nI have found three more spaces available so I will invite three other friends."
print(message)

message = "\nHello " + invities[3] + ". " + "How are you? \nI would like to invite you for a special dinner"
print(message)

message = "\nHello " + invities[4] + ". " + "\nI have found three more spaces available so I will invite three other friends."
print(message)

message = "\nHello " + invities[5] + ". " + "\nI have found three more spaces available so I will invite three other friends."
print(message)

message = "\nHello " + invities[6] + ". " + "\nI have found three more spaces available so I will invite three other friends."
print(message)

message = "\nHello " + invities[7] + ". " + "How are you? \nI would like to invite you for a special dinner"
print(message)

print("\n")

print(invities)

print("\nBad news! My new dinner table will not arrive on time. \nTherefore I can only invite two people.")

print("\nCancellation of some guests")
cancelled_guest = invities.pop()
print("\nI do apologise " + cancelled_guest + " " + "\ndue to my new dinner table arriving late, I can only invite two guests. \nI am very sorry")

cancelled_guest = invities.pop()
print("\nI do apologise " + cancelled_guest + " " + "\ndue to my new dinner table arriving late, I can only invite two guests. \nI am very sorry")

cancelled_guest = invities.pop()
print("\nI do apologise " + cancelled_guest + " " + "\ndue to my new dinner table arriving late, I can only invite two guests. \nI am very sorry")

cancelled_guest = invities.pop()
print("\nI do apologise " + cancelled_guest + " " + "\ndue to my new dinner table arriving late, I can only invite two guests. \nI am very sorry")

cancelled_guest = invities.pop()
print("\nI do apologise " + cancelled_guest + " " + "\ndue to my new dinner table arriving late, I can only invite two guests. \nI am very sorry")

cancelled_guest = invities.pop()
print("\nI do apologise " + cancelled_guest + " " + "\ndue to my new dinner table arriving late, I can only invite two guests. \nI am very sorry")

print("\n")
print(invities)

print("\nFinal invite")
message = "\nHello " + invities[0] + ". " + "Due to my new table delayed I can only reserved space for another two people which you were lucky to be chosen"
print(message)

message = "\nHello " + invities[1] + ". " + "Due to my new table delayed I can only reserved space for another two people which you were lucky to be chosen"
print(message)

del invities[0]
del invities[0]
print(invities)
