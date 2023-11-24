(define (split-at lst n) 'YOUR-CODE-HERE
    (cond ((null? lst) (cons nil nil))
          ((= n 0) (cons nil lst))
          (#t (cons (cons (car lst) (car (split-at (cdr lst) (- n 1)))) 
              (cdr (split-at (cdr lst) (- n 1)))))
    )
)

(define (compose-all funcs) 'YOUR-CODE-HERE
    (if (null? funcs) (lambda (x) x)
        (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x)))
    )
)
