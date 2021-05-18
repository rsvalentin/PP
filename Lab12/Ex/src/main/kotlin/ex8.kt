fun getAnotherFunction(n:Int):(String)->Unit {
    return {
        println("n:$n it:$it")
    }
}
fun main() {
    getAnotherFunction(0)("laborator")
    getAnotherFunction(2)("PP")
    getAnotherFunction(3)("Functional Kotlin")
}