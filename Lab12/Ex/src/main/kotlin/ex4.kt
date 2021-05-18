fun <T> transform(t: T, fn: (T) -> T): T {
    return fn(t)
}

fun main() {
    println(transform("kotlin", { str: String -> str.capitalize() }))
    println(transform("kotlin", { it.capitalize() }))
}