if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_sorted_scores = sorted(list(set(arr)))
    runner_up_score = unique_sorted_scores[-2]
    print(runner_up_score)
