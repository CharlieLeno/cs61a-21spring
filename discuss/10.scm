(define (factorial x)
  'YOUR-CODE-HERE
    (if (= x 1) 1
        (* x (factorial (- x 1))))
)

(define (fib n)
    'YOUR-CODE-HERE
    (if (< n 2) n
        (+ (fib (- n 1)) (fib (- n 2)))
        )
)

(define (list-concat a b)
    'YOUR-CODE-HERE
    (if (null? (cdr a)) 
        (cons (car a) b)
        (cons (car a) (list-concat (cdr a) b))
    )    
)

(define s '(5 4 (1 2) 3 7))
(define (f s val)
    (if (null? s) nil
        (if (list? (car s))
            (cons (f (car s) val) (f (cdr s) val))
            (if (= (car s) val)
                   (f (cdr s) val)
                   (cons (car s) (f (cdr s) val))
            )
        )
    )
)


(define (duplicate lst)
    'YOUR-CODE-HERE
    (if (null? lst) nil
        (if (list? (car lst))
            (cons (duplicate (car lst)) (duplicate (cdr lst)))
            (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
        )
    )
)


(define (insert element lst index)
   'YOUR-CODE-HERE
   (if (= index 0)
       (cons element lst)
       (cons (car lst) (insert element (cdr lst) (- index 1)))
       )
)

