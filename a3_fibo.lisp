(defvar num1 0)
(defvar num2 1)

(princ "limit of fibonacci:")
(setq lim (read))

(defun fibo(lim)
	
	(princ " 0 1")
	(loop 
	   (setq num1 (+ num1 num2))
	   (princ " ")
	   
	   (setq temp num1)
	   (setq num1 num2)
	   (setq num2 temp)
	   
	   (when (> num2 lim) (return lim))
	    (write num2)
	)
)
(if(< lim 1)
	()
	(fibo lim)
	)	
