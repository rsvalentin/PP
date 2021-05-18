fun <T> emit(t: T, vararg listeners: (T) -> Unit) = listeners.forEach{ listener ->listener(t)}

fun main() {
    emit(1, ::println, {i -> println(i * 2)})
    emit(
        listOf('a', 'b', 'c'),
        ::println,{list -> println(list.joinToString(prefix="<",
                                                     postfix=">",
                                                     separator=""))})}