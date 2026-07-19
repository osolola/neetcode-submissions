class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Step 1 Count How many times each number apperas
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] += 1
        
        # Step 2 Bucket Sort - Create Buckets index = frequency, value = list of numbers with that frequency
        # Size is len(nums) + 1 because a number could apperat at most len(nums) times
        # Syntax to create a list of lists
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Step 3 Place each number into the bucket  matching its frequency
        #freq.items() gives keys and value
        #num and count lets you traverse the entire map and add to byckets
        for num, count in freq.items():
            buckets[count].append(num)


        result = []
        # You start on the last valid index and you stop before reaching 0 and decrements by 1
        # Start backwards because the ones with the most values 
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
