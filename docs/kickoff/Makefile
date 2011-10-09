SRC=praesentation.tex
DST=praesentation.pdf

all: $(DST)

$(DST): $(SRC) *.tex
	pdflatex $(SRC)
	pdflatex $(SRC)
	pdflatex $(SRC)

clean:
	rm -f *.aux *.log *.idx *.toc *.dvi *.bbl *.blg *.lof *.nav *.out *.snm
