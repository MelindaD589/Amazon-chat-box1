# I opened Amazon's Customer Service on the app, then I chose Contact Us. Then the chat box starts like this. The plan is to write my code after what I see.

print("Hello! It's Amazon's Chat Assistant again.")
print("So, what can I help you with?")

# Here you can choose from four options

helplist = ["An item I ordered", "Managing my payment, Prime, or account", "Help with Kindle, Fire, or Alexa device", "Music, eBooks, Prime Video, etc."]
print(helplist)

# Ok, I choose the first
answer1 = "An item I ordered"

# A list of my previous orders come up. 
if answer1 == "An item I ordered":
    print("Select the item that you need help with.")

orders = ["apple", "phone", "Item not on list."]
print(orders)

# I do not choose any of them.
answer2 = "Item not on list."

# Messaging Assistant, Customer Service
if answer2 == "Item not on list.":
    print("I'm sorry to hear that. Let me know which of these you need help with.")