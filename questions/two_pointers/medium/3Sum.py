class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negative_hash = {}

        for i in range(len(nums)):
            print("index", i)
            negative_hash[(-1 * nums[i], i)] = nums[i]
            print(negative_hash)

        answer_array = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(i,j)
            current_sum = nums[i] + nums[j]
            if current_sum in [item[0] for item in negative_hash.keys()]:
                print("cur sum", current_sum)
                num, index = negative_hash[current_sum]

                if i != index and j != index:
                    answer_array.append([nums[i], nums[j], num])

        print(answer_array)

