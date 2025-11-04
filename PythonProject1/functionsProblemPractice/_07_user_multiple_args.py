import math

nums = list(map(int, input("enter the multiple numbers here:-").split()))

def total_sum(*nums):
    return {
        "total": sum(nums),
        "max": max(nums),
        "min": min(nums),
        "avg": math.floor(sum(nums) / len(nums)),

    }

print(total_sum(*nums))
