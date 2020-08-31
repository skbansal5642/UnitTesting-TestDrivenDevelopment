IAM  := tdd
VENV := venv.${IAM}/bin/activate
ACT  := . ${VENV} &&

venv.${IAM} : ${VENV} requirements.txt
	touch $@

${VENV} :
	python3 -m venv venv.${IAM}
	${ACT} python3 venv.${IAM}/bin/pip install --upgrade pip
	${ACT} python3 venv.${IAM}/bin/pip install --requirement requirements.txt

test : ${VENV}
	${ACT} pytest

clean :
	rm -rfv venv.${IAM}
	find * -name '*~' | sort | while read t ; do rm -v "$${t}" ; done

