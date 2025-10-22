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
  return True

def get_sentence():
  s = input("Enter a sentence: ")
  while not is_sentence(s):
    print("That doesn’t count as a proper sentence.")
    s = input("Enter a sentence: ")
  return s

def calculate_frequencies(sentence):
  sentence = sentence[:-1].lower()                  # removes last punctuation
  words = re.findall(r"\b\w+\b", sentence.lower())  # removes punctuation in words
  word_list = []
  freq_list = []

  for w in words:
    if w in word_list:
      i = word_list.index(w)
      freq_list[i] += 1
    else:
      word_list.append(w)
      freq_list.append(1)
  return word_list, freq_list

def print_frequencies(words, freq):
  print("\nWord Frequencies:")
  for i in range(len(words)):
    print(words[i], ":", freq[i])

def main():
  s = get_sentence()
  words, freq = calculate_frequencies(s)
  print_frequencies(words, freq)

if __name__ == "__main__":
  main()

