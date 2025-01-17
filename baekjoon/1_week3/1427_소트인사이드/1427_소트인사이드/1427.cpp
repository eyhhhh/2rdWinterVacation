#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int num;
	cin >> num;

	vector<int> digits;

	while (num>0) {
		int digit;
		digit = num % 10;
		digits.push_back(digit);
		num = num / 10;
	}

	sort(digits.rbegin(), digits.rend());

	int result = 0;
	for (int i = 0; i < digits.size(); i++) {
		result = result * 10 + digits[i];
	}

	cout << result << endl;
}