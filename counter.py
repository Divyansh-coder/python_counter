def count(text):
    """The function returns the descending order of frequency of 
       each letter present in the input string"""
    word={}
    final_word=[]
    text=text.lower()
    skips=[",",".","?",'"',"'",":",";"," "]
    for skip in skips:
        text=text.replace(skip,"")
    for words in text:
        if words in word:
            word[words]+=1
        else:
            word[words]=1
    value=sorted(word.values(),reverse=True)
    for i in range(len(value)):
        for w_d in word.keys():
            if word[w_d]==value[i]:
                final_word.append([w_d,value[i]])
                del word[w_d]
                break
    return final_word
    
string=input("enter any string: ")
result=count(string)
for x,y in result:
    print(x,"=",y)
