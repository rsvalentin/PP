class Transformer {
    fun upperCased(str: String): String {
        return str.toUpperCase()
    }
    companion object {
        fun lowerCased(str: String): String {
            return str.toLowerCase()
        }
    }
}
fun main() {
    val transformer = Transformer()
    println(transform("kotlin", transformer::upperCased))
    println(transform("kotlin", Transformer.Companion::lowerCased))
}