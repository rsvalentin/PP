fun reverse(str: String): String {
    return str.reversed()
}
fun main() {
    println(transform("kotlin", ::reverse))
}