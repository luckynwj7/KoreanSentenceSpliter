import kss

def sentenceSplit(inputText):
    result = []
    for sent in kss.split_sentences(inputText):
        result.append(sent)
    return result

print("파일 경로를 입력하세요.")
filePath = input()
print("파일 이름을 입력하세요.")
fileName = input()

r = open(filePath + "\\" + fileName, mode='rt', encoding='utf-8')
content = r.read()
resultList = sentenceSplit(content)

result = ""
for sent in resultList:
    result += sent
    result += "||SentSplitArea||"

f = open(filePath + '\\SentenceSplitResult.txt', mode='wt', encoding='utf-8')
f.write(result)