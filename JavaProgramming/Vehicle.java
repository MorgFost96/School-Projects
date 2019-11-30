//Morgan Foster
//Murtz
package vehicle;
public abstract class Vehicle {
        private String ownerName;
        private int numWheels;
        public Vehicle() 
        {}
        public Vehicle(String name, int wheels) { //Ovl
                this.ownerName = name;
                this.numWheels = wheels;
        }
}
