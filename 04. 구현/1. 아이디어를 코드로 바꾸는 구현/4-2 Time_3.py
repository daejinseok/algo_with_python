def solution(data):

    count = 0
    for k in range(data+1):
        for i in range(0, 60):
            for j in range(0, 60):
                if '3' in str(i) or '3' in str(j) or '3' in str(k):
                    count += 1

    return count


def main():
    assert solution(5) == 11475


if __name__ == "__main__":
    main()
