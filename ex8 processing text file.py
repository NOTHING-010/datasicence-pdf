def read_process(file_name):
    words=[]
    with open(file_name,"rt",encoding='utf-8')as f:
     words=[word for line in f for word in line.split()]
    
    words=[w.lower()for w in words]
    char_clean=''' !@#$%^&*|\/.,;:"'-`~'''
    clean_word=[]
    for word in words:
        for char in word:
            if char in char_clean:
                word=word.replace(char,"")
        clean_word.append(word)
                
    return clean_word
def count_freq(words,word_count):
    return words.count(word_count.lower())
if __name__ == "__main__":
    file_path = r"D:\py promg\dataset\sample.txt"
    word_list = read_process(file_path)
    print(count_freq(word_list, "The"))
    
