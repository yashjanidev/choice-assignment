def vowels_consonants(text):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel_count = 0
    consonant_count = 0

    for chars in text:
        if chars in vowels:
            vowel_count += 1
        elif chars in consonants:
            consonant_count += 1

    return {'vowels': vowel_count, 'consonants': consonant_count}


text_line = "Hello, world!. This is long statement."
vowel_consonant_counts = vowels_consonants(text_line)
print(f"Vowels: {vowel_consonant_counts['vowels']}")
print(f"Consonants: {vowel_consonant_counts['consonants']}")


def max_product_pair(arr):
    if len(arr) < 2:
        return "Please enter at least two integers."

    max1 = arr[0]
    max2 = arr[1]

    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]

    return max1 * max2


input_array = [5, 3, 8, 1, 4, 0, 5, 12]
max_product = max_product_pair(input_array)
print(f"Maximum product of two integers: {max_product}")
