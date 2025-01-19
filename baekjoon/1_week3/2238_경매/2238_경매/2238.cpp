#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    int U, N;
    cin >> U >> N;

    vector<string> names;
    vector<int> prices;

    // 입력 받기
    for (int i = 0; i < N; i++) {
        string S;
        int P;
        cin >> S >> P;
        names.push_back(S);
        prices.push_back(P);
    }

    // 각 가격의 빈도를 미리 계산
    unordered_map<int, int> priceFrequency;
    for (int price : prices) {
        priceFrequency[price]++;
    }

    int minimum = 1000000;   // 최소 빈도
    int minimumP = 10000;    // 최소 빈도의 최소 가격
    string minimumN;         // 최소 빈도의 최소 가격을 제시한 사람

    for (int i = 0; i < N; i++) {
        int cnt = priceFrequency[prices[i]]; // O(1)로 빈도 조회
        int p1 = prices[i];

        if (cnt < minimum) {
            minimum = cnt;
            minimumP = p1;
            minimumN = names[i];
        } else if (cnt == minimum && p1 < minimumP) {
            minimumP = p1;
            minimumN = names[i];
        }
    }

    cout << minimumN << " " << minimumP << endl;
}