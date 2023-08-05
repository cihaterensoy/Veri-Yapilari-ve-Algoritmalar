nums = [1,2,1,4,2,32,3,3,4]
#bit manipülasyonu yapmamız gerekiyor bunun için XOR kullanacağız
#XOR mantığı
# 0 0 -> 0
# 0 1 -> 1
# 1 0 -> 1
# 1 1 -> 0
#aynı olunca 0 farklı olunca 1 cıkıyor(girdiler aynıysa cıkış 0, girdiler farklıysa çıkış 1 olur)
#0101 ^ 0011 = 0110
#listenin her bir elemanını burada bu koşullara tabi tutuyoruz ve her bir eleman 0 ve 1ler olarak değişkenimizin içine atıyoruz ve elinde sonunda aynı birler birbirini götürüyor
# 1010 xor 1010 = 0000
#3 + 5 + 4 - 5 - 3
#3 - 3 =  0
def singleNumber():
    sayı = 0
    if len(nums) == 1:
        print(nums[0])  # Edge Case için yapılan bir if sütünu
    else:
        for i in nums:
            sayı = sayı ^ i
        return sayı


print(singleNumber())















