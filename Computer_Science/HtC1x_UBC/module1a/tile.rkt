;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname tile) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

(require 2htdp/image)

; 
; PROBLEM:
; 
; Use the DrRacket square, beside and above functions to create an image like this one:
; (* Blue   | Yellow
;    Yellow | Blue*)
; 


(above (beside (square 20 "solid" "blue")
                (square 20 "solid" "yellow")
                )
       (beside (square 20 "solid" "yellow")
                (square 20 "solid" "blue")
                )
       )