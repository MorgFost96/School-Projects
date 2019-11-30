//Mfoster
//1021803
//Murtz 
//Java Class
package restaurantclient;

public class RestaurantClient { 
public static void main(String[] args) { 
Restaurant one = new Restaurant("Carls Jr.", 100, 200); 

double taxableAmount = one.getTaxableAmount(); 
double expected = (100 * 0.1 * 200); 

assert (expected == taxableAmount) : String.format("Expected <%f> but was <%f>" , expected + 1, taxableAmount); 

System.out.println("The Taxable Amount is: " + taxableAmount);	
} 
} 

class Store { 
protected final double TAX_RATE = 0.1; 
private String name; 

public Store(String name) { 
setName(name); 
} 

public String getName() { 
return name; 
} 

public void setName(String name) { 
this.name = name; 
} 
} 

class Restaurant extends Store { 
private int numberOfCustomer; 
private double averagePricePerCustomer; 

public Restaurant(String name, int numberOfCustomer, 
double averagePricePerCustomer) { 
super(name); 
setNumberOfCustomer(numberOfCustomer);
setAveragePricePerCustomer(averagePricePerCustomer); 
} 

public int getNumberOfCustomer() { 
return numberOfCustomer; 
} 

public void setNumberOfCustomer(int numberOfCustomer) { 
this.numberOfCustomer = numberOfCustomer; 
} 

public double getAveragePricePerCustomer() { 
return averagePricePerCustomer; 
} 

public void setAveragePricePerCustomer(double averagePricePerCustomer) { 
this.averagePricePerCustomer = averagePricePerCustomer; 
} 

public double getTaxableAmount() { 
double result = 0; 
result = this.getNumberOfCustomer() * this.getAveragePricePerCustomer() 
* super.TAX_RATE; 
return result; 
} 
}