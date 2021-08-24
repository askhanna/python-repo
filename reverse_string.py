def reverse_string(string):
    if len(string) <= 1:
        return string
    return string[-1] + reverse_string(string[:-1])


def reverse_text(string):
    curr_word = ''
    result = ''
    for char in string:
        if char == ' ' or char == '\t':
            if not curr_word == '':
                result += reverse_string(curr_word)
                curr_word = '' 
            result += char
        else:
            curr_word += char
    result += reverse_string(curr_word)
    #print(result)
    return(result)
         
#assert reverse_string("Ashish") == 'hsihsA'
#assert reverse_string('moo cow  bark dog') == 'oom woc  krab god'
#assert reverse_string('moo  ') == 'oom  '
#assert reverse_string('  moo moo') == '  oom oom'
#assert reverse_string('  ') == '  '
def main():
    text = reverse_text('moo cow  bark dog')
    print(text)

if __name__ == "__main__":
    main()

