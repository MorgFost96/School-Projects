#include <iostream>
#include <cstdlib>
using namespace std;

struct int_node
{
	int data;
	int_node* next;
};
void insert(int_node** head_ref, int new_data);
void printList(int_node *head);

int main()
{
	int_node* head = NULL;
	string option;
	int num;

	cout << "Please enter in a number, then press -1 to stop: " << endl;

	while (1) 
	{
		cin >> num;
		if (num == -1)
			break;

		insert(&head, num);
	}
	printList(head);

	return 0;
}

void insert(int_node** head_ref, int new_data)
{
	int_node* node = new int_node;
	node->data = new_data;
	node->next = NULL;

	int_node* current;
	if (*head_ref == NULL || (*head_ref)->data >= node->data)
	{
		node->next = *head_ref;
		*head_ref = node;
	}
	else
	{
		current = *head_ref;
		while (current->next != NULL && current->next->data < node->data)
		{
			current = current->next;
		}
		node->next = current->next;
		current->next = node;
	}
}


void printList(int_node *head)
{
	int_node *temp = head;

	while (temp != NULL)
	{
		cout << temp->data << " " ;
		temp = temp->next;
	}
	cout << endl;
	system("PAUSE");
}

//Output
//Please enter in a number, then press - 1 to stop :
//3
//2
//8
//9
//14
//13
//10
//11
//21
//- 1
//2 3 8 9 10 11 13 14 21