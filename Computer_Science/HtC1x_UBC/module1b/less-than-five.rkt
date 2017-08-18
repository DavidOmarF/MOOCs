;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname less-than-five) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; 
; PROBLEM:
; 
; DESIGN function that consumes a string and determines whether its length is
; less than 5.  Follow the HtDF recipe and leave behind commented out versions 
; of the stub and template.
; 


;; String -> Boolean
;; Takes a string, and returns 5 iff its length is less than 5

(check-expect (isLess5 "1234") true)
(check-expect (isLess5 "12345") false)
(check-expect (isLess5 "123456") false)

;; (define (isLess5 s) false)        ;stub

;; (define (isLess5 s)               ;template
;;  (... s))


(define (isLess5 s)
  (< (string-length s) 5)
  )