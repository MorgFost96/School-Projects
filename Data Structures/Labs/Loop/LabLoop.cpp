#include <iostream>
using namespace std;

int main()
{
	int n;
	int sum = 0; 
	cout << "Enter in a number: ";
	cin >> n;

	for (int i = 1; i <= n; ++i)
	{
		sum += i;
	}
	cout << "The Sum is: " << sum << "\n";
	system("PAUSE");
	return 0;
}
