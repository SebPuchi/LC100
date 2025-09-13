class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        output = []

        n_id = 1
        one_i = 0
        two_i = 0
        while one_i < len(nums1) and two_i < len(nums2):
            current_sum = 0
            if nums1[one_i][0] == n_id:
                current_sum+=nums1[one_i][1]
                one_i +=1

            if nums2[two_i][0] == n_id:
                current_sum+= nums2[two_i][1]
                two_i +=1
            
            if current_sum != 0:
                output.append([n_id, current_sum])
            n_id += 1
        
        while one_i < len(nums1):
            output.append(nums1[one_i])
            one_i +=1
        while two_i < len(nums2):
            output.append(nums2[two_i])
            two_i +=1

        return(output)
