#include<iostream>
#include<conio.h>
using namespace std;
int main() {
	int array[5];
	int z; 
	int temp; 
	int x;
	cout << "Enter any 5 numbers in array: \n";
	// for loop to enter 5 numbers into the array
	for (z = 1; z < 6; z++) 
	{
		cout << "Enter Array Number " << z << " : ";
		cin >> array[z]; // inserting the numbers into an array
	}
	// printing array before sorting
	cout << "\Array before sorting: ";
	for (x = 1; x < 6; x++) {
		cout << " " << array[x] << ",";
	}
	//Sorting:
	for (z = 1; z < 6; z++) 
	{// this loop is traversing the array
		for (x = 1; x < 6 - z; x++)
		{
			if (array[x]>array[x + 1]) // comparing the array's
			{
				// if array[0] is greater than array[1] then it will swap
				temp = array[x];
				array[x] = array[x + 1];
				array[x + 1] = temp;
			}
		}
	}
	//the final array
	cout << "\nArray after sorting: ";
	for (x = 1; x < 6; x++)
	{
		cout << " " << array[x] << ",";
	}
	_getch();
}
//OUTPUT:
//Enter any 5 numbers in array:
//Enter Array Number 1 : 4
//Enter Array Number 2 : 7
//Enter Array Number 3 : 8
//Enter Array Number 4 : 2
//Enter Array Number 5 : 3
//Array before sorting : 4, 7, 8, 2, 3,
//Array after sorting : 2, 3, 4, 7, 8,
