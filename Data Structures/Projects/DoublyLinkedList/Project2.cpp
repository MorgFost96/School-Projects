#include <iostream>
#include <iomanip>
#include <sstream>

using namespace std;

class Node
{
public:
	string name;
	int weight;
	Node *next;
	Node *prev;
	Node *wNext;
	Node *wPrev;

	Node(string newName, int newWeight)
	{
		name = newName;
		weight = newWeight;
	}
}*head, *weightHead;

//Doubly Linked List
class DLL
{
public:
	void makeList(string n, int w);
	void insertion(string n, int w);
	void insertStart(string n, int w);
	void insertAfter(string n, int w);
	void checkWeight(Node *);
	void printNames();
	void printWeights();
	DLL()
	{
		head = NULL;
	}
};

//Making of the List
void DLL::makeList(string n, int w)
{
	Node *h, *temp, *wH;
	temp = new Node(n, w);
	temp->next = NULL;
	if (head == NULL)
	{
		temp->prev = NULL;
		head = temp;
		weightHead = temp;
	}
	else
	{
		h = head;
		while (h->next != NULL)
		{
			h = h->next;
		}
		h->next = temp;
		temp->prev = h;
	}
}

void DLL::insertion(string n, int w)
{
	Node *temp, *h, *wH;
	h = head;
	wH = weightHead;
	temp = new Node(n, w);
	if (temp->name < h->name)
	{
		insertStart(n, w);
		return;
	}
	else
	{
		if (h->next == NULL)
		{
			insertAfter(n, w);
			return;
		}
		while (h->next != NULL)
		{
			h = h->next;
			if (h->next == NULL || temp->name > h->next->name)
			{
				insertAfter(n, w);
				return;
			}
		}
	}
}

void DLL::insertStart(string n, int w)
{
	Node *temp = new Node(n, w);
	temp->prev = NULL;
	temp->next = head;
	head->prev = temp;
	head = temp;

	checkWeight(temp);
}

void DLL::insertAfter(string n, int w)
{
	Node *temp, *h, *wH;
	h = head;
	wH = weightHead;
	temp = new Node(n, w);
	//Add to next place in list
	if (h->next == NULL)
	{
		h->next = temp;
		temp->next = NULL;
		temp->prev = h;
		checkWeight(temp);
	}
	else
	{
		while (h->next != NULL)
		{
			h = h->next;
			//changes head if it's higher up
			if (temp->name < h->name)
			{
				temp->next = h;
				temp->prev = h->prev;
				temp->next->prev = temp;
				temp->prev->next = temp;
				checkWeight(temp);
				return;
			}
			//Otherwise just add it to the end
			else if (h->next == NULL)
			{
				h->next = temp;
				temp->prev = h;
				checkWeight(temp);
				return;
			}
		}

	}
}

void DLL::checkWeight(Node *temp)
{
	Node *wH = weightHead;
	//uses the heavier weight
	if (wH->weight < temp->weight)
	{
		while (wH->wNext != NULL && wH->weight < temp->weight)
		{
			wH = wH->wNext;
		}
		if (wH->weight > temp->weight)
		{
			temp->wNext = wH;
			temp->wPrev = wH->wPrev;
			temp->wPrev->wNext = temp;
			temp->wNext->wPrev = temp->wPrev;
		}
		else
		{
			temp->wNext = NULL;
			temp->wPrev = wH;
			temp->wPrev->wNext = temp;
			return;
		}
	}

	else
	{
		temp->wNext = wH;
		temp->wPrev = NULL;
		temp->wNext->wPrev = temp;
		weightHead = temp;
	}
	return;
}

void DLL::printNames()
{
	Node *temp = head;
	cout << "\nNames in order:\n";
	while (temp != NULL)
	{
		cout << temp->name << " - " << temp->weight << endl;
		temp = temp->next;
	}
}
void DLL::printWeights()
{
	Node *temp = weightHead;
	cout << "\nWeights in order:\n";
	while (temp != NULL)
	{
		cout << temp->name << " - " << temp->weight << endl;
		temp = temp->wNext;
	}
}

int main()
{
	DLL *roster = new DLL();
	string name;
	int weight;

	//the first person
	cout << "Enter first name: ";
	cin >> name;
	cout << "And first weight: ";
	cin >> weight;
	cout << endl;
	roster->makeList(name, weight);

	//loop the name and weight of the 14 people + one extra person
	for (int i = 0; i < 15; i++)
	{
		cout << "Enter next name: ";
		cin >> name;
		cout << "And next weight: ";
		cin >> weight;
		cout << endl;
		roster->insertion(name, weight);
	}

	roster->printNames();
	roster->printWeights();
	system("PAUSE");
}



//
//Enter first name : Jim
//And first weight : 150
//
//Enter next name : Tom
//And next weight : 212
//
//Enter next name : Michael
//And next weight : 174
//
//Enter next name : Abe
//And next weight : 199
//
//Enter next name : Richard
//And next weight : 200
//
//Enter next name : April
//And next weight : 117
//
//Enter next name : Claire
//And next weight : 124
//
//Enter next name : Bobby
//And next weight : 109
//
//Enter next name : Bob
//And next weight : 156
//
//Enter next name : Kevin
//And next weight : 145
//
//Enter next name : Jason
//And next weight : 182
//
//Enter next name : Brian
//And next weight : 150
//
//Enter next name : Chris
//And next weight : 175
//
//Enter next name : Steven
//And next weight : 164
//
//Enter next name : Annabelle
//And next weight : 99
//
//Enter next name : Jo
//And next weight : 132
//
//
//Names in order :
//Abe - 199
//Annabelle - 99
//April - 117
//Bob - 156
//Bobby - 109
//Brian - 150
//Chris - 175
//Claire - 124
//Jason - 182
//Jim - 150
//Jo - 132
//Kevin - 145
//Michael - 174
//Richard - 200
//Steven - 164
//Tom - 212
//
//Weights in order :
//Annabelle - 99
//Bobby - 109
//April - 117
//Jo - 132
//Kevin - 145
//Jim - 150
//Brian - 150
//Steven - 164
//Chris - 175