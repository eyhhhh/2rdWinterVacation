#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;

	vector<int> weights;
	if (n == 0) cout << 0;
	else {
		for (int i = 0; i < n; i++) {
			int w;
			cin >> w;
			weights.push_back(w);
		}
		int total = 0;
		int minimum = 1;
		for (auto w : weights) {
			total += w;
			if (total > m) {
				minimum++;
				total = w;
			}
		}
		cout << minimum;
	}
}