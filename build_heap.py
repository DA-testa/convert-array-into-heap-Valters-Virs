# python3
def siftDown(i, data, swaps):
    left = 2*i + 1
    right = 2*i + 2

    if right < len(data):
        smallest = left if (data[left] < data[right]) else right

        if data[smallest] < data[i]:
            data[i], data[smallest] = data[smallest], data[i]
            swaps.append([i, smallest])

            siftDown(smallest, data, swaps)

def build_heap(data):
    swaps = []

    for i in range((len(data) // 2) - 1, -1, -1):
        siftDown(i, data, swaps)

    return swaps


def main():
    input_type = input()
    swaps = []

    if input_type.upper()[0] == "I":
        # Input I

        try:
            n = int(input())
            data = list(map(int, input().split()))
        except:
            print("Wrong input")

    elif input_type.upper()[0] == "F":
        # Input F
        file_input = input()
        
        try:
            file = open("tests/" + file_input[:2], "r")
        except:
            print("File not found")
        else:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))

            file.close()
    else:
        print("Wrong input")

    assert len(data) == n, "Size isn't matching number of elements"

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
