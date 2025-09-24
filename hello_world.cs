using System;



string userName = Environment.GetEnvironmentVariable("UserName");
Console.WriteLine($"Hello World, it's {userName}!Today is:{DateTime.Now.ToString()}.");
Console.WriteLine($"Hola Mundo, soy {userName}");
