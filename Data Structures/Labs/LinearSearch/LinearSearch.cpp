#include <iostream>
#include <iomanip>

using namespace std;

int main()
{

	int num;
	//User Input of Array Size
	cout << "Enter in a Number: ";
	cin >> num;

	int array[1000];
	int i, key;

	for (int z = 0; z < num; z++)
	{
		cout << "Enter " << z << " Number: ";
		cin >> array[z];
	}
	
	//Index 
	for (int x = 0; x < num; x++)
	{
		cout << "Array[ " << x << " ] = ";
		cout << array[x] << endl;
	}

	//User enter's in a number and it will display the Index of where it's found
	cout << "Enter Key to find in the Array: ";
	cin >> key;

	//this loop is used to have the local variable 'i' used
	for (i = 0; i < num; i++)
	{
		if (key == array[i])
		{
			cout << "Key found at the Index: " << i << endl;
			break;
		}
	}

	//it will then print a double Found Index Key or NOT FOUND in the Array
	if (i != num)
	{
		cout << "Key Found at the Index: " << i << endl;
	}
	else
	{
		cout << "Key Not Found in Array " << endl;
	}
	system("PAUSE");
	return -1;
}

//Enter in a Number : 5
//Enter 0 Number : 20
//Enter 1 Number : 3
//Enter 2 Number : 21
//Enter 3 Number : 10
//Enter 4 Number : 6
//Array[0] = 20
//Array[1] = 3
//Array[2] = 21
//Array[3] = 10
//Array[4] = 6
//Enter Key to find in the Array : 10
//Key found at the Index : 3
//Key Found at the Index : 3
//Press any key to continue . . .
