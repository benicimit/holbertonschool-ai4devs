public class Bug4 {
    public static void main(String[] args) {
        // Intended to print numbers from 1 to 10 inclusive
        // Bug: Off-by-one error - loop condition is i < 10 instead of i <= 10

        for (int i = 1; i < 10; i++) {  // This will print 1 to 9
            System.out.println(i);
        }
    }
}