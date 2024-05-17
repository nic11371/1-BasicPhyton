from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    arr = []
    for e1, e2 in enumerate(zip(nums1, nums2)):
        if e2[0] < e2[1]:
            arr.append(e1)
    return arr

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

# l1 = [1,5,7,3]
# l2 = [8,11,6,10]
#
# print(get_indexes(l1, l2))