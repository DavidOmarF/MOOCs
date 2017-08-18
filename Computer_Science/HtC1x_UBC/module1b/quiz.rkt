;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname quiz) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;; Image, Image -> Boolean
;; Produces true iff the first image received is larger than the second

(check-expect(isLarger (rectangle 10 20 "solid" "red") (rectangle 10 15 "solid" "red")) true)
(check-expect(isLarger (rectangle 10 10 "solid" "red") (rectangle 10 15 "solid" "red")) false)
(check-expect(isLarger (rectangle 10 15 "solid" "red") (rectangle 10 15 "solid" "red")) false)

;; (define (isLarger img1 img2) false)     ; stub

;; (define (isLarger img1 img2)            ; template
;;    (... img1)
;;    (... img2))

(define (isLarger img1 img2)
  (> (* (image-height img1)
        (image-width img1))
     (* (image-height img2)
        (image-width img2))
     )
  )