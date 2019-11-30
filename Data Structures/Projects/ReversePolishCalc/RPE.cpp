//Morgan Foster
//Program 1
//Data Structures 


//The program will take in a Polish expression that separates 
//the operators and operands by a single space,
//and terminates the expression with an equals sign.

#include <iostream>
#include <iostream>
#include <string.h>
#include <sstream>
#include <stdlib.h>
using namespace std;

//Linked List Structure
struct node {
	float data;
	struct node *next; //Pointer to the next node
};

class stack {
	struct node *top; //will point to the top element in the stack
public: stack() {
	top = NULL;
}
		void push(float element);
		float pop();
		float peek();
		bool isEmpty();
		int size();

};

bool stack::isEmpty() {
	if (top == NULL) {
		return true;
	}
	return false;
}

float stack::peek() {
	if (top == NULL) {
		cout << "Error : empty stack";
	}
	return top->data;
}
//Push the data into the stack
void stack::push(float element) {
	struct node *newNode; //creates a new node for data and assigns it to the top pointer of the new node
	newNode = new node;
	newNode->data = element;
	newNode->next = NULL;
	if (top != NULL)
		newNode->next = top;
	top = newNode;
}
//Pop's to the top of the element 
float stack::pop() {
	struct node *temp;
	if (top == NULL) {
		cout << "Error : empty stack";
	}
	temp = top;
	top = top->next;
	float value = temp->data;
	delete temp;
	return value;
}
//the Size of the element
int stack::size() {
	struct node *temp;
	temp = top;
	int count = 0;
	while (temp != NULL) {
		count = count + 1;
		temp = temp->next;
	}
	return count;
}

//the main
int main() {
	while (1) {
		stack s;
		float first, second;
		string input, str1;

		getline(cin, input);  
		istringstream is(input);

		if (input == "0") {
			return 0;
		}

		bool flag = true;
		for (; is >> str1;) {
			//if the input character is an operator,
			//then pop two elements from the stack,
			//apply operator and push the result into
			//the stack going 
			if (str1.compare("+") == 0) {
				if (s.size() < 2) {
					cout << "Error: Too Many Operators\n";
					flag = false;
					break;
				}
				second = s.pop();
				first = s.pop();
				s.push(first + second);
			}
			else if (str1.compare("-") == 0) {
				if (s.size() < 2) {
					cout << "Error: Too Many Operators\n";
					flag = false;
					break;
				}
				second = s.pop();
				first = s.pop();
				s.push(first - second);
			}
			else if (str1.compare("*") == 0) {
				if (s.size() < 2) {
					cout << "Error: Too Many Operators\n";
					flag = false;
					break;
				}
				second = s.pop();
				first = s.pop();
				s.push(first * second);
			}
			else if (str1.compare("/") == 0) {
				if (s.size() < 2) {
					cout << "Error: Too Many Operators\n";
					flag = false;
					break;
				}
				second = s.pop();
				first = s.pop();
				if (second == 0) { //check division by zero
					cout << "Error: Division by zero\n";
					flag = false;
					break;
				}
				s.push(first / second);
			}
			else {
				s.push(strtof(str1.c_str(), NULL));
			}
		}
		//checks to see the size of the operands
		if (s.size() == 1 && flag) {
			cout << s.pop(); cout << "\n";
		}
		else if (s.size() > 1) {
			cout << "Error: Too Many Operands\n";
		}
	}
}

//Output 
//10 15 +
//25
//10 15 -
//-5
//2.5 3.5 +
//6
//10 0 /
//Error: Division by zero
//10 20 * /
//Error : Too Many Operators
//12 20 30 /
//Error : Too Many Operands
//- 10 - 30 -
//20
//100 10 50 25 / *--2 /
//-40
//