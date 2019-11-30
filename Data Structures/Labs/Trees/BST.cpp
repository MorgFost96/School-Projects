#include<stdio.h>
#include<stdlib.h>
struct node
{
	int key;
	struct node *left, *right;
};
struct node *newNode(int item)
{
	struct node *temp = (struct node *)malloc(sizeof(struct node));
	temp->key = item;
	temp->left = temp->right = NULL;
	return temp;
}
void inorder(struct node *root)
{
	if (root != NULL)
	{
		inorder(root->left);
		printf("%d \n", root->key);
		inorder(root->right);
	}
}
struct node* add(struct node* node, int key)
{
	if (node == NULL) return newNode(key);
	if (key < node->key)
		node->left = add(node->left, key);
	else if (key > node->key)
		node->right = add(node->right, key);
	return node;
}
int main()
{
	struct node *root = NULL;
	root = add(root, 7);
	add(root, 2);
	add(root, 1);
	add(root, 4);
	add(root, 6);
	add(root, 5);
	add(root, 10);
	inorder(root);
	system("PAUSE");
	return 0;
}