while True:
    print("""\tВыберите пункт меню:
1) Выберите файл для обработки
2) Просмотр результата
3) Выход из программы
    """)
    vibr=input("Выполнить: ")
    if vibr=="1":
        global file
        file=input("Введите путь: ")
        if file !="":
            file1=input("Введите имя файла: ")
            if file1 !="":
                x = open(file+"/"+file1, 'r')
                r = x.read()
                x.close()
                sum = 0
                for i in r:
                    # print(i)
                    if '0' <= i <= '9':
                        i = int(i)
                        sum += i

                x = open(file+"/Data2.txt", 'a+')

                x.write(str(sum) + '\n')
                x.close()
        else:
            continue
    elif vibr=="2":
        openfile=open(file+"/Data2.txt",'r')
        print("\tСодержимое файла:\n"+openfile.read())

    elif vibr=="3":
        print("Производится выход из программы")
        break
    else:
        print("Вы ввели не коректный символ или неправельный номер меню")
        
        asd
        dsffdsfdsdsfdsf
        saddsa
        adidas
