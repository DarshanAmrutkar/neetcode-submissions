class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        # Better
        # products = [0]*len(arr)
        # zeroCount = arr.count(0)

        # if zeroCount > 1:
        #     return products

        # if zeroCount == 1:
        #     prod = 1
        #     for num in arr:
        #         if num != 0:
        #             prod *= num
        #     for i in range(len(arr)):
        #         if arr[i] == 0:
        #             products[i] = prod
        #     return products
        
        # if zeroCount == 0:
        #     prod = 1
        #     for num in arr:
        #         prod *= num
        #     for i in range(len(arr)):
        #         products[i] = prod // arr[i]
        # return products

        # OPTIMAL
        products = [1]*len(arr)
        prefix = 1
        for i in range(len(arr)):
            products[i] = prefix
            prefix *= arr[i]

        sufix = 1
        for i in range(len(arr)-1, -1, -1):
            products[i] *= sufix
            sufix *= arr[i]    
            
        return products
