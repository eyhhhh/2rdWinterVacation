#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
    int s = 1;  // 테스트 케이스 번호
    map<int, string> results; // 각 테스트 케이스의 결과 저장
    while (true) {
        int n;
        cin >> n;
        cin.ignore();

        if (n == 0) break; // n이 0이면 종료

        map<int, string> names;
        for (int i = 0; i < n; i++) {
            string name;
            getline(cin, name);
            names[i+1] = name;
        }

        // 2n-1번 반복하면서 입력 받음
        map<int, char> st;
        for (int i = 0; i < 2 * n - 1; i++) {
            int num;
            char check;
            cin >> num >> check;

            if (st.count(num) == 1) {  // 이미 체크된 번호라면 해당 이름 변경
                names[num] = "removed";
            }
            else {  // 처음 보는 번호라면 map에 저장
                st[num] = check;
            }
        }

        // 결과 저장
        for (auto i : names) {
            string val;
            val = i.second;
            if (val != "removed") {
                results[s] = val;
            }
        }
        s++;
    }

    // 결과 출력
    for (auto iter : results) {
        cout << iter.first << " " << iter.second << endl;
    }

    return 0;
}
