#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main(void) {
    int a;
    cin >> a;
    for (int i = 0; i < a; i++) {
        string b;
        cin >> b;
        int result = 0;
        for (int r = 0; r < b.length(); r++) {
            double c = pow((b[r] - '0'), b.length());
            result += c;
        }
        if (b == to_string(result)) {
            cout << 1 << endl;
        }
        else {
            cout << 0 << endl;
        }
    }
    return 0;
}