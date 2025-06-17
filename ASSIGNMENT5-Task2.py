# 1. Creates a list of numbers from 1 to 10.
original_list = list(range(1,11))
print("Original List:" ,original_list)

# 2. Extracts the first five elements from the list.
extracted_list=original_list[0:5]
print("Extracted first five elements:" ,extracted_list)

# 3. Reverses these extracted elements.
extracted_list.reverse()

# 4. Prints both the extracted list and the reversed list
print("Reversed extracted elements:" ,extracted_list)
