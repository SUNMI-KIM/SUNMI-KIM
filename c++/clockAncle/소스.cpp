#include <iostream>
#include <stdlib.h>
using namespace std;

int angleClock(float h, float m);

int main(void)
{
    float t;
    float h, m;

    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> h >> m;
        cout << angleClock(h, m) << endl;
    }
    return 0;
}

int angleClock(float h, float m)
{   
    float n1 = 0.0;
    float n2 = 0.0;
    n1 = h * 30.0 + m * 0.5;
    n2 = m * 6;
    float result = abs(n1 - n2);
    if (result > 180) {
        result = 360 - result;
    }
    return int(result);
}