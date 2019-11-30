
package vehicle;

public class Bicycle extends Vehicle {
        private String ownerName;
        private int numWheels;
        public Bicycle() {}
        public Bicycle(String name) {
                ownerName = name;
                numWheels = 2;
        }
        public String getOwnerName() {
                return this.ownerName;
        }
        public int getNumWheels() {
                return this.numWheels;
        }
}
