import codecs
import collections

def frequencyAnalisys(hexstring):
    string = codecs.decode(hexstring, 'hex')
    string_list = list(string)
    common_list = collections.Counter(string_list)
    common_char_list = common_list.most_common()
    common_char = common_char_list[0][0]
    print('Most commom character is {}'.format(chr(common_char)))
    return common_char

def keyGen(hexstring, char):
    key_lenght = len(list(hexstring))//2
    hex_char = hex(char)[2:]
    key_list =[]
    
    for _ in range(key_lenght):
        key_list.extend(hex_char)
       
    key = ''.join(key_list)
    return key

def xorstrings(hexstring, key):

    return "".join(["%x" % (int(x,16) ^ int(y,16)) for (x, y) in zip(hexstring, key)])
    
    
def commonLetterkey(common_letter, commom_char):
    
    common = ord(common_letter)
    key_char = common^commom_char
    return key_char

def runAnalasys(common_letter_list, hexstring, to_test):
    freq_char = frequencyAnalisys(hexstring)

    for common_letter in common_letter_list:
        letter_key = commonLetterkey(common_letter, freq_char)
        key = keyGen(hexstring, letter_key)
        decoded = xorstrings(hexstring, key)
        print(decoded)

        silly = list(codecs.decode(decoded, 'hex'))
        silly_list = []
        for i in silly:
            silly_list.append(chr(i))
        silly_complet = ''.join(silly_list)
        

        for i in to_test:
            if i in silly_complet:
                print('key: {} text: {}'.format(letter_key, silly_complet))
                break
        
        


to_decode = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

to_test = ['th', 'er', 'on', 'an', 're', 'he', 'in', 'ed', 'nd', 'ha', 'at', 'en', 'es', 'of', 'or', 'nt', 'ea', 'ti', 'to', 'it', 'st', 'io', 'le', 'is', 'ou', 'ar', 'as', 'de', 'rt', 've']


common_letter_list = [' ', 'e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p', 'g', 'w', 'y', 'b', 'v', 'k', 'x', 'j', 'q', 'z']
runAnalasys(common_letter_list, to_decode, to_test)





