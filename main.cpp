#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
const ll INF = 987'654'321;

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    /* input.txt 예제
    1 2
    str1 str2
    I want input one line
    */

    // input Ex: 1 2
    int a, b;
    cin >> a >> b;
    int result = a + b;
    cout << result << "\n";

    // input Ex: str1 str2
    string str1, str2;
    cin >> str1 >> str2;
    cout << str1 << "\n";
    cout << str2 << "\n";

    // input Ex: I want input one line
    // 한 줄 입력을 받을 때 다음 함수를 사용한다. getline(입력소스, 저장될 문자열 변수)
    // 다만 getline() 호출 이전에 다음과 같이 cin >> a >> b 와 같이 줄바꿈이 있었다면
    /*
    10 20
    I want input one line
    */
    // getline에서는 20 뒤 줄바꿈 문자열까지 입력을 받아 비어있는 문자열이 들어온다.
    // 따라서 cin.ignore() 함수로 입력 버퍼의 문자 1개(줄바꿈문자)를 지워야 한다.

    string line;
    cin.ignore();
    getline(cin, line);
    cout << line << "\n";

    return 0;
}