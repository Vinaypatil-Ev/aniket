#  WAP to calculate average marks of a 10 students.

def cal_avg(arr):
    return sum(arr) / len(arr)


if __name__ == "__main__":
    arr = [60, 92, 68, 85, 87, 70, 98, 55, 39, 98]
    x = cal_avg(arr)
    print(f"Avg of 10 students: {x}")