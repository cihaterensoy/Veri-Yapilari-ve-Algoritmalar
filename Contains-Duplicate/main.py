nums = [1, 2, 3, 4, 5, 6, 7, 7]


def solution():
    # Brute Force yöntemi -> yer yönetimi olarak O(1), zaman yönetimi olarak O(n^2)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] == nums[j]:
                    return True
    return False


solution()
print(solution())
"""
#yer yönetimi O(n), zaman yönetimi 0(n)
def cozum():
    numsSet = set()
    for num in nums:
        if num in numsSet: #eklerken eklemeye çalıştığım eleman setimde varsa true döndürür yoksa false döner
            print(numsSet)
            return True
        numsSet.add(num)
    return False
print(cozum())



def solution2(): return len(nums) != len(set(nums)) #eleman sayıları eşit değilse illaki bir elemanı aynı olacak 
cünkü set koleksiyonu her bir elemandan bir tane olmasına izin verir print(solution2())"""
