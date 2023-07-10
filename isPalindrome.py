import re
def palindrome(s):
  # Using regular expression to filter just letters and numbers, excluding non alphanumerics chars. 
  cleanSentence = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
  return cleanSentence == cleanSentence[::-1]


s = "0P"
print(palindrome(s))