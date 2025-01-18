#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;

	int cnt = 1;
	for (int i = 1; i < N; i++) {
		int total = i;
		for (int j = i+1; j <= N; j++) {
			total += j;
			if (total == N) cnt++;
			else if (total > N) break;
		}
	}
	cout << cnt;
}