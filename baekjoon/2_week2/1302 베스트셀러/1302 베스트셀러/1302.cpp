#include <iostream>
#include <map>
using namespace std;

int main() {
	int N;
	cin >> N;

	map<string, int> books;
	while (N--) {
		string book;
		cin >> book;

		if (books.find(book) != books.end()) {
			books[book]++;
		}
		else {
			books[book] = 1;
		}
	}
	string bestseller;
	int compare = 0;
	for (auto i : books) {
		string b = i.first;
		int cnt = i.second;

		if (compare < cnt) {
			compare = cnt;
			bestseller = b;
		}
	}

	cout << bestseller;
}