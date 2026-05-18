def reverse_string(str):
    result = ""
    for char in str:
        result = char + result
    return result

input_str = input()
if input_str == reverse_string(input_str):
    print(f"{input_str}\n입력하신 단어는 회문(Palindrome)입니다.")