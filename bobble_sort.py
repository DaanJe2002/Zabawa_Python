    def sortowanie_babelkowe(list):
        n = len(list)
        while n > 1:
            zamien = False
            for i in range(0,n-1):
                if list[i] > list[i+1]:
                    list[i],list[i+1] = list[i+1],list[i]
                    zamien = True

            n -= 1
            print(list)
            if zamien == False:
                break
        return list

sortowanie_babelkowe()

