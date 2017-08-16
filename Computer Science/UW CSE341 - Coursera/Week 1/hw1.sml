fun is_older (a : (int*int*int), b : int*int*int) =
    (* a and b are dates in format: ( _YEAR_ , _MONTH_ , _DAY_ ) *)

    (* If years are not equal, one of them must been before *)
    if #1 a <> #1 b
        then #1 a < #1 b 

    (* ====== Years are equal ====== *)
    (* If months are not equal, one of them must been before*)
    else if #2 a <> #2 b
        then #2 a < #2 b

    (* ====== Months are equal ====== *)
    (* Only true if a_day is lower than b_day *)
    else #3 a < #3 b

fun number_in_month (dates : (int*int*int) list, month : int) = 
    (* dates = [] is edge case*)
    if dates = []
        then 0
    else
        (* Compares the second element on the first date on dates list with the given month *)
        if #2 (hd dates) = month
            (* Adds one if they are equal *)
            then 1 + number_in_month(tl dates, month)
        (* Calls itself again with the tail of dates list *)
        else number_in_month(tl dates, month)

fun number_in_months (dates: (int*int*int) list, months : int list) = 
    (* months = [] is edge case *)
    if months = []
        then 0
    else number_in_month(dates, hd months) + number_in_months(dates, tl months)

fun dates_in_month (dates: (int*int*int) list, month: int) = 
    (* dates = [] is edge case *)
    if dates = []
        then []
    else 
        (* compare month of current date, with given month *)
        if #2 (hd dates) = month
            (* add date at beginning of list, to all the other dates with that month *)
            then hd dates :: dates_in_month(tl dates, month)
        else dates_in_month(tl dates, month)

fun dates_in_months (dates: (int*int*int) list, months: int list) = 
    (* months = [] is edge case *)
    if months = []
    then []
    else 
        (* concatenate all the dates in one month, with all the dates in all the other months *)
        dates_in_month(dates, hd months) @ dates_in_months (dates, tl months)

fun get_nth (words: string list, nth: int) = 
    (* words = [] is edge case *)
    if words = []
    then ""
    else 
        (* once we did 'nth' recursive calls, return head of words *)
        if nth = 1
            then hd words
        (* call with tail of words, and nth = nth - 1 *)
        else get_nth(tl words, nth-1)

fun date_to_string (date: (int*int*int)) = 
    let 
        val months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October","November", "December"]
    in
        (List.nth (months, (#2 date) - 1) ) ^ " " ^ (Int.toString (#3 date)) ^ ", " ^ (Int.toString (#1 date))
    end

fun number_before_reaching_sum (sum: int, xs: int list) = 
    (* Adds one to the return everytime "sum - hd xs (and all the values previous to 
        that one" is greater than 0 *)
    if (sum - hd xs) <= 0
        then 0
    else 1 + number_before_reaching_sum((sum - hd xs), tl xs)

fun what_month (day: int) = 
    let 
        val monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    in 
        (* Adds one, because we want the month in which the day **falls** *)
        number_before_reaching_sum(day, monthDays) + 1
    end

fun month_range (day1 : int, day2 : int) = 
    if day1 > day2
        then []
    (* I think this solution isn't as efficient as can be: It calls
        'what_month' every recursion. 
        Maybe a solution would be to add 'critic' days
            (e.g: 31 evaluates to 1, 32 to 2.
                59 eveluates to 2, 60 to 3.)
        And make this function "push" 
        1 for all integers between 1 and 31 inclusive., 
        2 for all values between 32 and 59, inclusive, etc...*)
    else what_month day1 :: month_range (day1+1, day2)

fun oldest (dates : (int*int*int) list) =
    if dates = []
        then NONE
    else if tl dates = []
        then SOME (hd dates)
    else 
        (* get the oldest in the tail *)
        let val tl_oldest = oldest (tl dates)
        in
            if (isSome tl_oldest) (* if tl_oldest isn't NONE *)
                    (* and the head of dates is older than the value in tl_oldest *) 
                    andalso is_older(hd dates, valOf(tl_oldest))
            then SOME (hd dates) (*return SOME head of dates*)
            else tl_oldest (* return tl_oldest *)
        end


(*

===== PENDING ======
Challenge Problem: Write functions number_in_months_challenge and dates_in_months_challenge
that are like your solutions to problems 3 and 5 except having a month in the second argument multiple
times has no more effect than having it once. (Hint: Remove duplicates, then use previous work.)
13. 

Challenge Problem: Write a function reasonable_date that takes a date and determines if it
describes a real date in the common era. A “real date” has a positive year (year 0 did not exist), a
month between 1 and 12, and a day appropriate for the month. Solutions should properly handle leap
years. Leap years are years that are either divisible by 400 or divisible by 4 but not divisible by 100.
(Do not worry about days possibly lost in the conversion to the Gregorian calendar in the Late 1500s.)
*)