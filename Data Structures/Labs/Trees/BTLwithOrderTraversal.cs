using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BinaryTreeLab
{

    //Main Class BTree
    class BTreeLab
    {
        private int[] DataArray = new int[50];
        private int count;

        //
        public void BTree()
        {
            count = 0;
        }

        //This will Insert the Data(x) into the Array which contains the given number stored in it and increment the count   
        public void Add(int x)
        {
            DataArray[count] = x;
            count++;
        }

        //Pre-Order Traversal the Function 
        public void Preorder(int i) //VLR
        {
            if (i < count)
            {
                Console.WriteLine(DataArray[i]); //V
                Preorder(2 * i + 1); //left Child
                Preorder(2 * i + 2); //Right Child
            }
        }
        public void inorder(int i)  //LVR
        {
            if (i < count)
            {
                inorder(2 * i + 1); //Left Child
                Console.WriteLine(DataArray[i]); //V
                inorder(2 * i + 2); //Right Child
            }
        }
        public void postorder(int i)
        {
            if( i < count)
            {
                postorder(2 * i + 1); //left Child
                postorder(2 * i + 2); //right child
                Console.WriteLine(DataArray[i]); //V
            }
        }
    }

    //Main Class
    class MainClass
        {
            static void Main(string[] args)
            {
            BTreeLab Tree = new BTreeLab();
            Tree.Add(5);
            Tree.Add(10);
            Tree.Add(20);
            Tree.Add(15);
            Tree.Add(45);
            Tree.Add(30);
            Console.WriteLine("Pre Order: ");
            Tree.Preorder(0);
            Console.WriteLine();
            Console.WriteLine("In Order: ");
            Tree.inorder(0);
            Console.WriteLine();
            Console.WriteLine("Post Order: ");
            Tree.postorder(0);
            }
        }
}
//Pre Order:
//5
//10
//15
//45
//20
//30

//In Order:
//15
//10
//45
//5
//30
//20

//Post Order:
//15
//45
//10
//30
//20
//5