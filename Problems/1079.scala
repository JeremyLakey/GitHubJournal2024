object Solution {
    def tr(tiles: String, temp: String, mappy: scala.collection.mutable.Set[String]): Unit = {
        for (c <- tiles) {
            val temp2 = temp + c
            mappy.add(temp2)
            tr(tiles.replaceFirst(c.toString, ""), temp2, mappy)
        }

    }

    def numTilePossibilities(tiles: String): Int = {
        var mappy = scala.collection.mutable.Set[String]()
        tr(tiles, "", mappy)

        return mappy.toArray.size
    }
}