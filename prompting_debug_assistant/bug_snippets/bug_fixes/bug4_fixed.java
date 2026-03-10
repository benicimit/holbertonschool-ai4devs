public class Bug4 {
    public static void main(String[] args) {
        // Type: Off-by-One Error
        // Intended Behavior: Print numbers from 1 to 10 inclusive.
        // Issue: Loop excludes the upper bound (10).
        // Notes: Should use <= instead of < for inclusive upper bound.
        for (int i = 1; i <= 10; i++) {  // Fixed: changed < to <=
            System.out.println(i);
        }
    }
}