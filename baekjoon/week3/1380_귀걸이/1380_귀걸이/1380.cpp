#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
    int s = 1;  // �׽�Ʈ ���̽� ��ȣ
    map<int, string> results; // �� �׽�Ʈ ���̽��� ��� ����
    while (true) {
        int n;
        cin >> n;
        cin.ignore();

        if (n == 0) break; // n�� 0�̸� ����

        map<int, string> names;
        for (int i = 0; i < n; i++) {
            string name;
            getline(cin, name);
            names[i+1] = name;
        }

        // 2n-1�� �ݺ��ϸ鼭 �Է� ����
        map<int, char> st;
        for (int i = 0; i < 2 * n - 1; i++) {
            int num;
            char check;
            cin >> num >> check;

            if (st.count(num) == 1) {  // �̹� üũ�� ��ȣ��� �ش� �̸� ����
                names[num] = "removed";
            }
            else {  // ó�� ���� ��ȣ��� map�� ����
                st[num] = check;
            }
        }

        // ��� ����
        for (auto i : names) {
            string val;
            val = i.second;
            if (val != "removed") {
                results[s] = val;
            }
        }
        s++;
    }

    // ��� ���
    for (auto iter : results) {
        cout << iter.first << " " << iter.second << endl;
    }

    return 0;
}
