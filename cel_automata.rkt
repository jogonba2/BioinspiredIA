(define get-vecindario (lambda (i cautomata)
    (if (= i 0) (list (number->string (list-ref cautomata (- (length cautomata) 1))) (number->string (list-ref cautomata i)) (number->string (list-ref cautomata (+ i 1))))
    (if (= i (- (length cautomata) 1)) (list (number->string (list-ref cautomata (- i 1))) (number->string (list-ref cautomata i)) (number->string (list-ref cautomata 0)))
    (list (number->string (list-ref cautomata (- i 1))) (number->string (list-ref cautomata i)) (number->string (list-ref cautomata (+ i 1))))))))

(define aplica-reglas (lambda (vecinos reglas)
    (list-ref reglas (string->number vecinos 2))))

(define cel-automata (lambda (cautomata it reglas res)
    (if (= it 0) res
        (letrec ( (new-cautomata (one-step cautomata '() 0 reglas))
                  (new-res       (append res (list new-cautomata)))
                )
                (cel-automata new-cautomata (- it 1) reglas new-res)
        )
    )
))

(define one-step (lambda (cautomata res i reglas)
    (if (>= i (length cautomata)) res
        (one-step cautomata (append res (list (aplica-reglas (apply string-append (get-vecindario i cautomata)) reglas))) (+ i 1) reglas)    
    )
))
(require (lib "graphics.ss" "graphics"))
(open-graphics)
(define draw-automaton (lambda (cautomata x y)
    (draw-automaton-rec (open-viewport "Cellular automaton 1-dimensional v-moore" 500 500) cautomata x y)
))

(define draw-automaton-rec (lambda (mi-ventana cautomata x y)
    (if (not (null? cautomata))
    (letrec (  (act-pos    (make-posn x y))
               (act-iter   (car cautomata))
            )
            ((draw-string mi-ventana) act-pos (apply string-append (map number->string act-iter)))
            (draw-automaton-rec mi-ventana (cdr cautomata) x (+ y 15))
    ))
))

(draw-automaton (cel-automata '(0 1 1 1 1 0 1) 20 '(1 0 1 0 0 1 1 0) '((0 1 1 1 1 0 1))) 250 10)

