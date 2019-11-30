
package vehicle;

public class MoorizedVehicle extends Vehicle {
        private String ownerName;       
        private int numWheels;         
        private double engineSize;      
        public MoorizedVehicle() {}
        public MoorizedVehicle(String name, int wheels, double size) 
        {
                this.ownerName = name;
                this.numWheels = wheels;
                this.engineSize = size;
        }
        public String getOwnerName() {
                return this.ownerName;
        }
        public int getNumWheels() {
                return this.numWheels;
        }
        public double getEngineSize() {
                return this.engineSize;
        }
        public double getHorsePower() {
                return (this.engineSize * this.numWheels);
        }
}
