import re

roPunctuation = ",:;?!-()...-\"\""


# read a text file
def read_file(filename):
    with open(filename, "r") as f:
        text = f.read()
        f.close()
        return text


# delete ro punctuations symbols
def remove_punctuation(filename):
    text = read_file(filename)
    table = str.maketrans("", "", roPunctuation)
    res = text.translate(table)
    f = open(filename, "w")
    f.write(res)
    f.close()
    return filename


# print the result
def print_result(filename):
    f = read_file(filename)
    #print(f.read())


# delete multiple spaces
def del_multiple_spaces(filename):
    text = read_file(filename)
    text = re.sub(' + ', ' ', text)
    return text


if __name__ == '__main__':
    remove_punctuation("fisier.txt")
    text = del_multiple_spaces("fisier.txt")
    print(text)



