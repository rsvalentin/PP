fun <T>varargFun(vararg items: T) {
    items.forEach(::println)
}
fun main() {
    varargFun(1)
    varargFun(1.1, 2.2)
    varargFun("Cristina", "Andrei", "Roxana")
}