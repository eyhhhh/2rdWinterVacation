#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool desc(int a, int b) {
	return a > b;
}

int main() {
	int N;
	cin >> N;

	vector<int> A;
	vector<int> B;

	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		A.push_back(a);
	}

	for (int i = 0; i < N; i++) {
		int b;
		cin >> b;
		B.push_back(b);
	}

	int S = 0;
	sort(A.begin(), A.end()); // 오름차순
	sort(B.begin(), B.end(), desc); // 내림차순
	for (int k = 0; k < N; k++) {
		int x = A[k];
		int y = B[k];
		S += x * y;
	}

	cout << S << endl;

}