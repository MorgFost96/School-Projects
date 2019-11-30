//Morgan Foster
//1021802
//Java
//Murtz
package extracredit2;
import java.util.Scanner;
public class ExtraCredit2 
{
    public static void main(String[] args) 
    {
      Double Avg = 0.0;
      Double AtBats = 0.0;
      Double Hits = 0.0;
      String inputStr, StrAvg;
      
      Scanner in = new Scanner(System.in);
      System.out.println("Enter a number of hits and at bats of the player: ");
      AtBats = in.nextDouble();
      Hits = in.nextDouble();
      Avg = Hits/AtBats;
      if(Avg > 300)
          System.out.println("Player is eligible for the All Stars Game! ");
      else 
          System.out.println("player is not eligible.");
            
    
    
    
    }
    
}
//Output
//run:
//Enter a number of hits and at bats of the player: 
//20
//30
//player is not eligible.
//BUILD SUCCESSFUL (total time: 4 seconds)

//run:
//Enter a number of hits and at bats of the player: 
//1
//200000
//Player is eligible for the All Stars Game! 
//BUILD SUCCESSFUL (total time: 4 seconds)