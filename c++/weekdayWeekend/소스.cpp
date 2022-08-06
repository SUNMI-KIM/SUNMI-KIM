#include <iostream>

using namespace std;

int main() {
	string str_day[] = { "0", "1", "2", "3", "4", "5", "6" };
	int month_day[] = { 31,28,31,30,31,30,31,31,30,31,30,31 };
	int for_a;
	cin >> for_a;
	for (int i = 0; i < for_a; i++) {
		int year;
		int month;
		int day;
		int day_total = 0;
		cin >> year >> month >> day;
		for (int l = 1582; l < year; l++) {
			if ((l % 4 == 0 && l % 100 != 0) || (l % 400 == 0)) {
				day_total += 366 ;
			}
			else {
				day_total += 365 ;
			}
		}
		if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
			month_day[1] = 29;
		}
		else {
			month_day[1] = 28;
		}
		for (int r = 1; r < month; r++) {
			day_total += month_day[r-1];
		}
		day_total += day-1 ;
		cout << str_day[(5+ day_total) % 7] << endl;
	}
	return 0;
}

