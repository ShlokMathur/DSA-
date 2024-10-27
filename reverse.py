def reverse_words(s):
    # Split the string by dots
    words = s.split('.')
    # Reverse the list of words
    print(words)
    reversed_words = words[::-1]
    print(reversed_words)
    # Join the reversed list of words with dots
    return '.'.join(reversed_words)

# Example usage:
input_str = "i.like.this.program.very.much"
output_str = reverse_words(input_str)
print(output_str)  # Output should be "much.very.program.this.like.i"
