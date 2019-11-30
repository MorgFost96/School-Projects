using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proj_3
{
    //Node
    public class Node
    {
        public String Name { get; set; }
        public int Data { get; set; }
        public Node Left { get; set; }
        public Node Right { get; set; }
        public Node(string name, int data)
        {
            this.Data = data;
            this.Name = name;
        }
    }

    //Binary Search Tree
    public class BST
    {
        public Node _root;
        int LowWeight = 999;

        public BST()
        {
            _root = null;
        }
        //Return's the root
        public Node ReturnRoots()
        {
            return _root;
        }
        //Insert 
        public void Insert(String name, int data)
        {
            _root = InRec(_root, name, data);
        }
        //Insert's Recursion
        public Node InRec(Node node, string name, int data)
        {
            if (node == null)
            {
                node = new Node(name, data);
            }
            else
            {
                if (name.CompareTo(node.Name) < 1)
                {
                    node.Left = InRec(node.Left, name, data);
                }
                else
                {
                    node.Right = InRec(node.Right, name, data);
                }
            }
            return node;
        }

        //Max height of the tree
        public int MaxHeight()
        {
            return MaxHeight(_root);
        }
        private int MaxHeight(Node _root)
        {
            if (_root == null)
                return -1;
            else
            {
                int LHeight = MaxHeight(_root.Left);
                int RHeight = MaxHeight(_root.Right);
                return 1 + Math.Max(LHeight, RHeight);
            }
        }

        //# of leaves on the BST 
        public int Leaves(Node _root)
        {
            if(_root != null)
            {
                if(_root.Left == null && _root.Right == null)
                {
                    return 1;
                }
                else
                {
                    return Leaves(_root.Left) + Leaves(_root.Right);    
                }
            }
            return 0;
        }

        //Find's/Searches for the lowest weight in the Data
        public int LowData(Node _root)
        {
            if(_root != null)
            {
                if(_root.Data < LowWeight)
                {
                    LowWeight = _root.Data;
                }
                LowData(_root.Left);
                LowData(_root.Right);
            }
            return LowWeight;
        }

    //Find's the first person on the highest point of the tree  
    public String High(Node _root)
        {
            if(_root.Left != null)
            {
                return _root.Name;
            }
            else
            {
                return High(_root.Left);
            }
        }
        //Find's the First Name in Alphabetical Order
        public String LowAlpha(Node _root)
        {
            if (_root.Left == null)
            {
                return _root.Name;
            }
            else
            {
                return LowAlpha(_root.Left);
            }
        }
        //Searching Functionality 
        public Node Searching(Node _root, Node info)
        {
            if(_root == null)
            {
                return null;
            }
            if(_root.Name.Equals(info.Name) && _root.Data == info.Data)
            {
                return _root;
            }
            else if (_root.Name.CompareTo(info.Name) > 1)
            {
                return Searching(_root.Right, info);
            }
            else
            {
                return Searching(_root.Left, info);
            }
        }

        //Order Traversal's
        //Preorder
        public void Preorder(Node root)
        {
            if (root != null)
            {
                Console.WriteLine(root.Name + " - " + root.Data);
                Preorder(root.Left);
                Preorder(root.Right);
            }
        }

        //Inorder
        public void Inorder(Node root)
        {
            if (root != null)
            {
                Inorder(root.Left);
                Console.WriteLine(root.Name + " - " + root.Data);
                Inorder(root.Right);
            }
        }

        //PostOrder
        public void Postorder(Node root)
        {
            if (root != null)
            {
                Postorder(root.Left);
                Postorder(root.Right);
                Console.WriteLine(root.Name + " - " + root.Data);
            }
        }
    }


    //Main
    class Program
    {
        static void Main(string[] args)
        {
            BST theTreeName = new BST();
            theTreeName.Insert("Mike", 100);
            theTreeName.Insert("Tom", 75);
            theTreeName.Insert("Steve", 99);
            theTreeName.Insert("Carry", 58);
            theTreeName.Insert("Stephanie", 82);
            theTreeName.Insert("George", 42);
            Console.WriteLine("Inorder: ");
            theTreeName.Inorder(theTreeName.ReturnRoots());
            Console.WriteLine();
            Console.WriteLine("Preorder: ");
            theTreeName.Preorder(theTreeName.ReturnRoots());
            Console.WriteLine();
            Console.WriteLine("Postorder: ");
            theTreeName.Postorder(theTreeName.ReturnRoots());
            Console.WriteLine();
            Console.WriteLine("Max Height of the Tree: " + theTreeName.MaxHeight());
            Console.WriteLine();
            Console.WriteLine("Number of Leaves on the Tree: " + theTreeName.Leaves(theTreeName.ReturnRoots()));
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("Lowest Weight Contained in the Tree: " + theTreeName.LowData(theTreeName.ReturnRoots()));
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("First name on the Tree: " + theTreeName.High(theTreeName.ReturnRoots()));
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("First name in Alphabetical Order on the Tree: " + theTreeName.LowAlpha(theTreeName.ReturnRoots()));
            Console.WriteLine();
            Console.WriteLine();
            //Searching Functionality Nodes
            Console.WriteLine("Searching for node Mike and John");
            Console.WriteLine();
            Node node = new Node("Mike", 100);
            Node node1 = theTreeName.Searching(theTreeName.ReturnRoots(), node);
            if (node1 != null)
            {
                Console.WriteLine("Mike: Node Found");
            }
            else
                Console.WriteLine("Mike: Node Not Found");
            Console.WriteLine();
            Node node2 = new Node("John", 180);
            Node node3 = theTreeName.Searching(theTreeName.ReturnRoots(), node2);
            if (node3 != null)
            {
                Console.WriteLine("John: Node Found");
            }
            else
                Console.WriteLine("John: Node Not Found");
            Console.WriteLine();
            Console.WriteLine();
        }
    }
}

//Inorder:
//Carry - 58
//George - 42
//Mike - 100
//Stephanie - 82
//Steve - 99
//Tom - 75

//Preorder:
//Mike - 100
//Carry - 58
//George - 42
//Tom - 75
//Steve - 99
//Stephanie - 82

//Postorder:
//George - 42
//Carry - 58
//Stephanie - 82
//Steve - 99
//Tom - 75
//Mike - 100

//Max Height of the Tree: 3

//Number of Leaves on the Tree: 2


//Lowest Weight Contained in the Tree: 42


//First name on the Tree: Mike


//First name in Alphabetical Order on the Tree: Carry


//Searching for node Mike and John

//Mike: Node Found

//John: Node Not Found



