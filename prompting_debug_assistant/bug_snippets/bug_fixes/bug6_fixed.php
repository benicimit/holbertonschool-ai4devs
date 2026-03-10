<?php
function isPrime($num) {
    if ($num <= 1) {
        return false;
    }
    for ($i = 2; $i * $i <= $num; $i++) {
        if ($num % $i == 0) {
            return false;  // Fixed: changed return true to return false
        }
    }
    return true;
}

// Type: Logical Error
// Intended Behavior: Check if a number is prime.
// Issue: Returning true when a divisor is found.
// Notes: Should return false when a divisor is found, true otherwise.
$number = 7;
if (isPrime($number)) {
    echo "$number is prime\n";
} else {
    echo "$number is not prime\n";
}
?>