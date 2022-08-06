#include <iostream>

using namespace std;

int main(void) {
	int a;
	cin >> a;
	for (int i = 0; i < a; i++) {
		int b;
		cin >> b;
		int result = 0;
		int one, two, three;
		int pre = 0;
		cin >> one >> two >> three;
		if (one < two and two > three) {
			result++;
		}
		for (int j = 0; j < b-3; j++) {
			int input;
			cin >> input;
			one = two;
			two = three;
			three = input;
			if (one < two and two > three) {
				result++;
			}
			if (one == two and two == three) {
				continue;
			}
			if (one < two and two == three) {
				pre = one;
			}
			else if (one == two and two > three and pre != 0) {
				result++;
				pre = 0;
			}
			else if (one == two and two < three and pre != 0) {
				pre = 0;
			}
		}
		cout << result << endl;
	}
	return 0;
}