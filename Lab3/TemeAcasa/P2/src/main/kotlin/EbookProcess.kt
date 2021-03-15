import java.io.File

class EbookProcess {

    fun editText(text: String): String {

        // eliminate multiple newlines
        var text = text.replace("[\r\n]+".toRegex(), "\n")

        // remove multiples whitespace
        text = text.replace("\\s+".toRegex(), " ")

        //remove page number
        text = text.replace("\\s+\\d+\\s+".toRegex(), "\n")

        //remove capitol
        text = text.replace("\\s+Capitolul.*\\s+".toRegex(), "\n")

        return text;


    }
    fun readFromFile(fp: File) : String {
        return fp.inputStream().readBytes().toString(Charsets.UTF_8)
    }
}

fun main() {
    val readPath = File("Ebook.txt")
    val editText = EbookProcess();
    var story: String = editText.readFromFile(readPath)
    story = (editText.editText(story))
    print(story)
}