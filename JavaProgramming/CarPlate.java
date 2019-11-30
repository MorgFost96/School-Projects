//Morgan Foster
//Murtz
package carplate;

import java.io.*; 

public class CarPlate implements Serializable { 

private String plateNumber; 
private String state; 
private String color; 

public CarPlate() {}

public CarPlate(String pNumber, String st, String clr) { 
plateNumber = pNumber; 
state = st; 
color = clr; 
} 

public String toString() 
 { 
String s = "plate number: "+plateNumber; 
s += " state: "+state; 
s += " color: "+color; 
return s; 
 } 
}

