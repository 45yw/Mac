<?php
$n = "2";
for ($i = 1; $i <= 10; $i++) {
    $n = gmp_prob_prime($n);
    echo gmp_strval($n), "\n";
}
