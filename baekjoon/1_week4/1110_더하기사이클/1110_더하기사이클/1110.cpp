#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int result = N;
	int cnt = 0;
	int num;
	while (true) {
		num = (result % 10) + (result / 10);
		
		result = (result % 10) * 10 + (num % 10);
		if (result == N) {
			cnt++;
			break;
		}
		cnt++;
	}
	cout << cnt;
}