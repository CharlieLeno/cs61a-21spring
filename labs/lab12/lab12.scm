(define (tail-replicate x n) 'YOUR-CODE-HERE
  (define (helper x n res)
          (if (= n 0) res
              (helper x (- n 1) (cons x res))
          )
  )
  (helper x n nil)
)

(define-macro (def func args body)
  'YOUR-CODE-HERE
  `(define ,(cons func args) ,body
  )  
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))
