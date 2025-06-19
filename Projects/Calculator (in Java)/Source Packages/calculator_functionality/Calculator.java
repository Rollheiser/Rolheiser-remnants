package calculator_functionality;
import java.util.Scanner;

public class Calculator extends Operations {
    private Scanner input = new Scanner(System.in);

    public void receiveData() {
        while (true) {
            System.out.println("Enter the first number: ");
            
            if (input.hasNextInt()) {
                this.num1 = input.nextFloat();
            } else {
                System.out.println("Error: Invalid, enter a valid number.");
                input.next();
                continue;
            }
            
            System.out.println("Enter the second number: ");
            
            if (input.hasNextInt()) {
                this.num2 = input.nextFloat();
                break;
            } else {
                System.out.println("Error: Invalid, enter a valid number.");
                input.next();
            }
        }
    }
    
    public void doOperation() {
        int numOperation;
        
        while (true) {
            System.out.println("Select an operation, type the number of the operation");
            
            System.out.println("1.- Addition.");
            System.out.println("2.- Subtract.");
            System.out.println("3.- Multiplication.");
            System.out.println("4.- Division.");
            System.out.println("5.- Root.");
            System.out.println("6.- Raise to power.");
            System.out.println("7.- Exit.");
            System.out.println();
            
            numOperation = input.nextInt();
            
            if (numOperation == 7) {
                return;
            }
            
            if (numOperation < 1 || numOperation > 7) {
                System.out.println("Error: Introduce a valid option.");
            } else {
                break;
            }
        }
        
        receiveData();
        
        System.out.println();
        switch (numOperation) {
            case 1:
                addition();
                break;
            case 2:
                subtraction();
                break;
            case 3:
                multiplication();
                break;
            case 4:
                division();
                break;
            case 5:
                root();
                break;
            case 6:
                raiseTo();
                break;
        }
    }
}
