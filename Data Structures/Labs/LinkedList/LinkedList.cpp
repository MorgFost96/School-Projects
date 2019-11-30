#include <iostream>
#include <stdlib.h>

using namespace std;

struct ele {
	int value;
	struct ele *next;
};

struct ele *head = NULL;

// The list is stored here
class linklist {
public:

	void display() {
		if (head == NULL) {
			cout << "The list is empty ";
		}
		else {
			struct ele *temp;
			temp = head;
			while (temp != NULL) {
				cout << temp->value << " ";
				temp = temp->next;
			}
			cout << endl;
		}
	}

	//this will add a number to the list
	void add(int a) {
		struct ele *newElement; // add an element to the list and store it 
		newElement = (struct ele *)malloc(sizeof(struct ele));
		newElement->value = a;
		newElement->next = NULL;
		if (head == NULL) { // add to the new element if the head is null
			head = newElement;
		}
		else {
			newElement->next = head;
			head = newElement;
		}
	}
};


int main()
{
	linklist u = linklist();
	int z;
	do {
		cout << "Please enter in a number: ";
		cin >> z;
		if (z != -1) { // If the user add's -1 no list
			u.add(z); // Add's the number 
		}
		u.display(); // Shows the list under the number
	} while (z != -1); //Add's a number until -1 is entered

	system("PAUSE");
	return 0;
}