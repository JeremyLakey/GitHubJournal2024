object Solution {
    def allCellsDistOrder(rows: Int, cols: Int, rCenter: Int, cCenter: Int): Array[Array[Int]] = {
        val temp: Array[Array[(Int, (Int, Int))]] = (for (
            i <- 0 to (rows - 1)
        ) yield (for (j <- 0 to (cols - 1))
         yield { 
                ((i - rCenter).abs + (j - cCenter).abs, (i, j))
            }).toArray).toArray
        
        val so: Array[(Int, (Int, Int))] = temp.flatten.sortWith((a, b) => a._1 < b._1)
        (for ((_, j: (Int, Int)) <- so) yield {
            Array[Int](j._1, j._2)
        }).toArray
    }
}