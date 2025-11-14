class FenwickTree:
    def __init__(self, nums):
        self.nums = nums
        self.bit = [0] *(len(self.nums) + 1) # 1 indexed list

        for ind, ele in enumerate(self.nums):
            self.point_update(index = ind, val = 2*ele, init = True)

    def point_update(self, index, val, init = False):
        diff = val - self.nums[index]
        if not init:
            self.nums[index] = val
        index += 1 # fenwick tree is 1 indexed
        while index < len(self.bit):
            self.bit[index] += diff
            index  += (index & (-index))

    def prefix_sum(self, index):
        index += 1
        pre_sum = 0
        while index > 0:
            pre_sum += self.bit[index]
            index -= (index & (-index))
        return pre_sum
    
    def range_sum(self, i, j):
        return self.prefix_sum(index=j) - ( self.prefix_sum(index= i - 1) if i - 1 >= 0 else 0 )


# Example:
# FT = FenwickTree(nums = [3, 2, -1, 6, 5])
# print(FT.range_sum(2, 4))
# FT.point_update(3, 10)
# print(FT.range_sum(2, 4))