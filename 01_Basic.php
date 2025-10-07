<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <?php

    Define("Pi",3.14);
    $Lucky = 10;
    $Aman = 50;


    /* All Operators-

       Arithmetic Operators
       Logical Operators
       Assignment Operators
       Comparison Operators 
       Increment and Decrement Operators

    */
    //    //  Arithmetic Operators
    //    echo "The sume of Lucky and Aman is ";
    //    echo $Aman+$Lucky;
    //    echo "<br>";                // For Sum
    //    echo $Aman-$Lucky;          // For Subtraction
    //    echo "<br>"; 
    //    echo $Aman*$Lucky;
    //    echo "<br>";                // For Multiplication
    //    echo $Aman/$Lucky;
    //    echo "<br>";               // For Division
    
      // Assignment Operators

    //   $Neelkant = $Aman;
    //   $Neelkant += 1;
    //   echo "Neelkant now has more power than Aman ";
    //   echo $Neelkant;
    //   echo "<br>";
      
    //   echo "Because Aman Only got ";
    //   echo $Aman;
    //   echo "<br>";


    // $Neelkant = $Aman;
    // $Neelkant += 20;
    // $Neelkant /= $Lucky;
    // echo "The Power Neelkant has when divided by Lucky becomes ";
    // echo $Neelkant;
    // echo "<br>";

      // Increment and Decrement Operators

    // $Aman++;
    // echo $Aman;
    // echo "<br>";
    
    // $Lucky--;
    // echo $Lucky;
    // echo "<br>";

      //Logical Operators 
      /*
      and
      or
      xor
      ! (known as not) 
      */
    
    // $Newone = (true and true);
    // echo $Newone;  
    // echo "<br>";

    // $Newone = (false and true);
    // echo var_dump($Newone); 
    // echo "<br>";
      
    // $JJ = (true xor true);
    // echo var_dump($JJ);
    // echo "<br>";


    // $KK = (true xor False);
    // echo var_dump($KK);
    // echo "<br>";

    // $HH = (false xor false);
    // echo var_dump($HH);
    // echo "<br>";

    // $GG = (False xor True);
    // echo var_dump($GG);
    // echo "<br>";
    
    /*
    Data Types -

    String
    Integer
    Float
    Object
    Null
    Array 
    Boolean
    */
       
    $Name = "Lucky";
    echo var_dump($Name);
    echo "<br>"; 

    $Number = 120;
    echo var_dump($Number);
    echo "<br>";

    $Decimal = 20.01;
    echo var_dump($Decimal);
    echo "<br>";

    $Boolean = !true; //have used not function.
    echo var_dump($Boolean);
    echo "<br>";
    
    echo Pi;  // recalling the above Defined value here


    $Friends = ["Aman",10,"Boy",55];


    ?>
  
</body>
</html>