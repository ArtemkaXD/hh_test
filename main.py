#main.py
#Скрипт проверки правильности расставления скобок
#Объявление буффера открывающих скобок, счетчика, флага проверки
openList = []
counter = -1
check = True
#Ввод строки для проверки
inString = input()
#Цикл посимвольной проверки строки
for char in inString:
  if char == '(' or char == '{' or char == '[':
    counter += 1
    #Добавление в буффер кода символа без младшего разряда 
    openList.append(ord(char)//10)
  elif char == ')' or char == '}' or char == ']':
    #Проверка состояния буффера
    if counter == -1:
      check = False
      break
    #Сопоставление кода символа закрывающей скобки с данными из буфера
    if ord(char)//10 == openList[counter]:
      counter -= 1
      openList.pop()
    else:
      check = False
      break
if counter > 0:
  check = False
#Вывод результата проверки
print(str(check))