def is_polindrome(str):
    clear_str = ""
    signs = ', .:'
    for i in str:
        if i not in signs:
            clear_str += i
    lst = clear_str.split(' ')
    for j in range((len(lst) // 2) + 1):
        lst[j] = lst[j].lower()
        if lst[j] == lst[j - 1]:
            return 'string is polindrome'
    return False

print(is_polindrome("A man, a plan, a canal: Panama"))