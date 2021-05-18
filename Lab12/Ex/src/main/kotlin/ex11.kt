fun String.toPascalCase0(): String {
    val components = this.split(" ")
    var result: String = ""
    for(component in components) {
        result += component.capitalize()
    }
    return result
}
fun String.toPascalCase1(): String = this.split("").map{it.capitalize()}.joinToString(separator="")
fun String.toPascalCase2(): String = this.split("").joinToString(separator = "") { it.capitalize() }
val toPascalCase0 = {str: String -> str.split("").map{it.capitalize()}.joinToString(separator="")}
val toPascalCase1 = {str: String -> str.split("").joinToString(separator = "") { it.capitalize() } }
fun main() {
    println("Functii extensie: ")
    println("whatever name you want".toPascalCase0())
    println("whatever name you want".toPascalCase1())
    println("whatever name you want".toPascalCase2())
    println("Expresii lambda stocate in variabile: ")
    println(toPascalCase0("whatever name you want"))
    println(toPascalCase1("whatever name you want"))
}