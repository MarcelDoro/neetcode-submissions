class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def is_any_greater(triplet: List[int], max_values: List[int]) -> bool:
            for i in range(len(triplet)):
                if triplet[i] > max_values[i]:
                    return True

            return False


        max_values = [0, 0, 0]
        for triplet in triplets:
            if is_any_greater(triplet, target) == False:
                for i in range(len(triplet)):
                    max_values[i] = max(max_values[i], triplet[i])

        return max_values == target
