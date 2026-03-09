public class Bug4 {
    public static void main(String[] args) {
        // Type: Off-by-one Error
        // Intended Behavior: Print numbers 1 through 10 inclusive.
        // Issue: Loop uses i < 10, excluding 10.
        // Notes: Change condition to i <= 10.

        for (int i = 1; i < 10; i++) {  // This will print 1 to 9
            System.out.println(i);
        }
    }
}