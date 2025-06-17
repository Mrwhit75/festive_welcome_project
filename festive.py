def introduce_self():
  """
  Prints a welcome message. It now asks the user for their name
  and includes a statement about being new to AI, with a festive touch.
  """
  # This line now ASKS the user for their name using the 'input()' function.
  # Whatever the user types will be stored in the 'name' variable.
  name = input("Hello there! What's your name? ")

  # We're introducing a new variable named 'festive_touch'
  # to add a fun, celebratory part to the message.
  festive_touch = " Let's make this journey festive! ✨"

  # This line then uses the name the user typed and the festive_touch
  # to create the welcome message.
  print(f"Welcome! My name is {name} and I'm new to AI.{festive_touch}")

# Call the function to start the introduction process
introduce_self()
