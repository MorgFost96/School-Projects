#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *ptr;
}*t, *t1, *temp;

int topelement();
void push(int data);
void pop();
void empty();
void display();
void destroy();
void stack_count();
void create();

int count = 0;

void main()
{
	int no, ch, e;

	printf("\n 1 - Push");
	printf("\n 2 - Pop");
	printf("\n 3 - Top");
	printf("\n 4 - Empty");
	printf("\n 5 - Exit");
	printf("\n 6 - Display");
	printf("\n 7 - Stack Count");
	printf("\n 8 - Destroy stack");

	create();

	while (1)
	{
		printf("\n Enter choice : ");
		scanf_s("%d", &ch);

		switch (ch)
		{
		case 1:
			printf("Enter data : ");
			scanf_s("%d", &no);
			push(no);
			break;
		case 2:
			pop();
			break;
		case 3:
			if (t == NULL)
				printf("No elements in stack");
			else
			{
				e = topelement();
				printf("\n Top element : %d", e);
			}
			break;
		case 4:
			empty();
			break;
		case 5:
			exit(0);
		case 6:
			display();
			break;
		case 7:
			stack_count();
			break;
		case 8:
			destroy();
			break;
		default:
			printf(" Wrong choice, Please enter correct choice ");
			break;
		}
	}
}

void create()
{
	t = NULL;
}

void stack_count()
{
	printf("\n No. of elements in stack : %d", count);
}

void push(int info)
{
	if (t == NULL)
	{
		t = (struct node *)malloc(1 * sizeof(struct node));
		t->ptr = NULL;
		t->data = info;
	}
	else
	{
		temp = (struct node *)malloc(1 * sizeof(struct node));
		temp->ptr = t;
		temp->data = info;
		t = temp;
	}
	count++;
}


void display()
{
	t1 = t;

	if (t1 == NULL)
	{
		printf("Stack is empty");
		return;
	}

	while (t1 != NULL)
	{
		printf("%d ", t1->data);
		t1 = t1->ptr;
	}
}

void pop()
{
	t1 = t;

	if (t1 == NULL)
	{
		printf("\n Error : Trying to pop from empty stack");
		return;
	}
	else
		t1 = t1->ptr;
	printf("\n Popped value : %d", t->data);
	free(t);
	t = t1;
	count--;
}

int topelement()
{
	return(t->data);
}

void empty()
{
	if (t == NULL)
		printf("\n Stack is empty");
	else
		printf("\n Stack is not empty with %d elements", count);
}

void destroy()
{
	t1 = t;

	while (t1 != NULL)
	{
		t1 = t->ptr;
		free(t);
		t = t1;
		t1 = t1->ptr;
	}
	free(t1);
	t = NULL;

	printf("\n All stack elements destroyed");
	count = 0;
}

//Output 
//
//1 - Push
//2 - Pop
//3 - Top
//4 - Empty
//5 - Exit
//6 - Display
//7 - Stack Count
//8 - Destroy stack
//Enter choice : 1
//Enter data : 10
//
//Enter choice : 1
//Enter data : 20
//
//Enter choice : 1
//Enter data : 30
//
//Enter choice : 1
//Enter data : 40
//
//Enter choice : 2
//
//Popped value : 40
//Enter choice : 3
//
//Top element : 30
//Enter choice : 6
//30 20 10
//Enter choice : 4
//
//Stack is not empty with 3 elements
//Enter choice :