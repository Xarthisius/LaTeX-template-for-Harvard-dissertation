BNAME=thesis

all: ${BNAME}.pdf

${BNAME}.pdf: ${BNAME}.tex harvard-thesis.cls $(wildcard */*.tex)
	xelatex $<
	bibtex ${BNAME}
	xelatex $<
	xelatex $<

tarball:
	tar cvzf ${BNAME}.tar.gz *

clean:
	rm -rf ${BNAME}.{pdf,log,dvi,aux,out,tgz,bbl,blg}
