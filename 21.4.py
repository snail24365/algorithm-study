def solution(preorders, inorders):
    if len(preorders) <= 1:
        return preorders

    root = preorders[0]
    root_idx = inorders.index(root)
    left_in = inorders[:root_idx]
    right_in = inorders[root_idx+1:]
    left_pre = preorders[1:1+root_idx]
    right_pre = preorders[1+root_idx:]
    return solution(left_pre, left_in) + solution(right_pre, right_in) + [root]


print(solution([27,16,9,12,54,36,72], [9,12,16,27,36,54,72]))
