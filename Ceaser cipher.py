txt= list(input("Please, enter a text: "))
key =1 #Ceaser cipher's key
list= [] #convert the text to a list of letters
for i in txt:
    if i =='z':
        new_letter_ord = 'a'
        list.append(new_letter_ord)  #put 'a' in the list
    elif i =='Z':
        new_letter_ord = 'A'
        list.append(new_letter_ord)  # put 'a' in the list
    elif i == ' ':
        new_letter_ord = ' '
        list.append(new_letter_ord)  #put ' ' in the list

    elif i.isalpha():
        place = ord(i)  # convert the letter to its order in alphabets
        new_letter_ord = place + key
        the_encrypted_letter = chr(new_letter_ord)  # return it into encrypted chr
        list.append(the_encrypted_letter)  # put each letter in the list

    else:
        new_letter_ord = i
        list.append(new_letter_ord)  # put chr in the list
the_new_message="".join(list) #join all the chrs together to struct a sentence
print(the_new_message)