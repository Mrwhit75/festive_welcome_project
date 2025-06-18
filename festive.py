def introduce_self():
  """
  Prints a welcome message. It asks the user for their name and
  then delivers a greeting in either a Chris Rock tone (if the name is Jason, Afiya, Whitney, Ian, Frank, or Penny)
  or a Mr. Rogers tone (for any other name), including a festive touch.
  """
  # This line ASKS the user for their name using the 'input()' function.
  # Whatever the user types will be stored in the 'name' variable.
  name = input("Hello there! What's your name? ")

  # We still have our festive_touch variable for a bit of sparkle.
  festive_touch = " Let's make this journey festive! ✨"

  # Create a list of names that should get the Chris Rock tone.
  # We convert them to lowercase here so we can easily compare.
  chris_rock_names = ["jason", "afiya", "whitney", "ian", "frank", "penny"]

  # Now, let's decide the tone based on the name!
  # We check if the lowercase version of the input name is IN our list of Chris Rock names.
  if name.lower() in chris_rock_names:
    # Chris Rock tone for specific names
    print(f"Alright, alright, alright, {name}! So you new to AI, huh? Don't break nothin' important, man! We watchin' you!{festive_touch}")
  else:
    # Mr. Rogers tone for everyone else
    print(f"Welcome, my friend, {name}. It's a beautiful day to be new to AI, isn't it? We're so glad you're here.{festive_touch}")

# Call the function to start the introduction process
introduce_self()
