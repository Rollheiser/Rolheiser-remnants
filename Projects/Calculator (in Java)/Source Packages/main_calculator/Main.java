package main_calculator;

import java.util.Scanner;
import calculator_functionality.Calculator;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Welcome to my calculator.");
        System.out.println("In this program, you'll be able to: add, subtract, multiply, divide, find the root, and raise to the power.");
        System.out.println("Do you want to proceed? Type \"yes\" or \"no\"");
        
        String answer = sc.nextLine();
        
        if (answer.equals("yes") || answer.equals("Yes")) {
            System.out.println("Great, let's start");
        }
        
        if (answer.equals("no") || answer.equals("No")) {
            return;
        }
        
        Calculator calculator = new Calculator();
        
        calculator.doOperation();
        System.out.println("The result is: " + calculator.getResult());
    }
}
