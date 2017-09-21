datatype myType = TwoInts of int * int
                | Str of string
                | Pizza

fun f (x : myType) = 
    case x of
            Pizza => 0
        |   Str s => 1
        |   TwoInts (i1, i2) => i1*i2 + i1