def list_squared(m, n):
    data = [[1, 1], [42, 2500], [246, 84100], [287, 84100], [728, 722500], [1434, 2856100], [1673, 2856100], [
        1880, 4884100], [4264, 24304900], [6237, 45024100], [9799, 96079204], [9855, 113635600]]
    result = []
    index = 0
    while True:
        if m <= data[index][0] <= n:
            result.append(data[index])
        index += 1
        if index == len(data):
            break
    return result
