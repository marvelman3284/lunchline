from people import Person, Student, Teacher


donQuixote = Person("Don Quixote", 419, 60)  # don quixote was first published in 1605
jeevan = Student("Jeevan Shah", 16, 4, 11)
mrMaier = Teacher("Mr. Maier", 30, 1000, "computer science and math", 50)

# how will the following differ?
donQuixote.greet()
jeevan.greet()
mrMaier.greet()

print(jeevan.money, jeevan.knowledge)
print(mrMaier.money)

mrMaier.tutor(1, jeevan)

# based on the `tutor` function what do you expect the output to be?
print(jeevan.money, jeevan.knowledge)
print(mrMaier.money)

# note how Jeevan wasn't able to pay for his tutoring but he still got the knowledge from it
# try to see if you can figure out how to fix that!
