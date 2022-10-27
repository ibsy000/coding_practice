def solution(S):
    pass_cam_count = 0

    for idx, char in enumerate(S):
        if char == "<":
            pass_cam_count += S[:idx:].count(".")
        if char == ">":
            pass_cam_count += S[idx::].count(".")
    return pass_cam_count

print(solution(">..>.<.>.."))