#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

map<char, string> secret;

int main() {
    secret['A'] = "000000";
    secret['B'] = "001111";
    secret['C'] = "010011";
    secret['D'] = "011100";
    secret['E'] = "100110";
    secret['F'] = "101001";
    secret['G'] = "110101";
    secret['H'] = "111010";

    int n;
    string msg;

    cin >> n;
    cin >> msg;

    vector<string> msgs;
    for (int i = 0; i < n; i++) {
        msgs.push_back(msg.substr(i * 6, 6));
    }

    string result;

    for (int i = 0; i < n; i++) {
        string m = msgs[i];
        bool check = false; // �� �޽������� �ʱ�ȭ
        int best = 6;       // �ּ� ����
        char bestE = '?';   // ���� ����� ����

        for (auto iter : secret) {
            char key = iter.first;
            string value = iter.second;

            if (m == value) {
                result += key;
                check = true;
                break; // ��Ȯ�� ��ġ�ϸ� �� �̻� ���� �ʿ� ����
            }
            else {
                int cnt = 0;
                for (int j = 0; j < 6; j++) {
                    if (m[j] != value[j]) cnt++;
                }
                if (cnt < best) {
                    best = cnt;
                    bestE = key;
                }
            }
        }

        if (!check) {
            if (best == 1) { // ������ 1�� ���
                result += bestE;
            }
            else { // ������ 2 �̻��� ���
                cout << i + 1; // 1-based index ���
                return 0;      // ���α׷� ����
            }
        }
    }

    cout << result;
    return 0;
}
