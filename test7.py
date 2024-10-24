

#//*[@id="attribute-group-manufacturer"]/section/div[1]/div/div[1]/div[1]/section[2]/div/div/div

text = "The value 'Cambridge University Press'' specified cannot be used as it conflicts with the value 'Prakash India private limited' for ASIN Z in the Amazon catalog. If this is ASIN 'B0DFZ2FY11', update the value to match the ASIN data. If this is a different product, update identifying information (UPC/EAN/Part Number/etc)."

# Specify the starting index
start_index = 50
search_char = "'"

# Slice the text from the starting index
sliced_text = text[start_index:]

# Find the character in the sliced text
char_index_in_sliced = sliced_text.find(search_char)

sliced_text2 = sliced_text[char_index_in_sliced+5:]

char_index_in_sliced2 = sliced_text2.find(search_char)
# Adjust the index to be relative to the original text
st = start_index + char_index_in_sliced + 1
end = start_index + char_index_in_sliced + char_index_in_sliced2 + 5

print(text[st:end])  # This will give you the index of the character in the original text
