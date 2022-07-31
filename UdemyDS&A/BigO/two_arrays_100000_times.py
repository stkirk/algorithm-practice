# What is the time complexity of the code below?

def unordered_pairs(arrayA, arrayB):
    for i in arrayA: # O(len(arrayA))
        for j in arrayB: # O(len(arrayB))
            for k in range(0, 100000): # O(100000), CONSTANT TIME --> O(1)
                print(arrayA[i], arrayB[j])

# Time Complexity: O(ab)
