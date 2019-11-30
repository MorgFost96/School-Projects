//Morgan Foster
//1021803
//Murtz
//Java
package threerandomaverages;
import java.util.Random;

public class ThreeRandomAverages {
    public static void main(String[] args) 
    {
    int n1, n2, n3;
    int sum;
    int Avg;
    
    Random random = new Random( );
    n1 = random.nextInt(51);
    n2 = random.nextInt(51);
    n3 = random.nextInt(51);
    sum = n1 + n2 + n3;
    Avg = sum/3;
    System.out.println("The Sum is: " + sum);
    System.out.println("The Average is: " + Avg);
    }
    
}
//run:
//The Sum is: 54
//The Average is: 18
//BUILD SUCCESSFUL (total time: 0 seconds)

//run:
//The Sum is: 76
//The Average is: 25
//BUILD SUCCESSFUL (total time: 0 seconds)