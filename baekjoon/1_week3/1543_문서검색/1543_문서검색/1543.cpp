#include <iostream>
#include <string>
using namespace std;

int main() {
	string str;
	string search;

	getline(cin, str);
	getline(cin,search);

	if (search.length() > str.length()) {
		cout << 0;
	}
	else {
		int cnt = 0;
		for (int i = 0; i <= str.length()-search.length(); i++) {
			if (str.substr(i, search.length()) == search) {
				cnt++;
				i += search.length() - 1;
			}
		}
		cout << cnt;
	}
}