//Morgan Foster
//Murtz
package carplate;
import java.io.*; 
public class TestCarPlate { 
public static void main(String[] args) throws IOException { 

CarPlate plate0 = new CarPlate("ABC 123", "New York", "Silver"); 
CarPlate plate1 = new CarPlate("DEF 567", "Ohio", "White"); 
CarPlate plate2 = new CarPlate("GH 890", "Penn State", "Blue"); 

File f = new File("cardata.tmp"); 
ObjectOutputStream oos = null; 

try { 
FileOutputStream fos = new FileOutputStream(f); 
oos = new ObjectOutputStream(fos); 
oos.writeObject(plate0); 
oos.writeObject(plate1); 
oos.writeObject(plate2); 
} catch (IOException e) { 
e.printStackTrace(); 
} finally { 
if (oos != null) oos.close(); 
} // end try 

int c = 0; 
CarPlate cp; 

ObjectInputStream ois = null; 

try { 
FileInputStream fis = new FileInputStream(f); 
ois = new ObjectInputStream(fis); 
while (true) { 
cp = (CarPlate) ois.readObject(); 
System.out.println(cp.toString()); 
c++; 
} // end while 
} catch (EOFException e) { 
System.out.println("Number of objects = " +c); 
} catch (ClassNotFoundException e) { 
System.out.println("Class not found"); 
} finally { 
if (ois != null) ois.close(); 
} 
}  
} 
