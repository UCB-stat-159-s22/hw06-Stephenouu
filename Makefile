.PHONY : env
env:
	bash -i envsetup.sh

.PHONY : html
html:
	jupyter-book build .

.PHONY : html-hub
html-hub:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	cd _build/html
	python -m http.server

.PHONY : clean
clean:
	rm -r figures
	rm -r audio
	rm -rf _build