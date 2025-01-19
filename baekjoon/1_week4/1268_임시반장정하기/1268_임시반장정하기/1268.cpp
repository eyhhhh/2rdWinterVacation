#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;  // 학생 수 입력

    // 학생들의 1학년부터 5학년까지의 반 정보를 저장할 2D 벡터
    vector<vector<int>> students(n, vector<int>(5));

    // 학생들의 반 정보 입력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> students[i][j];
        }
    }

    int maxCount = -1;  // 최대 같은 반 친구 수
    int leader = -1;    // 임시 반장 번호

    // 각 학생에 대해 다른 학생들과 비교
    for (int i = 0; i < n; i++) {
        int count = 0;  // i번 학생과 같은 반이었던 학생의 수

        for (int j = 0; j < n; j++) {
            if (i != j) {
                // 두 학생이 1학년부터 5학년까지 동일한 반에 속했는지 확인
                bool sameClass = false;
                for (int k = 0; k < 5; k++) {
                    if (students[i][k] == students[j][k]) {
                        sameClass = true;
                        break;  // 한 번이라도 같은 반이었다면 true
                    }
                }
                if (sameClass) {
                    count++;
                }
            }
        }

        // 가장 많이 같은 반이었던 학생을 찾기
        if (count > maxCount) {
            maxCount = count;
            leader = i + 1;  // 학생 번호는 1부터 시작
        }
    }

    // 임시 반장 출력
    cout << leader << endl;

    return 0;
}
