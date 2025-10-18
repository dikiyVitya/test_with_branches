package main

import (
    "bufio"
    "os"
    "fmt"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin) // создаем экземпляр структуры bufio.Scanner для чтения из консоли
    fmt.Println("Введите строку с пробелами:")
    _ = scanner.Scan() // ожидает ввод строки с клавиатуры до нажатия Enter
    name := scanner.Text() // сохраняем введенную строку целиком в переменную name
    fmt.Println("Вы ввели:", name)
}
