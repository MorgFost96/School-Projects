#include <iostream>
#include <stdlib.h>

#define tableSize 27

using namespace std;

int hashTable[tableSize];

int Hash(int n)
{
	return n % tableSize;
}

void add(int n)
{
	int index = Hash(n);

	int count = 0;
	while (count < tableSize)
	{
		if (hashTable[index] == -1)
		{
			hashTable[index] = n;
			break;
		}
		else
		{
			index = (index + 1) % tableSize;
			count++;
		}
	}
}

void printArray()
{
	for (int i = 0; i < tableSize; i++)
	{
		cout << hashTable[i] << " ";
	}
	cout << endl;
}

int lookup(int n)
{
	int index = Hash(n);

	int count = 0;
	while (count < tableSize)
	{
		if (hashTable[index] == n)
		{
			return n;
		}
		else
		{
			index = (index + 1) % tableSize;
			count++;
		}
	}
	return -1;
}

int main()
{
	for (int i = 0; i < tableSize; i++)
	{
		hashTable[i] = -1;
	}

	while (true)
	{
		cout << "\nChoose from the given menu: " << endl;
		cout << "1. Add element to hash" << endl;
		cout << "2. Lookup value in hash" << endl;
		cout << "Enter -1 to quit" << endl;
		int choice;
		cin >> choice;
		if (choice == 1)
		{
			cout << "Enter number to be added: ";
			int n;
			cin >> n;
			add(n);
		}
		else if (choice == 2)
		{
			cout << "Enter number to be searched: ";
			int n;
			cin >> n;
			if (lookup(n) != -1)
			{
				cout << " Found" << endl;
			}
			else
			{
				cout << " Not found." << endl;
			}
		}
		else
		{
			break;
		}
	}
	return 0;
}