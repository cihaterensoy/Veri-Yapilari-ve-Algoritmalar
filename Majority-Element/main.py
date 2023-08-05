nums = [2,2,4,1,2,1,1,2,3,1,1,4,1,1]

def findMajority():
    numbers = {}
    result = 0
    maxNumber = 0

    for num in nums:
        #key değerleri nums listesinden geliyor
        #value olarak her döndüğünde 1 artı kendini alıyor ilk değer boşsa 0 veriyoruz
        #bu yüzden ilk anahtarımız 2, ilk değerimiz ise 1 + numbers.getten 0 geliyor
        numbers[num] = 1 + numbers.get(num,0)
        if numbers[num] > maxNumber:
            #keyimiz maxNumberdan büyükse diyoruz ki biz bu ifadeyi arıyoruz ve bu yüzden resulta eşitliyoruz
            result=num
        #bu olayı yapabilmek icin numbers anahtarlarının ve maxNumberın değerlerinden max'ı al yapıyoruz
        maxNumber = max(maxNumber,numbers[num])
    return result

print(findMajority())


#Boyer Moore

def boyerMoore():
    counter = 0
    value = 0
    for i in range(len(nums)):
        #counterımız 0 ise ilk elemanı value'nin içine atıyoruz
        if counter == 0:
            value = nums[i]
        #eğer value'miz bizim dizimizdeki elemanla aynıysa counterımızı 1 arttırıcaz
        if value == nums[i]:
            counter += 1
        #eğer aynı değilse 1 azaltıcaz
        else:
            counter -= 1
    return value
#farklı bir eleman görünce counterımız azalıyor eğer 0 a düşecek kadar farklı eleman gördüysek valuemiz değişiyor
print(boyerMoore())



