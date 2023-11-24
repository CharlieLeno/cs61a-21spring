(define (sum lst)
  'YOUR-CODE-HERE
    (define (helper lst res)
        (if (nill? lst) res
            (helper (cdr lst) (+ res (car lst))
            )
        )
    )
    (helper lst 0)
)

(sum '(1 2 3))
(sum '(10 -3 4))

(define (reverse lst)
  'YOUR-CODE-HERE
  (define (helper lst res)
    (if (null? lst) res
        (helper (cdr lst) (cons (car lst) res))
    )
  )
  (helper lst nil)
)
(reverse '(1 2 3))
(reverse '(0 9 1 2))

def make_lambda(params, body):
    """
    >>> f = eval(make_lambda("x, y", "x + y"))
    >>> f
    <function <lambda>>
    >>> f(1, 2)
    3
    >>> g = eval(make_lambda("a, b, c", "c if a > b else -c"))
    >>> g(1, 2, 3)
    -3
    >>> eval(make_lambda("f, x, y", "f(x, y)"))(f, 1, 2)
    3
    """
    "*** YOUR CODE HERE ***"
    return f"lambda {params}: {body}"

def if_macro(condition, true_result, false_result):
    """
    >>> eval(if_macro("True", "3", "4"))
    3
    >>> eval(if_macro("0", "'if true'", "'if false'"))
    'if false'
    >>> eval(if_macro("1", "print('true')", "print('false')"))
    true
    >>> eval(if_macro("print('condition')", "print('true_result')", "print('false_result')"))
    condition
    false_result
    """
    "*** YOUR CODE HERE ***"
    return f"{true_result} if {condition} else {false_result}"


scm> (define a +)
a
scm> (define b 1)
b
scm> (define c 2)
c
scm> `(a b c)
(a b c)
scm> `(a ,b c)
(a 1 c)
scm> (a b c)
3
scm> `(a `(b ,b) c)
(a (quasiquote (b (unquote b))) c)
scm> `(a (b ,b) c)
(a (b 1) c)
scm> `(a ,(a b c) c)
(a 3 c)
scm> (define condition '(= 1 1))
condition
scm> (define if-true '(print 3))
if-true
scm> (define if-false '(print 5))
if-false
scm> `(if ,condition ,if-true ,if-false)
(if (= 1 1) (print 3) (print 5))


(define (if-function condition if-true if-false)
  'YOUR-CODE-HERE
  `(if ,condition ,if-true ,if-false)
)

(define-macro (if-macro condition if-true if-false)
  'YOUR-CODE-HERE
  `(eval (if ,condition ,if-true ,if-false))
)

