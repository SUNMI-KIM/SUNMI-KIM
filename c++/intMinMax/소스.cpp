#include <iostream>
using namespace std;

int main(void) {
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; i++) {
        int max, min;
        int numData, data;

        cin >> numData;
        cin >> data;

        min = max = data;

        for (int j = 1; j < numData; j++) {
            cin >> data;
            if (data < min) min = data;
            if (data > max) max = data;
        }
        cout << max << " " << min << endl;
    }
    return 0;
}