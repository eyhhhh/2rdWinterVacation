#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;  // �л� �� �Է�

    // �л����� 1�г���� 5�г������ �� ������ ������ 2D ����
    vector<vector<int>> students(n, vector<int>(5));

    // �л����� �� ���� �Է�
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> students[i][j];
        }
    }

    int maxCount = -1;  // �ִ� ���� �� ģ�� ��
    int leader = -1;    // �ӽ� ���� ��ȣ

    // �� �л��� ���� �ٸ� �л���� ��
    for (int i = 0; i < n; i++) {
        int count = 0;  // i�� �л��� ���� ���̾��� �л��� ��

        for (int j = 0; j < n; j++) {
            if (i != j) {
                // �� �л��� 1�г���� 5�г���� ������ �ݿ� ���ߴ��� Ȯ��
                bool sameClass = false;
                for (int k = 0; k < 5; k++) {
                    if (students[i][k] == students[j][k]) {
                        sameClass = true;
                        break;  // �� ���̶� ���� ���̾��ٸ� true
                    }
                }
                if (sameClass) {
                    count++;
                }
            }
        }

        // ���� ���� ���� ���̾��� �л��� ã��
        if (count > maxCount) {
            maxCount = count;
            leader = i + 1;  // �л� ��ȣ�� 1���� ����
        }
    }

    // �ӽ� ���� ���
    cout << leader << endl;

    return 0;
}
