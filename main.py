path = input('Input filename pls: ')
testingFile = open(rf'./{path}',"w+")
print(testingFile.read())
addedTest = input("If you would like to write something in file, paste it here, if not just paste NO: ")
testingFile.write(addedTest)
print(testingFile.read())

# 
[SwitchyOmega Conditions]
@with result

*.yandex.* +direct
*.vk.* +direct
*.animego.* +direct
*.aniboom.* +direct
*.mangalib.* +direct
*.dzen.ru +direct
*.kinopoisk.ru +direct
192.168.31.* +direct
*.pikabu.ru +direct
*.gosuslugi.ru +direct
*.netology.* +direct
*.dvfu.ru +direct

* +proxy
