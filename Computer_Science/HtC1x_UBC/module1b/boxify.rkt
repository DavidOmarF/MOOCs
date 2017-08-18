;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname boxify) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

; 
; PROBLEM:
; 
; Use the How to Design Functions (HtDF) recipe to design a function that consumes an image, 
; and appears to put a box around it. Note that you can do this by creating an "outline" 
; rectangle that is bigger than the image, and then using overlay to put it on top of the image. 
; For example:
; 
; (boxify (ellipse 60 30 "solid" "red")) should produce .
; 
; Remember, when we say DESIGN, we mean follow the recipe.
; 
; Leave behind commented out versions of the stub and template.
; 


;; Image -> Image
;; Takes an image, and adds a border (outline rectangle with +1 px each side)

;; I don't define test cases because is image, and file is plain text.

;; (define (boxify _IMAGE_) _IMAGE_)        ;stub

;; (define (boxify _IMAGE_)                 ;template
;;    (... _IMAGE_)

(define (boxify img)
  (overlay img
           (rectangle (+ (image-width img) 1)
                      (+ (image-height img) 1)
                      "outline"
                      "black")
           )
  )