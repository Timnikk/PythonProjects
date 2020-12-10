##Create a story that every time will be different. The user will enter some details that will be used in the story.
import random
name = str(input("Enter a random name: "))
age = str(input("Enter a random age: "))
city = str(input("Enter a random city: "))
activity = str(input("Enter a random activity: "))

introduction = ["Last night", "Long time ago", "Yesterday", "This Week"]
age = [" , who is " + age + " years old", " , who lived on this planet for " + age + " years"]
city = [" went to " + city, "flew to " + city,]
print(random.choice(introduction) + ", " + name + random.choice(age) + ", " + random.choice(city) + " to " + activity + ".")
