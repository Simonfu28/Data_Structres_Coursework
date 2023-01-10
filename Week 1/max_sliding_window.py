# python3


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

def max_sliding_window(sequence, m):
    maximums = []
    temp_max = 0
    temp = []       ##queueish thing to store secondary maximums
    temp_index = 0

    for i in range(0, m):       ##analyses of the first window slice
        if sequence[i] > temp_max:
            temp_max = sequence[i]
        else:
            if not temp:
                temp.append(sequence[i])        ##adds an element into temp queue if empty
            else:
                if sequence[i] > temp[temp_index]:
                    temp[temp_index] = sequence[i]      ##stores the second biggest element in first window slice
                else:
                    temp.append(sequence[i])

    maximums.append(temp_max)       ##stores maximum in first window

    for i in range(m, len(sequence)):
        if sequence[i] > temp_max:
            temp_max = sequence[i]
        else:
            if sequence[i] > temp[-1]:
                temp[-1] = sequence[i]
            else:
                temp.append(sequence[i])
        
        dropped = sequence[i-m]
        if dropped == temp[temp_index]:
            temp_index += 1
        if dropped == temp_max:
            if temp[temp_index]>temp[temp_index+1]:
                temp_max = temp[temp_index]
            else:
                temp_max = temp[temp_index+1]
        
        maximums.append(temp_max)
    
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    y = max_sliding_window(input_sequence, window_size)
    print(y)

