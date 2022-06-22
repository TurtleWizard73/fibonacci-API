# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

def fibo_seq(nterms):
    fibseq = ""
    if nterms <= 0:
        fibseq = "Plese enter a positive integer between 0 and 100"
    else:
        fibseq = "Fibonacci sequence:"
        for i in range(nterms):
            fibseq += " "
            fibseq += str(recur_fibo(i))
    return(fibseq)

##################################################################
#nterms = input("Enter positive integer and hit enter ")
#nterms = int(nterms)

# check if the number of terms is valid
#if nterms <= 0:
#   print("Plese enter a positive integer")
#else:
#   print("Fibonacci sequence:")
#   for i in range(nterms):
#       print(recur_fibo(i))
