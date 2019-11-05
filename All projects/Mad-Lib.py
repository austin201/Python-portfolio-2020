user = input("What is your name? ")
word1 = input("Put a place that you go to ")
word2 = input("Choose an animal ")
word3 = input("Noise of animal ")
word4 = input("Put an adjective that discribes someone ")

text = str.format("""
{} Macdonald had a {} E-I-E-I-O
and on that {} he had an {} E-I-E-I-O
with a {} {} here
and a {} {} there,
here a {} there a {}
everywhere a {} {}
{} Macdonald had a {} E-I-E-I-O.""",word4,word1,word1,word2,word3,word3,word3,word3,word3,word3,word3,word3,word4,word1)
print("------------------------------------")
print("Hello"" "+user +" ""This is your mad-lib ")
print(text)
print("------------------------------------")
