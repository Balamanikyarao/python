def remove_vowel():
    l=['a','e','i','o','u']
    while True:
        str1=input("Enter The String, Enter x to Terminate")
        if (str1=='x'):
            break
        else:
            for i in str1:
                if i in l:
                    str1=str1.replace(i,'')
        print("After remove vowels in string:",str1)
remove_vowel()
