package vehicle;
public class TestVehicle {
        public static void main(String[] args) {
                Bicycle racer = new Bicycle("BOBO");
                System.out.println("Owner = "+racer.getOwnerName());
                System.out.println("Wheels = "+racer.getNumWheels());
                MoorizedVehicle car = new MoorizedVehicle("Billy Bob", 8, 2.4);         
                System.out.println("Vehicle owner = "+car.getOwnerName());
                System.out.println("Wheels = "+car.getNumWheels());
                System.out.println("Engine size (in litres) = "+car.getEngineSize());
                System.out.println("Horse Power = "+ car.getHorsePower());
 
        }
}
/*run:
Owner = BOBO
Wheels = 2
Vehicle owner = Billy Bob
Wheels = 8
Engine size (in litres) = 2.4
Horse Power = 19.2
BUILD SUCCESSFUL (total time: 0 seconds)
