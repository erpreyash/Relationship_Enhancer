import speech_to_text as negative_sentiments
import profanity_check

text = "This is a test sentence. It contains some bad words."

# check if text contains profanity
#TODO: Calculate the percent of the text/sentence, text/ day, text/entire audio recording
is_profane = profanity_check.is_profane(text)

# print result
print("Text contains profanity:", is_profane)