(define (cddr s) (cdr (cdr s)))

(define (cadr s) 'YOUR-CODE-HERE
    (car (cdr s))
)

(define (caddr s) 'YOUR-CODE-HERE
    (car (cdr (cdr s)))
)

(define (sign val) 'YOUR-CODE-HERE
    (cond ((< val 0) -1)
          ((= val 0) 0)
          ((> val 0) 1)
    )
)

(define (square x) (* x x))

(define (pow base exp) 'YOUR-CODE-HERE
    (cond ((= base 1) base)
          ((= exp 1) base)
          ((even? exp) (pow (square base) (/ exp 2)))
          (else (* base (pow base (- exp 1))))
    )
)
