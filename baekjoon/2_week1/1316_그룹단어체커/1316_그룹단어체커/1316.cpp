#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;

	vector<string> words(N);
	for (int i = 0; i < N; i++) {
		string word;
		cin >> word;
		words[i] = word;
	}

	vector<char> checks;
	int cnt = 0;
	for (int j = 0; j < N; j++) {
		string w = words[j];
		bool check = false;
		bool neighbor;
		for (int k = 0; k < w.size(); k++) {
			if (k != 0 && w[k - 1] == w[k]) {
				neighbor = true;
			}
			else {
				neighbor = false;
			}

			if (count(checks.begin(), checks.end(), w[k]) > 0) {
				if (not neighbor) {
					check = true;
					break;
				}
			}
			else {
				checks.push_back(w[k]);
			}
		}
		if (not check) {
			cnt++;
		}
		checks.clear();
	}

	cout << cnt;
}