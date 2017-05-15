;facrotial using recursive function

(princ "Enter number: ")
	(setq N (read))

(defun fact (N)
	(	if(= N 1)
		1
		(	if(= N 0)
			1
			(	if(< N 0)
				(print "Can't Do That")
				(* N (fact(- N 1)))
			)
		)
	)
)

(princ "Facorial is : ")
(write (fact N))
