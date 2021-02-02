def power_set(arr: list, idx: int, data: str, result: list):
    if idx == len(arr):
        result.append(data)
    else:
        power_set(arr, idx + 1, data, result)
        data += arr[idx]
        power_set(arr, idx + 1, data, result)
    return result

print(power_set(["a", "b", "c"], 0, "", []))