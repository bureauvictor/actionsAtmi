using System;

class Program{
    static void Main(string[] args){

        string userName = Environment.UserName;
        Console.WriteLine($"Hello World, it's {userName}!Today is:{DateTime.Now.ToString()}.");
        Console.WriteLine($"Hola Mundo, soy {userName}");
    }
}
