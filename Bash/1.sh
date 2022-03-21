
# 1) ****
#    ****
#    ****
#    ****

# i=0
# while [ $i -lt 5 ];
# do
#     for j in {1..$i}:
#     do
#         echo -n "*"
#     done
#     echo ""
#     ((i++))
# done

# 2) 1111
#    2222
#    3333
#    4444


# for i in {1..4};
# do
#     for j in {1..4};
#     do
#         echo -n "$i"
#     done
#     echo ""
# done

# 3) Sum of natural numbers
# num=0
# echo "Enter limit: "
# read limit
# for ((i=1; i<=$limit; i++));
# do
#     ((num=num+i))
# done
# echo $num

# 4) Factorial

 echo "Enter limit: "
 read limit
 num=1
 for ((i=1; i<=$limit; i++))
 do
     ((num = num * i))
 done
 echo $num


