#include <iostream>
using namespace std;

class BinaryTreeLab
{
private:
	int count;
	int *dataArray;
	int siz;
public:
	BinaryTreeLab() {
		dataArray = new int[10];
		siz = 10;
		count = 0;
	}

	void push(int n)
	{
		if (count < siz)
		{
			dataArray[count++] = n;
		}
		else
		{
			siz = siz * 2;
			int *temp = new int[siz];
			for (int i = 0; i < count; i++)
			{
				temp[i] = dataArray[i];
			}
			delete[] dataArray;
			dataArray = temp;
			dataArray[count++] = n;
		}
	}

	void preorder(int i)
	{
		if (i < count)
		{
			cout << dataArray[i] << " ";
			preorder(2 * i + 1);
			preorder(2 * i + 2);
		}
	}
};


int main()
{
	BinaryTreeLab btl;
	for (int i = 0; i < 20; i++)
	{
		btl.push(i);
	}
	btl.preorder(0);
	cout << endl;
	system("PAUSE");
	return 0;
}