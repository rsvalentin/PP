fun main() {
    val list = 1.until(5).toList() // [1, 2, 3, 4]
// filter - returnează doar elementele care îndeplinesc condiția din predicat
            list.filter{ it % 2 == 0 } // [2, 4]
// map - returnează elementele unei colecții după prelucrarea acestora
    list.map{ it * 2 } // [2, 4, 6, 8]
// flatMap - returnează rezultatul concatenării mai multor colecții
    list.flatMap{ listOf(it, it+10) } // [1, 11, 2, 12, 3, 13, 4, 14]
// fold / reduce - acumularea elementelor
    list.fold(0.0) {acc, i -> acc + i } // 10
    list.reduce{ acc, i -> acc * i } // 24
// forEach / onEach - realizează o acțiune pe fiecare element din colecție
    list.forEach{ println(it) } // afișează 1234, returnează Unit
//list.forEach(::println)
    list.onEach{ println(it) } // afișează 1234, returnează [1, 2, 3, 4]
//list.onEach(::println)
// partition - împarte într-o pereche de liste
    val (even, odd) = list.partition{ it % 2 == 0 }
    println(even) // [2, 4]
    println(odd) // [1, 3]
// min, max
    list.min() // 1
    list.max() // 4
// first, firstBy
    list.first() // 1
    list.first{ it % 2 == 0 } // first even: 2
// count - numără elementele care îndeplinesc condiția din predicatlist.count{ it % 2 == 0 } // 2
// sorted, sortedBy - returnează colecția sortată
    listOf(2, 3, 1, 4).sorted() //returnează o nouă listă, sortată: [1, 2, 3, 4]
    list.sortedBy{ it % 2 } // [2, 4, 1, 3]
// groupBy - grupează elementele unei colecții după cheie
    list.groupBy{ it% 2 } // Map: {1=[1, 3], 0=[2, 4]}
// distinct, distinctBy - returnează doar elementele unice
    listOf(1, 1, 1, 2, 2, 3).distinct() // [1, 2, 3]
// drop, dropLast - elimină primele/ultimele n elemente din colecție
    val longList = 1.until(50).toList()
    longList.drop(25) // [26, 27, 28, ..., 49]
    longList.dropLast(25) // [1, 2, 3, ..., 24]
// take, takeLast, takeWhile, takeLastWhile - selectează primele/ultimele n elemente din colecție
    longList.take(25) // [1, 2, 3, ..., 25]
    longList.takeLast(25) // [25, 26, 27, ..., 49]
    longList.takeWhile { it <= 10 } // [1, 2, 3, ..., 10]
    longList.takeLastWhile { it >= 40 } // [40, 41, 42, ..., 49]
// zip - funcția fermoar (zip) ia câte un element din fiecare colecție și formează o pereche
    val list1 = listOf(1,2,3,4,5,6,7,8)
    val list2 = listOf(
        "Item 1", "Item 2","Item 3", "Item 4", "Item 5")
    list1.zip(list2) // [(1, Item 1), (2, Item 2), (3, Item 3), (4, Item 4), (5, Item 5)]
    list1.zipWithNext() // [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
}