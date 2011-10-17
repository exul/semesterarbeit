src_praesentation=praesentation.tex
dst_praesentation=praesentation.pdf

src_protokoll=protokoll.tex
dst_protokoll=protokoll.pdf

protokoll: $(dst_protokoll)

$(dst_protokoll): $(src_protokoll) *.tex
	pdflatex $(src_protokoll)
	pdflatex $(src_protokoll)
	pdflatex $(src_protokoll)

praesentation: $(dst_praesentation)
$(dst_praesentation): $(src_praesentation) *.tex
	pdflatex $(src_praesentation)
	pdflatex $(src_praesentation)
	pdflatex $(src_praesentation)

clean:
	rm -f *.aux *.log *.idx *.toc *.dvi *.bbl *.blg *.lof *.nav *.out *.snm
