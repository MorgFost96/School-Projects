//Morgan Foster
//1021803
package extracredit3;

public class ExtraCredit3 
{
  public static void main(String[] args)
    {
        Grade cone = new Grade("Java", 90);
        String c1 = cone.getCN();
        System.out.println("Course Name: " + c1.toString());
        System.out.println("");
        Grade ct = new Grade("Java", 80);
        String c2 = cone.getCN();
        System.out.println("Course Name: " + c2.toString());
        System.out.println("");
        Grade cth = new Grade("Java", 70);
        String c3 = cone.getCN();
        System.out.println("Course Name: " + c3.toString());
        System.out.println("");
        Grade cf = new Grade("Java", 60);
        String c4 = cone.getCN();
        System.out.println("Course Name: " + c4.toString());
        System.out.println("");
        Grade cfi = new Grade("Java", 0);
        String c5 = cone.getCN();
        System.out.println("Course Name: " + c5.toString());
        System.out.println("");
        Grade cs = new Grade();
        cs.setCourse("Java");
        cs.setGrade(-1);
        String c6 = cone.getCN();
    }
}

/*run:
//Course Name is Java
//Grade can't be Negative
//Your Grade is A
//Course Name: Java

//Course Name is Java
//Your Grade is B
//Course Name: Java
//
Course Name is Java
Your Grade is C
Course Name: Java

Course Name is Java
Your Grade is D
Course Name: Java

Course Name is Java
Your Grade is F
Course Name: Java

BUILD SUCCESSFUL (total time: 0 seconds)
