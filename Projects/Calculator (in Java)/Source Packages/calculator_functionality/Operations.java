package calculator_functionality;

// This class will contain the operations of a normal calculator
public class Operations {
    protected float num1, num2, result;
    
    public void addition() {
        this.result = this.num1 + this.num2;
    }
    
    public void subtraction() {
        this.result = this.num1 - this.num2;
    }
    
    public void multiplication() {
        this.result = this.num1 * this.num2;
    }
    
    public void division() {
        try {
            this.result = this.num1 / this.num2;
        } catch (Exception e) {
            System.out.println("Error: Zero division error or invalid.");
        }
    }
    
    public void root() {
        this.result = (float) (Math.pow(this.num2, 1.0 / this.num1));
    }
    
    public void raiseTo() {
        this.result = (float) (Math.pow(this.num1, this.num2));
    }
    
    public float getResult() {
        return this.result;
    }
}
