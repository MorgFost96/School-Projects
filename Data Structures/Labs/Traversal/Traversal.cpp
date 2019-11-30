#include<iostream>
#define max 100

using namespace std;


class binarytree
{
private:
	int data[max];
	int count;
public:
	binarytree();
	void add(int);
	void preorder(int);
	void postorder(int);
	void inorder(int);
};

binarytree::binarytree()
{
	count = 0;
}

void binarytree::add(int dataone)
{
	data[count] = dataone;
	count++;
}

void binarytree::preorder(int i)
{
	if (i<count)
	{
		cout << " " << data[i] << endl;
		preorder(2 * i + 1);
		preorder(2 * i + 2);
	}
}
void binarytree::postorder(int i)
{
	if (i<count)
	{
		postorder(2 * i + 1);
		postorder(2 * i + 2);
		cout << " " << data[i] << endl;
	}
}
void binarytree::inorder(int i)
{
	if (i<count)
	{
		inorder(2 * i + 1);
		cout << " " << data[i] << endl;
		inorder(2 * i + 2);
	}
}

int main()
{
	binarytree tree;
	tree.add(10);
	tree.add(20);
	tree.add(30);
	tree.add(40);
	tree.add(50);
	tree.add(60);
	tree.add(70);
	tree.add(80);
	tree.add(90);
	tree.preorder(0);
	cout << "Post Order: " << endl;
	tree.postorder(0);
	cout << "In Order: " << endl;
	tree.inorder(0);
	system("PAUSE");
	return 0;
}