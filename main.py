import sys
import decimal
sys.stdin = open("input.txt", "rt", encoding="UTF-8")
sys.stdout = open("output.txt", "wt", encoding="UTF-8")


def main():
    """ input.txt 예제
    100
    input_override
    10 20
    """
    # 만약 자릿수가 엄청 큰 숫자를 다룬다면 decimal 라이브러리를 사용해야 한다.
    # 최대 100000자릿수로 설정하는 의미이다.
    decimal.getcontext().prec = 100000

    # sys.stdin.readline() -> 한줄을 입력 받는 함수
    # strip() 문자열 양 끝 줄바꿈, 공백 문자를 지운다.
    n = sys.stdin.readline().strip()
    n = decimal.Decimal(n)
    result = n + 1
    print(result)

    # input을 덮어씌워 다음과 같이 사용할 수 있다.
    input = sys.stdin.readline
    one_line = input().strip()
    print(one_line)

    # split()은 문자열을 공백을 기준으로 나누어 리스트로 반환한다.
    # map은 java Stream API map을 생각하면 된다.
    # 첫 번째는 함수 이름, 두 번째는 iterator 객체(ex, list, tuple)을 넣는다.
    # 두 번쨰에 들어온 값의 요소들을 순회하며 첫 번째에 들어온 함수 이름을 호출한다.
    # 그리고 각 요소 함수 호출 결과를 generator(iterator와 유사한 동작을 함)로 반환한다.
    a, b = map(int, sys.stdin.readline().split())
    sum = a + b
    print(sum)

    # print 함수의 자동 줄바꿈 안하기
    print("Hello world", end="")
    print("줄바꿈 되지 않았습니다.", end="")
    print("이제 줄바꿈 됩니다.")
    print("다음줄입니다.")


main()
