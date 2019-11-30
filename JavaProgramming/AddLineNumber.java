package addlinenumber;
//Morgan Foster
//1021803
//Java Programming
//Murtz
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.PrintWriter;
import java.io.FileOutputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class AddLineNumber {
    public static void main(String[] args)
    {
        try 
        {
         BufferedReader inputStream = 
                 new BufferedReader(new FileReader("dataInput.txt"));
         PrintWriter outputStream =
                 new PrintWriter(new FileOutputStream("NumberedData.txt"));
         
          int count = 0;
          String line = inputStream.readLine( );
          while (line != null)
          {
          count++;
          outputStream.println(count + " " + line);
          line = inputStream.readLine( );
          }
          inputStream.close( );
          outputStream.close( );
        } 
            //end of Try
        
        catch(FileNotFoundException e)
        {
            System.out.println("Problem Opening File");
        }
    catch(IOException e)
    {
    System.out.println("Error Reading from dataInput.txt");
    }
  }
}
//run:
//Problem Opening File
//BUILD SUCCESSFUL (total time: 0 seconds)
