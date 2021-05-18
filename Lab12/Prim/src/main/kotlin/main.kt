fun Int.checkPrime() : Boolean {
    var i = 2
    while (i <= this/2) {
        if (this % i == 0)
            return false;

        i++
    }
    return true;
}

fun main() {
    val n1 = 3
    val n2 = 6
    val n3 = 13
    val res1 = n1.checkPrime()
    if (res1 == true) {
        println("Numarul ${n1} e prim")
    }
    else {
        println("Numarul ${n1} nu e prim")
    }
    val res2 = n2.checkPrime()
    if (res2 == true) {
        println("Numarul ${n2} e prim")
    }
    else {
        println("Numarul ${n2} nu e prim")
    }
    val res3 = n3.checkPrime()
    if (res3 == true) {
        println("Numarul ${n3} e prim")
    }
    else {
        println("Numarul ${n3} nu e prim")
    }
}