<?php
// Intended to check if a number is prime
// Bug: Logical error - returns true when number is divisible instead of false

function isPrime($n) {
    if ($n <= 1) {
        return false;
    }
    if ($n == 2) {
        return true;
    }
    if ($n % 2 == 0) {
        return false;
    }
    for ($i = 3; $i < $n; $i += 2) {
        if ($n % $i == 0) {
            return true;  // Should be return false
        }
    }
    return true;
}

// Test
$num = 9;
if (isPrime($num)) {
    echo "$num is prime\n";
} else {
    echo "$num is not prime\n";
}
?>