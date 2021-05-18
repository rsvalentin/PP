import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.util.*

fun String.convertDate(formatter:Any): LocalDate? {

    return LocalDate.parse(this, formatter as DateTimeFormatter?)

}

fun main() {


    var datastring="2020-05-22"
    datastring.convertDate(DateTimeFormatter.ISO_DATE);
    print(datastring);
}