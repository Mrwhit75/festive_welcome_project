import random

def introduce_self():
  """
  Prints a welcome message. It asks the user for their name and
  then delivers a greeting in either a Chris Rock tone (if the name is Jason, Afiya, Whitney, Ian, Frank, or Penny)
  or a Mr. Rogers tone (for any other name), including a festive touch.
  Those with Chris Rock names get a joke, others get a motivational quote.
  """
  # This line ASKS the user for their name using the 'input()' function.
  # Whatever the user types will be stored in the 'name' variable.
  while True:
    try:
      name = input("Hello there! What's your name? ").strip()
      if name:  # Check if name is not empty after stripping whitespace
        break
      print("Please enter a valid name!")
    except KeyboardInterrupt:
      print("\nGoodbye! Have a great day! ✨")
      return

  # We still have our festive_touch variable for a bit of sparkle.
  festive_touch = " Let's make this journey festive! ✨"

  # Create a list of names that should get the Chris Rock tone.
  # We convert them to lowercase here so we can easily compare.
  chris_rock_names = ["jason", "afiya", "whitney", "ian", "frank", "penny"]

  # Define multiple jokes and quotes for variety
  jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What do you call a fake noodle? An impasta!"
  ]
  
  motivational_quotes = [
    "The best way to predict the future is to create it.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there."
  ]

  # Now, let's decide the tone based on the name!
  # We check if the lowercase version of the input name is IN our list of Chris Rock names.
  if name.lower() in chris_rock_names:
    # Chris Rock tone for specific names
    print(f"Alright, alright, alright, {name}! So you new to AI, huh? Don't break nothin' important, man! We watchin' you!{festive_touch}")
    # Add a random joke for Chris Rock names
    print(f"\nHere's a quick laugh for you: {random.choice(jokes)}")
  else:
    # Mr. Rogers tone for everyone else
    print(f"Welcome, my friend, {name}. It's a beautiful day to be new to AI, isn't it? We're so glad you're here.{festive_touch}")
    # Add a random motivational quote for Mr. Rogers names
    print(f"\nRemember this, friend: {random.choice(motivational_quotes)}")

  # Add a goodbye message
  print(f"\nThanks for stopping by, {name}! Keep learning and growing! 🌟")

if __name__ == "__main__":
  # Call the function to start the introduction process
  introduce_self()
