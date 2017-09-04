;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname booleans) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

; 
; PROBLEM:
; 
; Based on the two constants provided, write three expressions to determine whether: 
; 
; 1) IMAGE1 is taller than IMAGE2
; 2) IMAGE1 is narrower than IMAGE2
; 3) IMAGE1 has both the same width AND height as IMAGE2
; 


(define IMAGE1 (rectangle 10 15 "solid" "red"))
(define IMAGE2 (rectangle 15 10 "solid" "red"))

(> (image-height IMAGE1) (image-height IMAGE2))
(< (image-width IMAGE1)(image-width IMAGE2))
(and (equal? (image-height IMAGE1)
             (image-height IMAGE2))
     (equal? (image-width IMAGE1)
             (image-width IMAGE2))