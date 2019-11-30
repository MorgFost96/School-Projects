//Thank you, Professor Cuevas for a nice fall semester :)
//Happy Holidays! 
#include <limits>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

class Node // node class
{
public:
	string varName; // variable name
	int scope; // scope level
	int value; // value
	Node *next; // pointer
	Node(string varName = " ", int scope = 0, int value = 0, Node *link = 0) // default node constructor
	{
		this->varName = varName;
		this->scope = scope;
		this->value = value;
		next = link;
	}
};

const int TABLE_SIZE = 17; // hash table size, as said in SimpleHashTable in Modules it's best to use 17

class HashTable 
{
private:
	Node **table;
public:
	HashTable() // deafult constructor that creates an table of objects with null value
	{
		table = new Node*[TABLE_SIZE];
		for (int i = 0; i < TABLE_SIZE; i++)
			table[i] = NULL;
	}

	void insert(string varName = " ", int scope = 0, int value = 0, Node *link = 0) // insert method with default values
	{
		int total = 0;
		for (int i = 0, l = 1; i < varName.length(); i++, l++) // first part of hash key
		{
			total += l * int(varName[i]);
		}
		int hash = (total % TABLE_SIZE); // total table size to get hash key
		if (table[hash] == NULL) // if it is empty = new node 
			table[hash] = new Node(varName, scope, value, link);
		else
		{
			Node *tempNode = table[hash];
			while (tempNode->next != NULL)  
				tempNode = tempNode->next;
			tempNode->next = new Node(varName, scope, value, link);
		}
	}

	void print(string varName, int scope, string operation = " ", int amount = 0) //Print Class
	{
		int total = 0;
		for (int i = 0, l = 1; i < varName.length(); i++, l++) // same as insert to get hash key to know where to begin
		{
			total += l * int(varName[i]);
		}
		int hash = (total % TABLE_SIZE); // hash key
		Node *tempNode = table[hash]; // temp node to traverse
		while (tempNode != NULL && tempNode->next != NULL) // to get to the end of the list
			tempNode = tempNode->next;
		if (tempNode == NULL) // if name hash resulted in a value that isn't in the table, it would be empty thus value would be undefined
			cout << varName << " UNDEFINED" << endl;
		else if (tempNode->varName == varName && tempNode->scope <= scope)
			cout << tempNode->varName << " is " << tempNode->value << endl;
		else // the value isn't in scope
			cout << varName << " NOT IN SCOPE " << endl;
	}

	void arithmetic(string varName, int scope, string arithmetic, int amount = 0)
	{
		int total = 0;
		for (int i = 0, l = 1; i < varName.length(); i++, l++)
		{
			total += l * int(varName[i]);
		}
		int hash = (total % TABLE_SIZE); // get hash key
		Node *tempNode = table[hash]; // temp node to traverse
		while (tempNode != NULL && tempNode->next != NULL) // traverse 
			tempNode = tempNode->next;
		if (tempNode == NULL) // if the node is null, the variable wasn't defined 
			cout << varName << " UNDEFINED " << endl;
		else
		{
			if (tempNode->varName == varName && tempNode->scope <= scope) 
			{
				if (arithmetic == "++") // post increment
					tempNode->value++;
				else if (arithmetic == "--") // post decrement
					tempNode->value--;
				else if (arithmetic == "=") // assign a value
					tempNode->value = amount;
				else if (arithmetic == "*") // multiply 
					cout << tempNode->varName << ' ' << arithmetic << ' ' << amount << " is " << tempNode->value * amount << endl;
				else if (arithmetic == "+") // add
					cout << tempNode->varName << ' ' << arithmetic << ' ' << amount << " is " << tempNode->value + amount << endl;
				else if (arithmetic == "-") // sub
					cout << tempNode->varName << ' ' << arithmetic << ' ' << amount << " is " << tempNode->value - amount << endl;
				else if (arithmetic == "/") // divide
					cout << tempNode->varName << ' ' << arithmetic << ' ' << amount << " is " << tempNode->value / amount << endl;
				else if (arithmetic == "%") // modulo
					cout << tempNode->varName << ' ' << arithmetic << ' ' << amount << " is " << tempNode->value % amount << endl;
				else if (arithmetic == "^") // exponent
					cout << tempNode->varName << ' ' << arithmetic << ' ' << amount << " is " << pow(double(tempNode->value), amount) << endl;
			}
			else
				cout << varName << " NOT IN SCOPE " << endl;
		}
	}
};

int main(void)
{
	HashTable borg; // hashtable
	int level = 0; // scope level
	string word; // holds current word from file
	string name; // to temp store stream words
	string operation; // to hold operation
	string temp; // temp holder 
	int num; // value for variable
	ifstream stream("Borg.txt"); // read from txt file
	while (!stream.eof()) // keep reading while not at the end of the file
	{
		if (!temp.empty()) // to see if temp is holding anything 
			temp = ""; // if it isn't empty set it back to zero so it can be used again
		else
			stream >> word; // or else get next word in file
		if (word == "COM") // comment line
			stream.ignore(numeric_limits<streamsize>::max(), '\n');
		else if (word == "START") // increases scope level
			level++;
		else if (word == "FINISH") // decreases scope level
			level--;
		else if (word == "VAR") // instantiate a new node for the hash table
		{
			stream >> word;
			name = word;
			stream >> word;
			stream >> word;
			istringstream stm;
			stm.str(word); // converts the string into an int to be passed on
			stm >> num;
			borg.insert(name, level, num); // calls an insert method and passes to the current values
		}
		else if (word == "PRINT") // prints the data
		{
			stream >> word;
			name = word;
			stream >> word;
			if (word == "*" || word == "/" || word == "+" || word == "-" || word == "%" || word == "^") // for when we are printing and performing an operation
			{
				operation = word;
				stream >> word;
				istringstream stm;
				stm.str(word);
				stm >> num;
				borg.arithmetic(name, level, operation, num); // call for the arithmetic function
			}
			else // when we are only printing
			{
				borg.print(name, level); // calls for the print function
				temp = word; // temp to check at the end
			}
		}
		else // default case where we are simply using pre or post increment or new value
		{
			name = word;
			stream >> word;
			if (word == "++" || word == "--") // pre/post Incerements
				borg.arithmetic(name, level, word); // Txt file calling to Arithmetic
			else if (word == "=") //new value to a variable
			{
				operation = word;
				stream >> word;
				istringstream stm;
				stm.str(word);
				stm >> num;
				borg.arithmetic(name, level, operation, num); // pass data and new values over
			}
			else
				cout << word << endl;
		}
	}
    system("pause");
	return 0;
}

//OUTPUT:
//BORAMIR is 25
//LEGOLAS is 101
//GANDALF UNDEFINED
//BORAMIR * 2 is 52
//BORAMIR + 103 is 129
//BORAMIR - 12 is 14
//BORAMIR / 5 is 5
//BORAMIR % 8 is 2
//BORAMIR ^ 3 is 17576
//GANDALF is 49
//BORAMIR is 26
//GANDALF NOT IN SCOPE
//LEGOLAS is 1000
//LEGOLAS is 1000
//LEGOLAS is 999
//GANDALF is 49
