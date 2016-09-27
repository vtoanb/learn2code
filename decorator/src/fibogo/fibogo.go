package main

import "fmt"
import "time"

func main() {
    start := time.Now()
    f := fibonaci(45)
    t := time.Since(start)
    fmt.Println(f,t)
}

func fibonaci(n int) int{
    if n == 0 {return 0}
    if n == 1 {return 1}
    return fibonaci(n-1) + fibonaci(n-2)
}
