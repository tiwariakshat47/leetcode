class med2arrays:


    def findMedianSortedArrays(self, nums1, nums2):
        subarray = []
        count = 0
        min = 1000000

        for i in nums1:
            if i<min:
                min = i
            subarray.append(i)
            count += 1
        for j in nums2:
            subarray.append(j)
            count +=1

        if count % 2 == 1:
            return subarray[count//2]
        else:
            return (subarray[(count-1)//2] + subarray[(count)//2])/2

if __name__ == "__main__":
    obj = med2arrays()
    print(obj.findMedianSortedArrays([1,3], [2]))