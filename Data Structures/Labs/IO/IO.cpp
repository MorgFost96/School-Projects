#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

using namespace std;

int ChangeToInt(char c)
{
	int arr[] = { 0,1,2,3,4,5,6,7,8,9 };
	return arr[c - '0'];
}
int main() {
	char name[1000];
	char str[30];
	cout << "Sentence: ";
	cin.getline(name, 1000);
	cout << "\n";
	int num = 0;
	int dflag = 0;
	double num1 = 0;
	int x = 0;
	int z = 0;
	while (name[x] != '\0') {
		if (name[x] != ' ') {
			if (isalpha(name[x])) {
				cout << name[x];
			}
			if (name[x] == '.') {
				z++;
			}
			if (isdigit(name[x])) {
				int digit = ChangeToInt(name[x]);
				num = (num * 10) + digit;
			}
		}
		else
		{
			if (num != 0) {
				num = num * 2;
				if (z != 0) {
					num1 = num;
					while (z != 0) {
						num1 = num1 / 10;
						z--;
					}
					cout << num1;
				}
				else {
					cout << num;
				} 
			}
			cout << "\n";
			num = 0;
		}
		x++;
	}
	if (num != 0) {
		num = num * 2;
		if (z != 0) {
			num1 = num;
			while (z != 0) {
				num1 = num1 / 10;
				z--;
			}
		}
		else {
			cout << num;
		}
	}
	cout << "\n";
	cout << "\n";
	cout << "\n";
	system("PAUSE");
	return 0;
}



//Output:
//Sentence: Hello World, There are 3.5 Items
//
//	Hello
//	World
//	There
//	are
//	7
//	Items
//
