#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

def is_sentence(text):
  if not isinstance(text, str) or not text.strip():
    return False
  if not text[0].isupper():
    return False
  if not re.search(r'[.!?]$', text):
    return False
  if not re.search(r'\w+', text):
    return False
  return True

def get_sentence():
  sentence = input("Enter a sentence: ")
  while not is_sentence(sentence):
    print("That doesn’t count as a proper sentence.")
    sentence = input("Enter a sentence: ")
  return sentence

def calculate_frequencies(sentence):
  sentence = sentence[:-1].lower()                  # removes last punctuation
  words = re.findall(r"\b\w+\b", sentence.lower())  # removes punctuation in words
  word_list = []
  freq_list = []

  for word in words:
    if word in word_list:
      index = word_list.index(word)
      freq_list[index] += 1
    else:
      word_list.append(word)
      freq_list.append(1)
  return word_list, freq_list

def print_frequencies(words, freq):
  print("\nWord Frequencies:")
  for i in range(len(words)):
    print(words[i], ":", freq[i])

def main():
  sentence = get_sentence()
  words, freq = calculate_frequencies(sentence)
  print_frequencies(words, freq)

if __name__ == "__main__":
  main()
