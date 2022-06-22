Open API:
    localhost:8000

GET the n-th number in the Fibonacci sequence:
    localhost:8000/indput/n
        ~n is the n-th number in sequence

Description:
./app/main.py
    ~contains the GET requests

./app/fibonacci.py
    recur_fibo(n)
        ~recursive function gives the n-th elemnt of the sequence
    fibo_seq(nterms)
        ~function gives back the entire sequence from first to the n-th element by building a string array from them
        ~if the given integer is less than zero it gives an error massage

./Dockerfile
    ~instructions for building the image file

./docker-compose.yml
    ~instructions for building a container from image
    
./requirements.txt
    ~pip freeze > requirements.txt
    ~managing dependencies for python

