def search_duplicates ():
    a = list(map(int, input().split()))
    N = len(a)
    b = []
    for i in range(N-1):
        for j in range(i+1, N):
            if a[i] == a[j]:
                b.append(a[i])
                b.append(a[j])
    # print(b) - это проверка, должна составить лист из дублей. Но проверка не проходится если повторов в исходном списке не 2, а больше. 
    # Преобразование в набор это решает, но остается вопрос как показать b корректно
    print(set(a) - set(b))

search_duplicates ()

    