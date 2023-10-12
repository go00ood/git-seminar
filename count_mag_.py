'''개수 세기'''
def count_word_occurrences(text, word_to_search):
    text_lower = text.lower()
    word_lower = word_to_search.lower()
    word_count = text_lower.count(word_lower)
    return word_count

if __name__ == "__main__":
    file_path = 'nY.txt'  #말뭉치 파일 지정
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words_to_search=''
    while True:
        word=input() #검색할 단어 입력, ! 입력 시 끝남
        if word=='!':
            break
        word+=' '
        words_to_search+=word

    words_to_search= words_to_search.split()
    print(words_to_search)
    result_dict = {}
    for word_to_search in words_to_search:
        count=0
        for a in range(2):
            if a==0:
                word_to_search_n=word_to_search+'_mag'

                count_tem = count_word_occurrences(text, word_to_search_n)
                count+=count_tem
            else:
                word_to_search_n=word_to_search+'<<'

                count_tem = count_word_occurrences(text, word_to_search_n)
                count+=count_tem
                result_dict[word_to_search] = count
        print(word_to_search, 'end!')


    '''파일 저장 부분 '''
    result_file_path = 'results.txt'
    with open(result_file_path, 'w', encoding='utf-8') as result_file:
        for word, count in result_dict.items():
            result_file.write(f"{word}: {count}\n")

    print(f"Results saved to {result_file_path}.")
