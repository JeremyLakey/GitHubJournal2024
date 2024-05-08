object Solution {

    def getMinny(x: Int, quiet: Array[Int], m:scala.collection.mutable.Map[Int, scala.collection.mutable.ArrayBuffer[Int]], cache: scala.collection.mutable.Map[Int, (Int, Int)]): (Int, Int) = {
        var target = x
        var best = quiet(x)
        if (cache.contains(x)) {
            return cache.get(x).getOrElse((0, 0))
        }
        for (j <- m.get(x)) {
            (for (i <- j) yield {
                val tup = getMinny(i, quiet, m, cache)
                if (tup(0) < best) {
                    best = tup(0)
                    target = tup(1)
                }
            })
        }
        cache.addOne((x -> (best, target)))
        (best, target)
    }

    def loudAndRich(richer: Array[Array[Int]], quiet: Array[Int]): Array[Int] = {
        var m = scala.collection.mutable.Map[Int, scala.collection.mutable.ArrayBuffer[Int]]()

        for (r <- richer) {
            if (!m.contains(r(1))) {
                m.addOne(r(1) -> new scala.collection.mutable.ArrayBuffer[Int](0))
            }
            m.get(r(1)).get += r(0)
        }


        var cache = scala.collection.mutable.Map[Int, (Int, Int)]()
        (for (i <- 0 until quiet.length) yield {
            getMinny(i, quiet, m, cache)(1)
        }).toArray
    }
}