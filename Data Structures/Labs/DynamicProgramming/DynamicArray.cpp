#include <iostream>
#include<iomanip>

using namespace std;

int main()
{
	int size;
	int num = 0;
	int input = 0;
	int *array;
	cout << "Please enter in the size of the array you would like: " << "\n";
	cin >> size; 
	array = new int[size]; //The Array will now be the size the user input
	cout << "Please enter in a couple of Numbers to store in your Array then/or enter -1 to quit: " << "\n";

	//loop used for the number in the array the user put in or if user enters in -1 
	//they will input the number at which the array is
	//at and the number the user input in
	while (num != -1)
	{
		cin >> num;
		if (num == -1)
		{
			int x = 0;
			for (x; x < input; x++)
				cout << "The Number at " << x << " is: " << array[x] << "\n";
		}
		else
		{
			array[input] = num;
			input++;
			if (input == size)
			{
				size += size;
				cout << "The Size of your array is now: " << size;
			}
		}

	}
	system("PAUSE");
	return 0;
}
//Output
//Please enter in the size of the array you would like :
//10
//Please enter in a couple of Number to store in your Array or -1 to quit :
//1
//2
//7
//8
//- 1
//The Number at 0 is: 1
//The Number at 1 is : 2
//The Number at 2 is : 7
//The Number at 3 is : 8