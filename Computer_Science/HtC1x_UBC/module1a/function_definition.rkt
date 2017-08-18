;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname function2) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

; 
; PROBLEM:
; 
; Write a function that consumes two numbers and produces the larger of the two. 
; 


(define (max_fun a b)
  (if(> a b)
     a
     b
     )
  )
