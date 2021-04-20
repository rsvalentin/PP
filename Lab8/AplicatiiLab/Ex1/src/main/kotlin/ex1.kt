package com.pp.laborator
fun main(args: Array<String>) {
    val snail = Snail()
    val still = Still(snail)
    val a = still.seeHero()
    println(a is Still)
    println(a is Aggressive)
    val b = still.timePassed()
    println(b is Still)
}
class Snail {
    internal var mood: Mood = Still(this)
    private var healthPoints = 10
}
interface WhatCanHappen {
    fun seeHero(): Mood
    fun getHit(pointsOfDamage: Int): Mood
    fun timePassed(): Mood
}
sealed class Mood : WhatCanHappen {
    override fun seeHero() = this
    override fun getHit(pointsOfDamage: Int) = this
    override fun timePassed() = this
}
class Still(private val snail: Snail) : Mood() {
    override fun seeHero(): Mood {
        return snail.mood.run {
            Aggressive(snail)
        }
    }
}
class Aggressive(snail: Snail) : Mood() {
    override fun seeHero(): Mood {
        TODO("not implemented")
    }
    override fun getHit(pointsOfDamage: Int): Mood {
        TODO("not implemented")
    }
    override fun timePassed(): Mood {
        TODO("not implemented")
    }
}
class Retreating : Mood()
class Dead : Mood()