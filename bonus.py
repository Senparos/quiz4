#author: Jay Sanders

def lengthCalculator(arr) -> str:
    for i in range(len(arr)):
        arr[i] = len(str(arr[i]))
    return arr

def main():
    arr1 = ["abc", "apple", "orange"]
    arr2 = [12, 456, 9000]
    arr3 = lengthCalculator(arr1)
    arr4 = lengthCalculator(arr2)
    # print("[", end="")
    # for i in range(len(arr3) - 1):
        # print(arr3[i], end=",")
    # print(f"{arr3[len(arr3) - 1]}]")

    # print("[", end="")
    # for i in range(len(arr4) - 1):
        # print(arr4[i], end=",")
    # print(f"{arr4[len(arr4) - 1]}]")

if __name__ == "__main__":
    main()
    