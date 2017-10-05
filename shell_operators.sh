#!/bin/bash

#6. piemērs loģiskas operācijas
if [ $# == 2 ]
then
#5. piemērs ar argumentiem no arpuses
a=$1
b=$2
val51=`expr $a + $b`
echo "$a + $b  ="$val51
val52=`expr $a - $b`
echo "$a - $b ="$val52
val53=`expr $a / $b`
echo "$a / $b ="$val53
val54=`expr $a \* $b`
echo "$a * $b ="$val54
val56=`expr $a % $b`
echo "$a % $b ="$val56
fi

#4. piemērs
#a=30
#b=10
#val21=`expr $a + $b`
#echo "$a + $b  ="$val21
#val22=`expr $a - $b`
#echo "$a - $b ="$val22
#val23=`expr $a / $b`
#echo "$a / $b ="$val23
#val24=`expr $a \* $b`
#echo "$a * $b ="$val24
#val26=`expr $a % $b`
#echo "$a % $b ="$val26

#3. piemers
#val31=`expr 2 + 3`
#echo "2 + 3 ="$val31
#val32=`expr 2 - 3`
#echo "2 - 3 ="$val32
#val33=`expr 2 / 3`
#echo "2 / 3 ="$val33
#val34=`expr 2 \* 3`
#echo "2 * 3 ="$val34
#val331=`expr 5 / 3`
#echo "5 / 3 ="$val331
#val332=`expr 5 % 3`
#echo "5 % 3 ="$val332
#val343=`expr 999 / 1000`
#echo "999 / 1000 ="$val343



#2. piemērs
#val1=`expr 2+2`
#echo "NNepareasti apostrofi bez attarpem "$val1
#val2='expr 2+2'
#echo "Parasti apostrofi bez atstarpem "$val2
#val3=`expr 2 + 2`
#echo "Nepareasti apostrofi atstarpem "$val3
#val4='expr 2 + 2'
#echo "Parasti apostrofi ar atstarpem "$val4


#1. piemērs

#val=`expr 2 + 2`
#echo "Total value : $val"
