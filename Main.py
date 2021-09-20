# Repeat the exercise 2-5. Famous Quote, but this time,
# represent the famous person's name using a variable
# called famous_person.Then compose a message and
# represent the quote in a variable named message.

famous_person = "friedrich nietzsche"
quote = "'That which does not kill us " \
        "\n\tmakes us stronger'"
message = f"{quote}" \
          f"\n\t-{famous_person.title()}"
print(message)
