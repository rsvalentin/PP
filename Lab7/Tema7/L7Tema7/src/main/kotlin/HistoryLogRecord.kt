import java.io.File
import java.sql.Timestamp

fun main() {
    val metaList = mutableListOf<String>()
    File("/var/log/apt/history.log")
        .forEachLine {
           if (it.contains("Start-Date") or it.contains("Commandline")) {
               metaList.add(it)
           }
        }
    val timeStampList = mutableListOf<String>()
    val commandsList = mutableListOf<String>()
    for (i in metaList.indices) {
        if (metaList[i].startsWith('S')) {
            val string = metaList[i].substring(12)
            val date = Timestamp.valueOf(string.replace(" +".toRegex(), " "))
            timeStampList.add(date.toString())
        }
        else if (metaList[i].startsWith('C')){
            val string = metaList[i].substring(13)
            commandsList.add(string)
        }
    }
    println("timestampList is $timeStampList")
    println("\n")
    println("commandslist is $commandsList")
    println("\n")
    println("metalist is $metaList")
    println("\n")
    val obj1 = HistoryLogRecord(timeStampList[0], commandsList[0])
    val obj2 = HistoryLogRecord(timeStampList[1], commandsList[1])
    val obj3 = HistoryLogRecord(timeStampList[2], commandsList[2])
    val res = obj1.compareTo(obj2)
    println("\nTimestamp-ul obj1: " + obj1.timeStamp)
    println("Timestamp-ul obj2: " + obj2.timeStamp)
    println("Maximul il reprezinta cea mai recenta data. < 0 => obj1 date is before obj2 date, =0 => dates are equal, >0 => obj1 date is after obj2 date: Res =  $res")

    println("\nTimestamp-ul obj1: " + obj1.timeStamp)
    println("Timestamp-ul obj2: " + obj2.timeStamp)
    val obj4 = maxim<HistoryLogRecord>(obj1, obj2)
    println("Maximul este " +obj4.timeStamp)
    println("\n")

    val mutableHashMap: MutableMap<String, HistoryLogRecord> = mutableMapOf(
        timeStampList[0] to obj1,
        timeStampList[1] to obj2,
        timeStampList[2] to obj3
    )
    var my_map: MutableMap<String, HistoryLogRecord> = findAndReplace<HistoryLogRecord>(obj1, obj2, mutableHashMap)
    println("\nInainte de functia Find And Replace: ")
    for ((ts, objects) in mutableHashMap) {
        println ("$ts - $objects")
    }

    println("\nDupa functia Find And Replace: ")
    for ((ts, objects) in my_map) {
        println ("$ts - $objects")
    }

}


class HistoryLogRecord(tStamp: String, command: String) : Comparable<HistoryLogRecord> {
    val timeStamp = tStamp
    val comm = command

    override fun compareTo(other: HistoryLogRecord): Int {
        //return other.timeStamp.compareTo(timeStamp)

        val ts1 = timeStamp
        val ts2 = other.timeStamp
        val ts1Year = ts1.substring(1,4).toInt() * 31556952
        val ts2Year = ts2.substring(1,4).toInt() * 31556952

        val ts1Month = ts1.substring(5,7).toInt() * 2629746
        val ts2Month = ts2.substring(5,7).toInt() * 2629746

        val ts1Day = ts1.substring(8,10).toInt() * 86400
        val ts2Day = ts2.substring(8,10).toInt() * 86400

        val ts1Hour = ts1.substring(11,13).toInt() * 3600
        val ts2Hour = ts2.substring(11,13).toInt() * 3600

        val ts1Minute = ts1.substring(14,16).toInt() * 60
        val ts2Minute = ts2.substring(14,16).toInt() * 60

        val ts1Second = ts1.substring(14,16).toInt()
        val ts2Second = ts2.substring(14,16).toInt()

        val sumSec1 = ts1Year + ts1Month + ts1Day + ts1Hour + ts1Minute + ts1Second
        val sumSec2 = ts2Year + ts2Month + ts2Day + ts2Hour + ts2Minute + ts2Second

        if (sumSec1 > sumSec2) {
            return 1
        }
        else {
            if (sumSec1 < sumSec2) {
                return -1
            }
            else {
                return 0
            }
        }
    }

}


fun<T: Comparable<T>>maxim(obj1: T, obj2: T) : T {
    val res = obj1.compareTo(obj2)
    if (res >= 0) {
        return obj1;
    }
    else {
        return obj2;
    }
}


fun<T> findAndReplace(searchedObj: HistoryLogRecord, replacedObj: HistoryLogRecord, findReplace: MutableMap<String, T> ) : MutableMap<String, T> {

    val temp = findReplace.toMutableMap()
    if (findReplace.containsKey(searchedObj.timeStamp)) {

        val value = findReplace.getValue(searchedObj.timeStamp)
        //println("Value is $value")
        temp.put(replacedObj.timeStamp, value)
    }
    return temp
}
